# Add number of Student
from operator import truediv
from re import T


def input_numberStudent():
    n = int(input("Give me number of Student you want to add: "))
    return n


# add information to each Student
def input_infro(number):
    ID = input("Id: ")
    Name = input("Name: ")
    Dob = input("Dob: ")
    student = {
        'ID'  : ID,
        'Name' : Name ,
        'Dob' : Dob
    }
    return student

# add number of courses
def input_numberofcoures():
     return int(input("The number of courses you want to add: "))

# add infromation to each course
def input_course(number):
     course = {
          "ID": input("ID: "),
          "Name": input("Name: ")
     }
     return course

# create mark table for each coure
def crearte_marktable(number,id, name, mark):
     markstudent ={
          "ID ": id,
          "Name ": name,
          "Mark": mark
     }
     return markstudent

# input mark for each student in each coures
def input_mark_each_course(number,student,course):
     table = []
     table.append(course[number])
     k = int(input("The number of student you want to add in this class: "))
     print(student)
     for i in range(1,k+1):
          q = input("ID of student you want to add: ")
          count= 0
          for j in range(len(student)):
               if (q== student[j].get("ID")):
                    a = student[j].get("ID")
                    b = student[j].get("Name")
                    c = float(input("Mark of this Student: "))
                    per = crearte_marktable(i,a,b,c)
                    table.append(per)
                    break
               else:
                    count= count+1
               if (count == len(student)):
                    print("This ID is not found.")
                    break
          
     return table
     


def main():
    Students =[]
    Coures = []
    Cou =[]
    while (True):
       print("1. Add information of Student.")
       print("2. Add information of Course. ")
       print("3. Show the information of all the Student.")
       print("4. Show the information of all Course.")
       print("5. Add the mark in Course.")
       print("6. Show mark of student in all Course.")
       print("0. Exit")
       choose = input("Please choose: ")
       match choose:
         case '1':
              n = input_numberStudent()
              for i in range(n):
                person= input_infro(i)
                Students.append(person)
         case '2':
               m = input_numberofcoures()
               for i in range(m):
                   listcourse = input_course(i)
                   Coures.append(listcourse)
         case '3':
              for i in range(len(Students)):
                   print(Students[i])
         case '4':
              for i in range(len(Coures)):
                   print(Coures[i])
         case '5':
               l = input("ID of course you want to add mark: ")
               count =0
               for i in range(m):
                    if (Coures[i].get('ID')==l):
                        makrcour = input_mark_each_course(i,Students,Coures)
                        Cou.append(makrcour)
                    else: 
                        count = count+1      
               if (count == m):
                    print("This class not found.")     
         case '6':
              for i in range(len(Cou)):
                   print(Cou[i])    
         case '0':
                 break




          

main()




