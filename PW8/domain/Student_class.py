import function as fc
from domain import Crouse_class as cc
import numpy as np
class Student:
    def __init__(self,id, name, Dob,):
         self.id = id
         self.name = name
         self.Dob= Dob
         self.mark = np.array([])
    def __str__(self):
        return f" ID: {self.id} \n Name: {self.name} \n Dob: {self.Dob} \n ====================== \n "
    # input mark of each course to Student, form list.
    def point(self, id,name, mark, credict):
        a = id
        b= name
        c= mark
        d =credict
        point = cc.mark_of_student(a,b,d,c)
        self.mark= np.append(self.mark,point)
    # print list of mark in each course of this student
    def print(self,stdscr):
        stdscr.clear()
        stdscr.addstr(0,2,f"ID: {self.id} \t Name: {self.name} \t Dob: {self.Dob}")
        stdscr.addstr(2,2,f"{'Id of course':<15}{'Name of course':<30}{'Mark':<5}")
        row =4
        for i in range(len(self.mark)):
            stdscr.addstr(row,2,f"{self.mark[i].id:<15}{self.mark[i].name:<30}{self.mark[i].point}")
            row +=2
    # caculate GPA 
    def GPA(self):
        result = 0
        cre = 0
        for i in range(len(self.mark)):
             result = float(result+ fc.cla_GPA(self.mark[i].point,self.mark[i].credict))
             cre = int(cre + self.mark[i].credict)
        firesult = float(result /cre)
        return fc.round_down(firesult)
    def rank(self,stdscr,row):
        stdscr.addstr(row,2,f"ID: {self.id:<15}Name: {self.name:<30}GPA: {self.GPA()}")
# make child class of class Student
class mark_in_course(Student):
    def __init__(self, id, name, Dob, mark):
        super().__init__(id, name, Dob)
        self.mark = mark
    def __str__(self):
        return f"ID: {self.id} \t Name: {self.name} \t Mark: {self.mark}"
    