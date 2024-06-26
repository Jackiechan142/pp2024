import math
import os
import zipfile
import numpy as np
import pickle
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
    

# write to file student.txt
def write_file(student):
    with open("students.txt","wb") as file:
        for i in range(len(student)): 
             pickle.dump(student[i],file)
#    f = open("students.txt","w")
#    for i in range(len(student)):
#        f.writelines(student[i].id+"||"+student[i].name+"||"+student[i].Dob)
#        f.write("\n")
#    f.close()
# write to file courses.txt
def print_file(course):
    with open('courses.txt','wb') as file:
        for i in range(len(course)):
            pickle.dump(course[i],file)
    # f= open("courses.txt","w")
    # for i in range(len(course)):
    #     f.write(course[i].id+"||"+course[i].name+"||"+str(course[i].credict))
    #     f.write("\n")
    # f.close()
# write to file marks.txt
def write_mark(courese):
    with open('marks.txt','wb') as file:
        for i in range(len(courese)):
            pickle.dump(courese[i],file)
            for j in range(len(courese[i].markcour)):
                pickle.dump(courese[i].markcour[j],file)
    # f= open("marks.txt","w") 
    # for i in range(len(courese)):
    #     f.write(courese[i].id +"----------"+courese[i].name+"----------"+str(courese[i].credict))
    #     f.write("\n")
    #     for j in range(len(courese[i].markcour)):
    #        f.write(courese[i].markcour[j].id+"\t||\t"+courese[i].markcour[j].name+"\t||\t"+str(courese[i].markcour[j].mark))
    #        f.write("\n")
    # f.close()
# create a Zipfile Object:
def zip_file():
   zp = "Students.dat"
   fz = ["students.txt","courses.txt","marks.txt"]
   with zipfile.ZipFile(zp,'w') as zip_ref:
       for f in fz:
           zip_ref.write(f)
           os.remove(f)
   print("Zip file created succesfully.")
