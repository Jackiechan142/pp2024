
import input as ip
import output as op
import function as fc
import numpy as np
import zipfile
import os
import Box
from curses import wrapper
def main(stdscr):
    student = np.array([])
    course = np.array([])
    zf = "Students.dat"
    f1 = 'students.txt'
    f2 = 'courses.txt'
    f3 = 'marks.txt'
    if os.path.isfile(zf):
           with zipfile.ZipFile(zf) as zipf:
               zipf.extractall()
               list_zip = zipf.namelist()
               for file_name in list_zip:
                   if file_name == f1:
                      with open(f1,'r') as file:
                        lines = file.readlines()
                        for line in lines:
                            arr = line.split("||")
                            if (len(arr) == 3):
                                student = np.append(student, ip.load_student(arr[0],arr[1],arr[2]))
                            else: 
                                continue
                   elif file_name == f2:
                        with open(f2,'r') as file1:
                          lines1= file1.readlines()
                          for line1 in lines1:
                             arr1= line1.split("||")
                             course = np.append(course, ip.load_course(arr1[0],arr1[1],int(arr1[2])))
                   elif file_name == f3:
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
        stdscr.clear()
        stdscr.addstr("1. Add information of Student.\n")
        stdscr.addstr("2. Add information of Course.\n")
        stdscr.addstr("3. Show the information of all the Student.\n")
        stdscr.addstr("4. Show the information of all Course.\n")
        stdscr.addstr("5. Add the mark in Course.\n")
        stdscr.addstr("6. Show mark of student in each Course.\n")
        stdscr.addstr("7. Delete data.\n")
        stdscr.addstr("8. Show mark of each Student.\n")
        stdscr.addstr("9. Rank of GPA.\n")
        stdscr.addstr("10. clear all data.\n")
        stdscr.addstr("0. Exit\n")
        stdscr.addstr("Please choice: ")
        stdscr.refresh()
        choose = stdscr.getch()
       
        if (choose == ord('1')):
                    student = np.append(student,ip.input_student(stdscr))
                    stdscr.addstr(10,25,"Student added done.")
                    try:
                      fc.write_file(student)
                    except IOError:
                        print("Error in write to file.")
                    stdscr.refresh()
                    stdscr.getch()
        elif choose == ord('2'):
                    course = np.append(course,ip.input_Course(stdscr))
                    stdscr.addstr(10,25,"Course added done.")
                    try:
                      fc.print_file(course)
                    except IOError:
                        print("Error in write to file.")
                    stdscr.refresh()
                    stdscr.getch()
        elif choose == ord('3'):
                    op.print_student_infor(student,stdscr)
        elif choose == ord('4'):       
                    op.print_course_infor(course,stdscr)     
        elif choose == ord('5'):
                    while(len(course) == 0):
                         stdscr.addstr("There no course, please input data of course.")
                         student = np.append(student,ip.input_student(stdscr))
                         stdscr.addstr(10,25,"Student added done.")
                         try:
                            fc.write_file(student)
                         except IOError:
                           print("Error in write to file.")
                         stdscr.refresh()
                         stdscr.getch()
                    while (len(student)==0):
                        course = np.append(course,ip.input_Course(stdscr))
                        stdscr.addstr(10,25,"Course added done.")
                        try:
                           fc.print_file(course)
                        except IOError:
                            print("Error in write to file.")
                            stdscr.refresh()
                            stdscr.getch()
                    ip.input_mark(student,course,stdscr)
                    try:
                            fc.write_mark(course)
                    except IOError:
                        print("Error in write to file.")
        elif choose == ord('6'):   
                    op.print_mark_of_course(course,stdscr)
        elif choose == ord('7'):
                    stdscr.clear()
                    stdscr.addstr(1,2,"1. Remove student.")
                    stdscr.addstr(2,2,"2. Remove course.")
                    stdscr.addstr(3,2,"Your choose: ")
                    stdscr.refresh()
                    chos = stdscr.getch()
                    if chos == ord("1"):
                            stdscr.clear()
                            stdscr.addstr(1,2,"Student you want to remove")
                            q = Box.makebox(stdscr,"ID",1,20,2,2)
                            out = 0
                            for i in range(len(student)):
                                if (q.gather() == student[i].id):
                                      fc.remove_student(student[i],course)
                                      fc.write_mark(course)
                                      student = np.delete(student,i)
                                      fc.write_file(student)
                                      break
                                else:
                                  out = out +1
                            if (out > len(student)):
                                stdscr.addstr(4,2,"This ID is not found.")
                    elif chos == ord("2"):
                            stdscr.clear()
                            stdscr.addstr(1,2,"Course you want to remove")
                            w = Box.makebox(stdscr,"ID",1,20,2,2)
                            ou = 0
                            for i in range(len(course)):
                                if (w.gather() == course[i].id):
                                  fc.remove_course(course[i],student)
                                  course = np.delete(course,i)
                                  fc.print_file(course)
                                  break
                                else:
                                    ou = ou +1
                            if ou > len(course):
                                   stdscr.addstr(4,2,"This ID is not found.")
                    else:
                         stdscr.clear()
                         stdscr.addstr(1,25,"Wrong type of input.")
                         stdscr.refresh()
                         stdscr.addstr(18,25,"Press any key to continue ...")
                         stdscr.getch()
        elif choose == ord('8'):
                    op.print_mark_of_student(student,stdscr)
        elif choose == ord('9'):
                    op.print_GPA(student,stdscr)
        elif choose == ord('*'):
                    stdscr.clear()
                    stdscr.addstr(1,2,"Are you sure? Y?N")
                    stdscr.refresh()
                    sure = stdscr.getch()
                    if sure == ord("Y") or sure == ord("y"):
                            student = np.delete(student,np.s_[:])
                            course = np.delete(course,np.s_[:])
                            fc.write_file(student)
                            fc.print_file(course)
                            with open(f3,'w') as file:
                                pass
                    elif sure == ord("N") or sure == ord("n"):  
                            print("OK, fine!")
                    else:
                          break
                    stdscr.refresh()
                    stdscr.addstr(18,25,"Press any key to continue ...")
                    stdscr.getch()
        elif choose == ord('0'):
                    fc.zip_file()
                    break
       
if __name__=="__main__":
   wrapper(main)