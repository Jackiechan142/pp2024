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
    # input mark  of each student in this course.
    def mark(self,student,stdscr):
        stdscr.clear()
        try:
            i= True
            while (i):
                stdscr.addstr(0,10,"Student you want to add.\n")
                sid = Box.makebox(stdscr,"ID",1,20,2,2)
                stdscr.refresh()
                sid.edit()
                count = 0
                for j in range(len(student)):
                    if(sid.gather() == student[j].id):
                        mark = Box.makebox(stdscr,"Mark",1,20,4,2)
                        stdscr.refresh()
                        mark.edit()
                        try:
                           e = float(mark.gather())
                        except ValueError:
                           stdscr.addstr(8,2,"Wrong type of input in credict, please try again.")
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
                    stdscr.addstr(8,8,"This ID not found.")
                
                while(True):
                 try:
                   stdscr.addstr(10,25,"Do you want to continue? Y/N:\n ")
                   stdscr.refresh()
                   chose = stdscr.getch()
                   if (chose ==ord("N") or chose == ord("n")):
                     i=False
                     break
                   elif(chose != ord("Y") or chose !=ord("y")):
                    break
                 except ValueError:
                    stdscr.addstr(20,25,"Wrong type of input, please try again.")
        except ValueError:
            stdscr.addstr(20,25,"Wrong type of input, please try again.")
            Course.mark(student)
    # print mark of all student in this cousre
    def print(self,stdscr):
        stdscr.clear()
        stdscr.addstr(0,2,f"Course: {self.name} \t ID: {self.id} \t Credict: {self.credict}")
        stdscr.addstr(1,2,f"{'Number':<5}{'ID':<15}{'Name':<30}{'Mark':<5}")
        stdscr.addstr(3,2,"="*55)
        row = 4
        for i in range(len(self.markcour)):
           stdscr.addstr(row,2,f"{i:<5}{self.markcour[i].id:<15}{self.markcour[i].name:<30}{self.markcour[i].mark}")
           row +=2
# create a child class of class Course
class mark_of_student(Course):
    def __init__(self, id, name,credict,point):
        super().__init__(id, name, credict)
        self.point = point
    def __str__(self):
        return f" ID of course: {self.id} \t Name of course: {self.name} \t Credict: {self.credict} \t Mark: {self.point}"
