import math
import numpy as np
# make class Student
class Student:
    def __init__(self,id, name, Dob,):
         self.id = id
         self.name = name
         self.Dob= Dob
         self.mark = np.array([])
    def __str__(self):
        return f" ID: {self.id} \n Name: {self.name} \n Dob: {self.Dob} \n ================= \n "
    # input mark of each course to Student, form list.
    def point(self, id,name, mark, credict):
        a = id
        b= name
        c= mark
        d =credict
        point = mark_of_student(a,b,d,c)
        self.mark= np.append(self.mark,point)
    # print list of mark in each course of this student
    def print(self):
        print("ID: ", self.id,"\nName: ",self.name,"\n===========================\n")
        for i in range(len(self.mark)):
            print(self.mark[i])
    # caculate GPA 
    def GPA(self):
        result = 0
        cre = 0
        for i in range(len(self.mark)):
             result = float(result+ cla_GPA(self.mark[i].point,self.mark[i].credict))
             cre = int(cre + self.mark[i].credict)
        firesult = float(result /cre)
        return round_down(firesult)
# make child class of class Student
class mark_in_course(Student):
    def __init__(self, id, name, Dob, mark):
        super().__init__(id, name, Dob)
        self.mark = mark
    def __str__(self):
        return f"ID: {self.id} \t Name: {self.name} \t Mark: {self.mark}"
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
    def mark(self, student):
        try:
            i= True
            while (i):
                id = input("ID of student you want to add: ")
                count = 0
                for j in range(len(student)):
                    if(id == student[j].id):
                        e = float(input("Mark of this student: "))
                        a = round_down(e)
                        b = student[j].id
                        c = student[j].name
                        d = student[j].Dob
                        point = mark_in_course(b,c,d,a)
                        self.markcour = np.append(self.markcour,point)
                        student[j].point(self.id, self.name,a,self.credict)
                    else:
                        count = count +1
                if (count == len(student)):
                    print("This ID not found.")
                
                while(True):
                 try:
                   chose = input("Do you want to continue? Y/N: ")
                   if (chose =='N' or chose == 'n'):
                     i=False
                     break
                   elif(chose != 'Y' or chose !='y'):
                    break
                 except ValueError:
                    print("Wrong type of input, please try again.")
        except ValueError:
            print("Wrong type of input, please try again.")
            Course.mark(student)
    # print mark of all student in this cousre
    def print(self):
        print(" Id:",self.id," \n Name: ", self.name, "Credict: ", self.credict, "\n ================================================= \n")
        for i in range(len(self.markcour)):
            print(self.markcour[i])
# create a child class of class Course
class mark_of_student(Course):
    def __init__(self, id, name,credict,point):
        super().__init__(id, name, credict)
        self.point = point
    def __str__(self):
        return f" ID of course: {self.id} \t Name of course: {self.name} \t Credict: {self.credict} \t Mark: {self.point}"

# # input data of student
# def input_student(stud):
#     try: 
#          n = int(input("Number of Student you want to add: "))
#          for i in range(n):
#             id = input("Id of student: ")
#             name = input("Name of Student: ")
#             dob = input("Dob of Student: ")
#             print("==================")
#             stu = Student(id,name,dob)  
#             stud = np.append(stud,stu)
#     except ValueError:
#         print("Wrong type of input, please try again.")
#         input_student(stud)

# # input data of cousre
# def input_Course(Cour):
#     try:
#         n = int(input("Number of Course you want to add: "))
#         for i in range(n):
#             id = input("Id of course: ")
#             name = input("Name of cousre: ")
#             credict = int(input("Credict od this course: "))
#             print("===================")
#             cou = Course(id,name,credict)
#             Cour = np.append(Cour,cou)
#     except ValueError:
#         print("Wrong type of input, please try again.")
#         input_Course(Cour)

# round down mark to 1 digit.
def round_down(number):
    a = number*10
    newnumber= float(math.floor(a)/10)
    return newnumber
# calculate the GPA 
def cla_GPA(mark, credict):
    result = float(mark * credict)
    return result

def clear():
    print("\033c")

def exit():
    input("\nPress Enter to exit ...")
    clear()

