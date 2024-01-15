# Add number of Student

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
def crearte_marktable(number):
     idstudent = input("ID: ")
     namestudent = input("Name: ")
     resultstudent = input("Mark: ")
     markstudent ={
          "ID ": idstudent,
          "Name ": namestudent,
          "Mark": resultstudent
     }
     return markstudent



def main():
    n = input_numberStudent()
    Students =[]
    Coures = []
    Table_mark_coures = []
    for i in range(n):
          person= input_infro(i)
          Students.append(person)
    for i in range(n):
         print(Students[i].get("ID"))
    m = input_numberofcoures()
    for i in range(m):
         listcourse = input_course(i)
         Coures.append(listcourse)
    for i in range(m):
         print(Coures[i])
    l = input("ID of course you want to add mark: ")
    count =0
    for i in range(m):
         if (Coures[i].get('ID')==l):
              Table_mark_coures.append(Coures[i])
              k= int(input("The number in this class you want to add: "))
              for j in range(1,k+1):
                   personmark = crearte_marktable(j)
                   Table_mark_coures.append(personmark)
         else: 
              count = count+1     
                   
    if (count == m):
         print("This class not found.")     
    print(Table_mark_coures)
                   
    


          

main()




