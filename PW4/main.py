import input as ip
import output as op
import function as fc
import numpy as np
def main():
    student = np.array([])
    course = np.array([])
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
                    fc.clear()
                    i =0
                    try:
                      n = int(input("Number of Student you want to add: "))
                      while(i< n ):
                        student = np.append(student,ip.input_student())
                        i = i + 1
                    except ValueError:
                        print("Wrong type of input, please try again.")
                case '2':
                    fc.clear()
                    c = 0
                    try:
                      h = int(input("Number of Course you want to add: "))
                      while(c< h ):
                        course = np.append(course,ip.input_Course())
                        c = c + 1
                    except ValueError:
                        print("Wrong type of input, please try again.")
                case '3':
                    fc.clear()
                    op.print_student_infor(student)
                    fc.exit()
                case '4':
                    fc.clear()
                    op.print_course_infor(course)
                    fc.exit()
                case '5':
                    fc.clear()
                    while(len(course) == 0):
                         print("There no course, please input data of course.")
                         a = 0
                         try:
                             b = int(input("Number of Course you want to add: "))
                             while(a< b ):
                                 course = np.append(course,ip.input_Course())
                                 a = a + 1
                         except ValueError:
                             print("Wrong type of input, please try again.")
                    while (len(student)==0):
                        print("There no data of student, please input data of student.")
                        e= 0
                        try:
                            f = int(input("Number of Student you want to add: "))
                            while(e< f ):
                               student = np.append(student,ip.input_student())
                               e = e + 1
                        except ValueError:
                            print("Wrong type of input, please try again.")
                    ip.input_mark(student,course)
                    fc.exit()
                case '6':
                    fc.clear()
                    op.print_mark_of_course(course)
                    fc.exit()
                case '7':
                    fc.clear()
                    fc.remove_student(student)
                    fc.exit()
                case '8':
                    fc.clear()
                    op.print_mark_of_student(student)
                    fc.exit()
                case '9':
                    fc.clear()
                    op.print_GPA(student)
                    fc.exit()
                case '0':
                    break
        except ValueError:
             print("Wrong type of inpur, please try agian.")
             main()

main()