def main():
    stud = np.array([]) 
    Cour = np.array([])
    while(True):
        print("1. Add information of Student.")
        print("2. Add information of Course. ")
        print("3. Show the information of all the Student.")
        print("4. Show the information of all Course.")
        print("5. Add the mark in Course.")
        print("6. Show mark of student in each Course.")
        print("7. Remove sutdent.")
        print("8. Show mark of each Student.")
        print("9. Rank of GPA.")
        print("0. Exit")
        choose = input("Please choose: ")
        try: 
            val = int(choose)
            match choose:
                case '1':
                    clear()
                    try: 
                        n = int(input("Number of Student you want to add: "))
                        for i in range(n):
                           id = input("Id of student: ")
                           name = input("Name of Student: ")
                           dob = input("Dob of Student: ")
                           print("==================")
                           stu = Student(id,name,dob)  
                           stud = np.append(stud,stu)
                    except ValueError:
                       print("Wrong type of input, please try again.")
                case '2':
                    clear()
                    try:
                       n = int(input("Number of Course you want to add: "))
                       for i in range(n):
                            id = input("Id of course: ")
                            name = input("Name of cousre: ")
                            credict = int(input("Credict of this course: "))
                            print("===================")
                            cou = Course(id,name,credict)
                            Cour = np.append(Cour,cou)
                    except ValueError:
                             print("Wrong type of input, please try again.")
                case '3':
                    clear()
                    for i in range(len(stud)):
                        print(stud[i])
                    exit()
                case '4':
                    clear()
                    for i in range(len(Cour)):
                        print(Cour[i])
                    exit()
                case '5':
                    clear()
                    while(len(stud) == 0):
                        print("There no course, please input data of course.")
                    try: 
                        n = int(input("Number of Student you want to add: "))
                        for i in range(n):
                           id = input("Id of student: ")
                           name = input("Name of Student: ")
                           dob = input("Dob of Student: ")
                           print("==================")
                           stu = Student(id,name,dob)  
                           stud = np.append(stud,stu)
                    except ValueError:
                       print("Wrong type of input, please try again.")
                    while(len(Cour) == 0):
                        print("There no data of Student, please input information of student.")
                    try:
                       n = int(input("Number of Course you want to add: "))
                       for i in range(n):
                            id = input("Id of course: ")
                            name = input("Name of cousre: ")
                            credict = int(input("Credict of this course: "))
                            print("===================")
                            cou = Course(id,name,credict)
                            Cour = np.append(Cour,cou)
                    except ValueError:
                             print("Wrong type of input, please try again.")
                    k = input("ID of course you want to add mark: ")
                    count = 0
                    for i in range(len(Cour)):
                        if (k == Cour[i].id):
                            Cour[i].mark(stud)
                        else:
                            count = count+1
                    if (count == len(Cour)):
                        print("Id of course not found.")
                    exit()
                case '6':
                     clear()
                     n = input("ID of course you want to see mark: ")
                     cont = 0
                     for i in range(len(Cour)):
                        if (n == Cour[i].id):
                            Cour[i].print()
                        else:
                            cont = cont+1
                     if (cont == len(Cour)):
                        print("Id of course not found.")
                     exit()
                case '7':
                    clear()
                    a = input("ID of student you want to remove: ")
                    cout = 0
                    for i in range(len(stud)):
                        if (a == stud[i].id):
                            stud.remove(stud[i])
                        else:
                            cout = cout +1
                    if (cout == len(stud)):
                        print("This ID is not found.")
                    exit()
                case '8':
                    clear()
                    b = input("ID of student you want to see mark: ")
                    cot = 0
                    for i in range(len(stud)):
                        if (b == stud[i].id):
                            stud[i].print()
                            print("GPA : ",stud[i].GPA())
                        else:
                            cot = cot +1
                    if (cot == len(stud)):
                        print("This ID is not found.")
                    exit()
                case '9':
                    clear()
                    new_list = sorted(stud, key=lambda x: x.GPA(), reverse=True)
                    for i in range(len(new_list)):
                        print(new_list[i])
                        print(new_list[i].GPA())
                case '0':
                    break
        except ValueError: 
            print("Wrong type of inpur, please try agian.")
            main()
        
main()
