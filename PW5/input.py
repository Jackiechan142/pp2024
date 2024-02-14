from domain import Student_class as sc
from domain import Crouse_class as cc
import numpy as np
# input data of student
def input_student(): 
       id = input("Id of student: ")
       name = input("Name of Student: ")
       dob = input("Dob of Student: ")
       print("==================")
       stu = sc.Student(id,name,dob)  
       return stu
   
# input data of cousre
def input_Course():
      id = input("Id of course: ")
      name = input("Name of cousre: ")
      credict = int(input("Credict od this course: "))
      print("===================")
      cou = cc.Course(id,name,credict)
      return cou 
# input mark in each course
def input_mark(stud, Cour):
    k = input("ID of course you want to add mark: ")
    count = 0
    for i in range(len(Cour)):
        if (k == Cour[i].id):
          Cour[i].mark(stud)
        else:
            count = count+1
    if (count == len(Cour)):
        print("Id of course not found.")
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
    
    