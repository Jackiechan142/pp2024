
import input as ip
import output as op
import function as fc
import numpy as np
import zipfile
def main():
    zf = "Students.dat"
    if bool(fc.check_zip(zf)):
        print("File have data before.")
    else:
        print("No data before.")
    student = np.array([])
    course = np.array([])
    f1 = "students.txt"
    f2 = 'courses.txt'
    f3 = 'marks.txt'
    with open(f1,'r') as file:
        lines = file.readlines()
        for line in lines:
            arr = line.split("||")
            if (len(arr) == 3):
                student = np.append(student, ip.load_student(arr[0],arr[1],arr[2]))
            else: 
                continue
    with open(f2,'r') as file1:
        lines1= file1.readlines()
        for line1 in lines1:
            arr1= line1.split("||")
            course = np.append(course, ip.load_course(arr1[0],arr1[1],int(arr1[2])))
    with open(f3, 'r') as file2:
        lines2 = file2.readlines()
        for line2 in lines2:
            arr2 = line2.split("----------")
            arr3 = line2.split("\t||\t")
            if (len(arr2)==1):
                for j in range(len(student)):
                    if (arr3[0] == student[j].id):
                        ip.load_mark(course[number],student[j],float(arr3[2]))
                continue
            else:
                for i in range(len(course)):
                    if (arr2[0]==course[i].id):
                        number = i
    while(True):
        print("1. Add information of Student.")
        print("2. Add information of Course. ")
        print("3. Show the information of all the Student.")
        print("4. Show the information of all Course.")
        print("5. Add the mark in Course.")
        print("6. Show mark of student in each Course.")
        print("7. Delete data.")
        print("8. Show mark of each Student.")
        print("9. Rank of GPA.")
        print("10. clear all data.")
        print("0. Exit")
        choose = input("Please choose: ")
        match choose:
                case '1':
                    fc.clear()
                    i =0
                    try:
                      n = int(input("Number of Student you want to add: "))
                      while(i< n ):
                        student = np.append(student,ip.input_student())
                        i = i + 1
                      fc.write_file(student)
                    except ValueError:
                        print("Wrong type of input, please try again.")
                    except IOError:
                        print("Error in write to file.")
                case '2':
                    fc.clear()
                    c = 0
                    try:
                      h = int(input("Number of Course you want to add: "))
                      while(c< h ):
                        course = np.append(course,ip.input_Course())
                        c = c + 1
                      fc.print_file(course)
                    except ValueError:
                        print("Wrong type of input, please try again.")
                    except IOError:
                        print("Error in write to file.")
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
                             fc.print_file(course)
                         except ValueError:
                             print("Wrong type of input, please try again.")
                         except IOError:
                             print("Error in write to file")
                    while (len(student)==0):
                        print("There no data of student, please input data of student.")
                        e= 0
                        try:
                            f = int(input("Number of Student you want to add: "))
                            while(e< f ):
                               student = np.append(student,ip.input_student())
                               e = e + 1
                            fc.write_file(student)
                        except ValueError:
                            print("Wrong type of input, please try again.")
                        except IOError:
                            print("Error in write to file.")
                    ip.input_mark(student,course)
                    try:
                            fc.write_mark(course)
                    except IOError:
                        print("Error in write to file.")
                    fc.exit()
                case '6':
                    fc.clear()
                    op.print_mark_of_course(course)
                    fc.exit()
                case '7':
                    fc.clear()
                    print("1. Remove student.")
                    print("2. Remove course.")
                    chos = input("Your choose: ")
                    match chos:
                        case '1':
                            q = input("ID of student you want to remove: ")
                            out = 0
                            for i in range(len(student)):
                                if (q == student[i].id):
                                      fc.remove_student(student[i],course)
                                      fc.write_mark(course)
                                      student = np.delete(student,i)
                                      fc.write_file(student)
                                      break
                                else:
                                  out = out +1
                            if (out > len(student)):
                                print("This ID is not found.")
                        case '2':
                            w = input("ID of course you want to remove: ")
                            ou = 0
                            for i in range(len(course)):
                                if (w == course[i].id):
                                  fc.remove_course(course[i],student)
                                  course = np.delete(course,i)
                                  fc.print_file(course)
                                  break
                                else:
                                    ou = ou +1
                            if ou > len(course):
                                   print("This ID is not found.")
                    fc.exit()
                case '8':
                    fc.clear()
                    op.print_mark_of_student(student)
                    fc.exit()
                case '9':
                    fc.clear()
                    op.print_GPA(student)
                    fc.exit()
                case '10':
                    fc.clear()
                    sure=input("Are you sure? Y?N")
                    match sure:
                        case 'Y':
                            student = np.delete(student,np.s_[:])
                            course = np.delete(course,np.s_[:])
                            fc.write_file(student)
                            fc.print_file(course)
                            with open(f3,'w') as file:
                                pass
                        case 'y':
                            student = np.delete(student,np.s_[:])
                            course = np.delete(course,np.s_[:])
                            fc.write_file(student)
                            fc.print_file(course)
                            with open(f3,'w') as file:
                                pass
                        case 'N':
                            print("OK, fine!")
                            fc.exit()
                        case 'n':
                            print("OK, fine!")
                            fc.exit()
            
                case '0':
                    fc.zip_file()
                    break
       

main()