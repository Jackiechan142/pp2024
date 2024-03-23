import math
import os
import zipfile
import numpy as np
import pickle
import Box
import output as op
def round_down(number):
    a = number*10
    newnumber= float(math.floor(a)/10)
    return newnumber
# calculate the GPA 
def cla_GPA(mark, credict):
    result = float(mark * credict)
    return result

# remove student
def remove_student(stud,cour):
    for i in range(len(cour)):
        for j in range(len(cour[i].markcour)):
           if stud.id == cour[i].markcour[j].id:
               cour[i].markcour = np.delete(cour[i].markcour,j)
               break
def remove_course(cour,stud):
    for i in range(len(stud)):
        for j in range(len(stud[i].mark)):
            if cour.id == stud[i].mark[j].id:
                stud[i].mark = np.delete(stud[i].mark,j)
                break

# check duplicate ID:
def check_ID(id,clas):
    for i in range(len(clas)):
        if id == clas[i].id:
            return True
    return False

# write to file student.txt
def write_file(student):
    with open("students.txt","wb") as file:
        for i in range(len(student)): 
             pickle.dump(student[i],file)

# write to file courses.txt
def print_file(course):
    with open('courses.txt','wb') as file:
        for i in range(len(course)):
            pickle.dump(course[i],file)
  
# write to file marks.txt
def write_mark(courese):
    with open('marks.txt','wb') as file:
        for i in range(len(courese)):
            pickle.dump(courese[i],file)
            for j in range(len(courese[i].markcour)):
                pickle.dump(courese[i].markcour[j],file)

# create a Zipfile Object:
def zip_file():
   zp = "Students.dat"
   fz = ["students.txt","courses.txt","marks.txt"]
   with zipfile.ZipFile(zp,'w') as zip_ref:
       for f in fz:
           zip_ref.write(f)
           os.remove(f)
   print("Zip file created succesfully.")



# function to choice what you want to show: student or course?
def show_choice(stdscr,student,course):
    stdscr.clear()
    stdscr.addstr(1,2,"1. Show information of all Students.")
    stdscr.addstr(2,2,"2. Show information of all Courses.")
    stdscr.addstr(3,2,"Your choice:")
    stdscr.refresh()
    choice = stdscr.getch()
    if choice == ord('1'):
        op.print_student_infor(student,stdscr)
    elif choice == ord('2'):
        op.print_course_infor(course,stdscr)  
    else:
         stdscr.refresh()
         stdscr.addstr(18,25,"Press any key to continue ...")
         stdscr.getch()

# Check if this student have mark before.
def check_mark(id,markcour):
    for i in range(len(markcour)):
        if id == markcour[i].id:
            return True
    return False

# fix mark for student.
def Fix_point(stdscr,course,student):
    stdscr.clear()
    stdscr.addstr(1,2,"ID of course you want to fix point.")
    coufix = Box.makebox(stdscr,"ID of Course",1,20,2,2)
    stdscr.refresh()
    coufix.edit()
    while True:
        if coufix.gather().strip() =="":
            stdscr.addstr(8,2,"please fill in ID of Course flied.")
            stdscr.refresh()
            coufix.edit()
        else:
            break
    for i in range(len(course)):
        if coufix.gather() == course[i].id:
            stdscr.clear()
            stdscr.addstr(0,1,"ID of student you want to fix mark.")
            idbox = Box.makebox(stdscr,"ID of Student",1,20,2,2)
            stdscr.refresh()
            idbox.edit()
            while True:
                if idbox.gather().strip() == "":
                    stdscr.addstr(10,10,"Please fill in ID of Student flied.")
                    stdscr.refresh()
                    idbox.edit()
                else:
                    break
            if check_ID(idbox.gather(),student) == True:
                course[i].fix_mark(stdscr,idbox.gather(),student)

