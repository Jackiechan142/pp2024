import function as fc
import numpy as np
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
                        a = fc.round_down(e)
                        b = student[j].id
                        c = student[j].name
                        d = student[j].Dob
                        point = fc.mark_in_course(b,c,d,a)
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
