
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
    try: 
       n = int(input("The number of courses you want to add: "))
    except ValueError:
          print("Wrong type of input, please try again.")
          input_numberofcoures()
    return n

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

# input mark for each student in each course.
def  input_mark_each_course(student,mark,number,studentmark):
    try:
      table = []
      k = int(input("The number of student you want to add in this class: "))
      print(student)
      for i in range(0,k):
        t = True  
        while (t):
           q = input("ID of student you want to add: ")
           count= 0
           for j in range(len(student)):
               if (q == student[j].get("ID")):
                    a = student[j].get("ID")
                    b = student[j].get("Name")
                    c = float(input("Mark of this Student: "))
                    d = mark[number].get("ID")
                    e = mark[number].get("Name")
                    f= c
                    per = crearte_marktable(i,a,b,c)
                    table.append(per)
                    tab= copy_mark(j,d,e,f)
                    marktable =[]
                    marktable.append(tab)
                    studentmark[j]["markTable"] = marktable
                    t =False
                    break
               else:
                    count= count+1
               if (count == len(student)):
                    print("This ID is not found, please try again.")
      mark[number][len(mark[number])] = table
    except ValueError:
        print("Wrong type of input, please try again.")
        input_mark_each_course()
     
     
# Copy mark in each course to return each student learned.
def copy_mark(number,id,name,mark):
    table ={
        "ID of cousre": id,
        "Name od cousre":name,
        "Mark": mark
    }
    return table


           




def clear():
    print("\033c")

def exit():
    input("\nPress Enter to exit ...")
    clear()


def main():
    Students =[]
    Coures = []
    mark =[]
    studentmark = []
    while (True): 
       print("1. Add information of Student.")
       print("2. Add information of Course. ")
       print("3. Show the information of all the Student.")
       print("4. Show the information of all Course.")
       print("5. Add the mark in Course.")
       print("6. Show mark of student in all Course.")
       print("7. Remove sutdent.")
       print("8. Show mark of each Student.")
       print("0. Exit")
       choose = input("Please choose: ")
       try:
         val = int(choose)
         match choose:
          case '1':
              clear()
              try:
                n = int(input("Give me number of Student you want to add: "))
                for i in range(n):
                  person= input_infro(i)
                  Students.append(person)
                  studentmark.append(person)
             
              except ValueError:
                print("Wrong type of input, plese try again.")     
          case '2':
               clear()
               m = input_numberofcoures()
               for i in range(m):
                   listcourse = input_course(i)
                   Coures.append(listcourse)
                   mark.append(listcourse)
          case '3':
              clear()
              while (len(Students) == 0):
                  print("You haven't entered The Student, please add the Student.")
                  n = input_numberStudent()
                  for i in range(n):
                    person= input_infro(i)
                    Students.append(person)
                    studentmark.append(person)
              for i in range(len(Students)):
                   print(Students[i])
              exit()
          case '4':
              clear()
              while (len(Coures) == 0):
                print("You haven't enterd the Course, please add the Course.")
                m = input_numberofcoures()
                for i in range(m):
                    listcourse = input_course(i)
                    Coures.append(listcourse)
                    mark.append(listcourse)
              for i in range(len(Coures)):
                   print(Coures[i])
              exit()
          case '5':
               clear()
               while (len(Coures) == 0):
                    print("You haven't enterd the Course, please add the Course.")
                    m = input_numberofcoures()
                    for i in range(m):
                        listcourse = input_course(i)
                        Coures.append(listcourse)
                        mark.append(listcourse)
               for i in range(len(Coures)):
                   print(Coures[i])
               t= True
               while (t):
                   l = input("ID of course you want to add mark: ")
                   count =0
                   for i in range(len(Coures)):
                     if (Coures[i].get('ID')== l):
                        while (len(Students) == 0):
                            print("You haven't add stduent, please add student.")
                            n = input_numberStudent()
                            for k in range(n):
                                  person= input_infro(k)
                                  Students.append(person)
                                  studentmark.append(person)
                        input_mark_each_course(Students,mark,i,studentmark)
                        t = False
                        break
                     else: 
                        count = count+1      
                   if (count == len(Coures)):
                    print("This class not found, please try again.")   
               exit()
          case '6':
              clear()
              if (len(Coures) != 0):
               for i in range(len(Coures)):
                   print(Coures[i])
               g = input("ID of Course you want to see mark: ")
               for i in range(len(mark)):
                   if (mark[i].get("ID") == g):
                      if (len(mark[i]) != 1):                     
                          print(mark[i])   
                      else:
                        print("This Course haven't student.")
              exit() 
          case '7': 
             clear()
             if (len(Students) != 0):  
               f = input("ID of student you want to remove: ")
               Count = 0
               for i in range(len(Students)):
                   if (Students[i].get("ID" == f)):
                       Students.remove(Students[i])
                   else:
                       Count +=1
               if (Count == len(Students)):
                   print(" There have not Student who you want to remove.")    
             else: 
                 print("You haven't add the Student yet.")    
             exit()  
          case  '8':
               clear()
               if (len(Coures) != 0):
                   for i in  range(len(Students)):
                       print(Students[i])
                   h = input("ID of Student you want to see mark: ")
                   for i in range(len(studentmark)):
                      if (studentmark[i].get("ID") == h):
                        if (len(studentmark[i]) != 1):                     
                          print(studentmark[i])   
               exit() 

          case '0':
                 break
       except ValueError:
           print("Wrong type of value, please try again.")
           main()


main()
