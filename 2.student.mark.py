class Student:
    def __init__(self,id, name, Dob,):
         self.id = id
         self.name = name
         self.Dob= Dob
         self.mark = []
    def __str__(self):
        return f" ID: {self.id} \n Name: {self.name} \n Dob: {self.Dob} \n ================= \n "
    def point(self, id,name, mark):
        a = id
        b= name
        c= mark
        self.mark.append(input_markstudent(a,b,c))
    def print(self):
        print("ID: ", self.id,"\nName: ",self.name,"\n===========================\n")
        for i in range(len(self.mark)):
            print(self.mark[i])
class Course:
    def __init__(self, id, name,):
        self.id = id
        self.name = name 
        self.markcour = []
    def __str__(self):
        return f" Id: {self.id} \n Name: {self.name} \n ================================================= \n"
    def mark(self, student):
        try:
            i= True
            while (i):
                id = input("ID of student you want to add: ")
                count = 0
                for j in range(len(student)):
                    if(id == student[j].id):
                        a = int(input("Mark of this student: "))
                        b = student[j].id
                        c = student[j].name
                        self.markcour.append(input_markcourse(b,c,a))
                        student[j].point(self.id, self.name,a)
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
    def print(self):
        print(" Id:",self.id," \n Name: ", self.name,"\n ================================================= \n")
        for i in range(len(self.markcour)):
            print(self.markcour[i])
def input_student(stud):
    try: 
         n = int(input("Number of Student you want to add: "))
         for i in range(n):
            id = input("Id of student: ")
            name = input("Name of Student: ")
            dob = input("Dob of Student: ")
            print("==================")
            stu = Student(id,name,dob)  
            stud.append(stu)
    except ValueError:
        print("Wrong type of input, please try again.")
        input_student(stud)

def input_Course(Cour):
    try:
        n = int(input("Number of Course you want to add: "))
        for i in range(n):
            id = input("Id of course: ")
            name = input("Name of cousre: ")
            print("===================")
            cou = Course(id,name)
            Cour.append(cou)
    except ValueError:
        print("Wrong type of input, please try again.")
        input_Course(Cour)
def input_markcourse(id, name, mark):
    table= {
        'ID':id,
        'Name':name,
        'Mark':mark
    }
    return table
def input_markstudent(id,name,mark):
    table = {
        'ID of course':id,
        'Name of cousre':name,
        'Mark': mark
    }
    return table
def clear():
    print("\033c")

def exit():
    input("\nPress Enter to exit ...")
    clear()
def main():
    stud = []
    cour = []
    while(True):
        print("1. Add information of Student.")
        print("2. Add information of Course. ")
        print("3. Show the information of all the Student.")
        print("4. Show the information of all Course.")
        print("5. Add the mark in Course.")
        print("6. Show mark of student in each Course.")
        print("7. Remove sutdent.")
        print("8. Show mark of each Student.")
        print("0. Exit")
        choose = input("Please choose: ")
        try: 
            val = int(choose)
            match choose:
                case '1':
                    clear()
                    input_student(stud)
                    exit()
                case '2':
                    clear()
                    input_Course(cour)
                    exit()
                case '3':
                    clear()
                    for i in range(len(stud)):
                        print(stud[i])
                    exit()
                case '4':
                    clear()
                    for i in range(len(cour)):
                        print(cour[i])
                    exit()
                case '5':
                    clear()
                    while(len(cour) == 0):
                        print("There no course, please input data of course.")
                        input_Course(cour)
                    while(len(stud) == 0):
                        print("There no data of Student, please input information of student.")
                        input_student(stud)
                    k = input("ID of course you want to add mark: ")
                    count = 0
                    for i in range(len(cour)):
                        if (k == cour[i].id):
                            cour[i].mark(stud)
                        else:
                            count = count+1
                    if (count == len(cour)):
                        print("Id of course not found.")
                    exit()
                case '6':
                     clear()
                     n = input("ID of course you want to see mark: ")
                     cont = 0
                     for i in range(len(cour)):
                        if (n == cour[i].id):
                            cour[i].print()
                        else:
                            cont = cont+1
                     if (cont == len(cour)):
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
                        else:
                            cot = cot +1
                    if (cot == len(stud)):
                        print("This ID is not found.")
                        exit()
                case '0':
                    break
        except ValueError: 
            print("Wrong type of inpur, please try agian.")
            main()

main()