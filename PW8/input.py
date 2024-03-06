from domain import Student_class as sc
from domain import Crouse_class as cc
import numpy as np
import Box
# input data of student
def input_student(stdscr): 
       stdscr.clear()
       IdBox = Box.makebox(stdscr,"ID",1,20,2,2)
       NameBox = Box.makebox(stdscr,"Name",1,20,4,2)
       DobBox = Box.makebox(stdscr,"Dob",1,20,6,2)
       stdscr.refresh()
       IdBox.edit()
       NameBox.edit()
       DobBox.edit()
       while True:
         if IdBox.gather().strip() == "":
            stdscr.addstr(8,2,"Please fill in Id fields!")
            stdscr.refresh()
            IdBox.edit()
         elif NameBox.gather().strip() == "":
            stdscr.addstr(8,2,"Please fill in Name fields!")
            stdscr.refresh()
            NameBox.edit()
         elif DobBox.gather().strip() == "":
            stdscr.addstr(8,2,"Please fill in DoB fields!")
            stdscr.refresh()
            DobBox.edit()
         else:
            break
       
       stu = sc.Student(IdBox.gather(),NameBox.gather(),DobBox.gather())  
       return stu
   
# input data of cousre
def input_Course(stdscr):
      stdscr.clear()
      id = Box.makebox(stdscr,"Course ID", 1,20,2,2)
      name = Box.makebox(stdscr,"Course Name",1,20,4,2)
      credict = Box.makebox(stdscr,"Course credict",1,20,6,2)
      stdscr.refresh()
      id.edit()
      name.edit()
      credict.edit()
      t= True
      while t:
         if id.gather().strip() == "":
            stdscr.addstr(8,2,"Please fill in Course ID fields!")
            stdscr.refresh()
            id.edit()
         elif name.gather().strip() == "":
            stdscr.addstr(8,2,"Please fill in Course Name fields!")
            stdscr.refresh()
            name.edit()
         elif credict.gather().strip() == "":
            stdscr.addstr(8,2,"Please fill in Credit fields!")
            stdscr.refresh()
            credict.edit()
         while credict.gather().strip() != "":
            try:
               c = int(credict.gather().strip())
               cou = cc.Course(id.gather(),name.gather(),c)
               t =False
               break
            except ValueError:
               stdscr.addstr(8,2,"Wrong type of input in credict, please try again.")
               stdscr.refresh()
               credict.edit()
      return cou 
# input mark in each course
def input_mark(stud, Cour,stdscr):
    stdscr.clear()
    stdscr.addstr(0,2,"Course you want to add mark")
    k =Box.makebox(stdscr,"ID",1,20,2,2)
    stdscr.refresh()
    k.edit()
    count = 0
    for i in range(len(Cour)):
        if (k.gather() == Cour[i].id):
          Cour[i].mark(stud,stdscr)
        else:
            count +=1
    if (count == len(Cour)):
        print("Id of course not found.")
    stdscr.refresh()
    stdscr.addstr(15,0,"Press any key to continue ...")
    stdscr.getch()
def load_student(id,name,dob):
    stu = sc.Student(id,name,dob)
    return stu
def load_course(id, name, credict):
    cou = cc.Course(id,name,credict)
    return cou
def load_mark(Cour, stud, mark):
    a = mark
    b = stud.id
    c = stud.name
    d = stud.Dob
    point = sc.mark_in_course(b,c,d,a)
    Cour.markcour = np.append(Cour.markcour,point)
    stud.point(Cour.id,Cour.name,a, Cour.credict)
    
    