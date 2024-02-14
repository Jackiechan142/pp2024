# print information of all Student
def print_student_infor(stud):
   for i in range(len(stud)):
         print(stud[i])

# print information of all Course
def print_course_infor(Cour):
     for i in range(len(Cour)):
          print(Cour[i])

# print mark of Course want to see
def print_mark_of_course(Cour):
     n = input("ID of course you want to see mark: ")
     cont = 0
     for i in range(len(Cour)):
            if (n == Cour[i].id):
                Cour[i].print()
            else:
                cont = cont+1
     if (cont == len(Cour)):
        print("Id of course not found.")

# print mark of student
def print_mark_of_student(stud):
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

# print Rank of GPA
def print_GPA(stud):
    if len(stud) == 0 :
        print("There no data of Student.")
    else:
       new_list = sorted(stud, key=lambda x: x.GPA(), reverse=True)
       for i in range(len(new_list)):
            new_list[i].rank()
         