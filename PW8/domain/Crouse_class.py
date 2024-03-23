import function as fc
from domain import Student_class as sc
import numpy as np
import Box
# make class Crouse
class Course:
    def __init__(self, id, name,credict,):
        self.id = id
        self.name = name 
        self.credict = credict
        self.markcour = np.array([])
    def __str__(self):
        return f" Id: {self.id} \n Name: {self.name} \n Credict: {self.credict} \n ================================================= \n"
    def getName(self):
        return self.name
    def setName(self,name):
        self.name = name
    def getCredict(self):
        return self.credict
    def setCredict(self,credict):
        self.credict = credict

    # input mark  of each student in this course.
    def mark(self,student,stdscr):
        stdscr.clear()
        try:
            t= True
            stdscr.addstr(2,0,f"{'ID':<15}{'Name':<30}{'Dob':<15}")
            stdscr.addstr(3,0,"-"*60)
            row = 4
            for i in range(len(student)):
                stdscr.addstr(row,0,f"{student[i].id:<15}{student[i].name:<30}{student[i].Dob:<15}")
                row +=2
            while (t):
                stdscr.addstr(0,10,"Student you want to add.\n")
                sid = Box.makebox(stdscr,"ID",1,20,row +4,2)
                stdscr.refresh()
                sid.edit()
                count = 0
                for j in range(len(student)):
                    if(sid.gather() == student[j].id):
                        if fc.check_mark(student[j].id, self.markcour) == True:
                           stdscr.addstr(10,2,"This Student have mark in this Course before, please choice other option.")
                           break
                        mark = Box.makebox(stdscr,"Mark",1,20,row +6,2)
                        stdscr.refresh()
                        mark.edit()
                        try:
                           e = float(mark.gather())
                        except ValueError:
                           stdscr.addstr(row +8,2,"Wrong type of input in credict, please try again.")
                           stdscr.refresh()
                           mark.edit()
                        a = fc.round_down(e)
                        b = student[j].id
                        c = student[j].name
                        d = student[j].Dob
                        point = sc.mark_in_course(b,c,d,a)
                        self.markcour = np.append(self.markcour,point)
                        student[j].point(self.id, self.name,a,self.credict)
                    else:
                        count +=1
                if (count == len(student)):
                    stdscr.addstr(row+10,8,"This ID is not exists.")
                
                while(True):
                 try:
                   stdscr.addstr(row+14,25,"Do you want to continue? Y/N:\n ")
                   stdscr.refresh()
                   chose = stdscr.getch()
                   if (chose ==ord("N") or chose == ord("n")):
                     t=False
                     break
                   elif(chose != ord("Y") or chose !=ord("y")):
                    break
                 except ValueError:
                    stdscr.addstr(row + 16,25,"Wrong type of input, please try again.")
        except ValueError:
            stdscr.addstr(row +16,25,"Wrong type of input, please try again.")
            Course.mark(student)
    # print mark of all student in this cousre
    def print(self,stdscr):
      try:
        stdscr.clear()
        stdscr.addstr(0,2,f"Course: {self.name} \t ID: {self.id} \t Credict: {self.credict}")
        stdscr.addstr(1,2,f"{'No.':<5}{'ID':<15}{'Name':<30}{'Mark':<5}")
        stdscr.addstr(3,2,"="*55)
        row = 4
        for i in range(len(self.markcour)):
           stdscr.addstr(row,2,f"{i+1:<5}{self.markcour[i].id:<15}{self.markcour[i].name:<30}{self.markcour[i].mark:<5}")
           row +=2
      except EOFError:
         print("Something wrong or not work.")
#    fix makr in course
    def fix_mark(self,stdscr,id,student):
       stdscr.clear()
       stdscr.addstr(4,2,"Mark of this Student you want to fix: ")
       for j in range(len(student)):
          if student[j].id == id:
               if fc.check_mark(id,self.markcour) == True:
                  for i in range(len(self.markcour)):
                     if id == self.markcour[i].id :
                         fix = Box.makebox(stdscr,"Mark",1,20,6,2)
                         stdscr.refresh()
                         fix.edit()
                         while True:
                              if fix.gather().strip() =="":
                                   stdscr.addstr(8,2,"Please fill in Mark field!")
                                   stdscr.refresh()
                                   fix.edit()
                              elif fix.gather().strip()!="":
                                    try:
                                       a = float(fix.gather().strip())
                                       break
                                    except ValueError:
                                        stdscr.addstr(9,2,"Wrong type of input, please try again.")
                                        stdscr.refresh()
                                        fix.edit()
                              else:
                                    break
                         self.markcour[i].set_mark(fc.round_down(a))
                         student[j].refe_point(fc.round_down(a),self.id)
                         stdscr.addstr(10,2,"Fix mark for this Student is done.")
       stdscr.refresh()
       stdscr.addstr(18,25,"Press any key to continue ..........")
       stdscr.getch()

# create a child class of class Course
class mark_of_student(Course):
    def __init__(self, id, name,credict,point):
        super().__init__(id, name, credict)
        self.point = point
    def setName(self,name):
        self.name = name
    def setCredict(self,credict):
        self.credict = credict
    def __str__(self):
        return f" ID of course: {self.id} \t Name of course: {self.name} \t Credict: {self.credict} \t Mark: {self.point}"
    def set_point(self, point):
       self.point = point
    def get_point(self):
       return self.point
