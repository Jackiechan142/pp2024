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
          "ID: ": input("ID: "),
          "Name": input("Name: ")
     }
     return course



def main():
    n = input_numberStudent()
    Students =[]
    for i in range(n):
          person= input_infro(i)
          Students.append(person)
    for i in range(n):
         print(Students[i])

main()