def fix_student(stdscr,student,course):
    stdscr.clear()
    stdscr.addstr(1,2,"1. Fix the Name of Student.")
    stdscr.addstr(2,2,"2. Fix the Dob of Student.")
    stdscr.refresh()
    choice = stdscr.getch()
    if choice == ord('1'):
        stdscr.clear()
        nameBox = Box.makebox(stdscr,"Name",1,20,2,2)
        stdscr.refresh()
        nameBox.edit()
        while True:
            if nameBox.gather().strip() =="":
                stdscr.addstr(10,10,"Please fill in Name field!")
                stdscr.refresh()
                nameBox.edit()
            else:
                student.setName(nameBox.gather())
                for i in range(len(course)):
                    for j in range(len(course[i].markcour)):
                         if student.id == course[i].markcour[j].id:
                             course[i].markcour[j].setName(nameBox.gather())
                             break
                stdscr.addstr(10,10,"Name of Student was fix done!")
                stdscr.refresh()
                stdscr.addstr(18,25,"Press any key to continue ...")
                stdscr.getch()
                break
    elif choice == ord('2'):
        stdscr.clear()
        DobBox = Box.makebox(stdscr,"Dob",1,20,2,2)
        stdscr.refresh()
        DobBox.edit()
        while True:
            if DobBox.gather().strip() =="":
                stdscr.addstr(10,10,"Please fill in Dob field!")
                stdscr.refresh()
                DobBox.edit()
            else:
                student.setDob(DobBox.gather())
                for i in range(len(course)):
                    for j in range(len(course[i].markcour)):
                         if student.id == course[i].markcour[j].id:
                             course[i].markcour[j].setDob(DobBoxBox.gather())
                             break
                stdscr.addstr(10,10,"Dob of Student was fix done!")
                stdscr.refresh()
                stdscr.addstr(18,25,"Press any key to continue ...")
                stdscr.getch()
                break
    else:
        stdscr.addstr(8,2,"Wrong type of input in credict, please try again from menu.")
        stdscr.refresh()
        stdscr.getch()
def fix_course(stdscr,course,student):
    stdscr.clear()
    stdscr.addstr(1,2,"1. Fix the Name of Course.")
    stdscr.addstr(2,2,"2. Fix the credict of Course.")
    stdscr.refresh()
    choice = stdscr.getch()
    if choice == ord('1'):
        stdscr.clear()
        nameBox = Box.makebox(stdscr,"Name",1,20,2,2)
        stdscr.refresh()
        nameBox.edit()
        while True:
            if nameBox.gather().strip() =="":
                stdscr.addstr(10,10,"Please fill in Name field!")
                stdscr.refresh()
                nameBox.edit()
            else:
                course.setName(nameBox.gather())
                for i in range(len(student)):
                    for j in range(len(student[i].mark)):
                        if course.id == student[i].mark[j].id:
                            student[i].mark[j].setName(nameBox.gather())
                            break
                stdscr.addstr(10,10,"Name of Course was fix done!")
                stdscr.refresh()
                stdscr.addstr(18,25,"Press any key to continue ...")
                stdscr.getch()
                break
    elif choice == ord('2'):
        stdscr.clear()
        creBox = Box.makebox(stdscr,"Credict",1,20,2,2)
        stdscr.refresh()
        creBox.edit()
        t = True
        while t:
            if creBox.gather().strip() =="":
                stdscr.addstr(10,10,"Please fill in Credict field!")
                stdscr.refresh()
                creBox.edit()
            while creBox.gather().strip() != "":
                try:
                    c = int(creBox.gather())
                    course.setCredict(c)
                    for i in range(len(student)):
                      for j in range(len(student[i].mark)):
                        if course.id == student[i].mark[j].id:
                            student[i].mark[j].setCredict(c)
                            break
                    stdscr.addstr(10,10,"Credict of Course was fix done!")
                    t= False
                    break
                except ValueError:
                    stdscr.addstr(10,10,"Wrong type of input in credict, please try again.")
                    stdscr.refresh()
                    creBox.edit()
        stdscr.refresh()
        stdscr.addstr(18,25,"Press any key to continue ...")
        stdscr.getch()
    else:
        stdscr.addstr(8,2,"Wrong type of input in credict, please try again from menu.")
        stdscr.refresh()
        stdscr.getch()
