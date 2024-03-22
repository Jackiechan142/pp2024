
import input as ip
import output as op
import function as fc
import numpy as np
import zipfile
import os
import pickle
from curses import wrapper
import threading
import Box

student = np.array([])
course = np.array([])
zf = "Students.dat"

def read_data():
   global student
   global course
   if os.path.isfile(zf):   
      with zipfile.ZipFile(zf) as zipf:
         zipf.extractall()
         list_zip = zipf.namelist()
         for file_name in list_zip:
             if file_name == 'students.txt':
                with open('students.txt','rb') as file:
                    while True:
                       try:
                            data = pickle.load(file)
                            student = np.append(student,data)
                       except EOFError:
                           break
             elif file_name ==  'courses.txt':
                with open( 'courses.txt','rb') as file1:
                   while True:
                     try:   
                        data1 = pickle.load(file1)
                        course = np.append(course,data1)
                     except EOFError:
                        break
             elif file_name == 'marks.txt':
               with open('marks.txt', 'rb') as file2:
                  while True:
                      try:   
                         data2 = pickle.load(file2)
                         t= True
                         for i in range(len(course)):
                            if data2.id == course[i].id and data2.name == course[i].name:
                                numb = 0
                                while t:
                                  datamark = pickle.load(file2)
                                  for j in range(len(student)):
                                     if (datamark.id==student[j].id):
                                        if fc.check_mark(datamark.id,course[i].markcour) == True:
                                             t= False
                                             break
                                        ip.load_mark(course[i],student[j],float(datamark.mark))
                                     else:
                                       numb +=1
                                  if numb == len(student):
                                    t= False
                      except EOFError:
                        break
   return student,course


def main(stdscr): 
    global student
    global course
  
    t1= threading.Thread(target=read_data)
    t1.start()
    t1.join()

    try:
      fc.write_file(student)
      fc.print_file(course)
      fc.write_mark(course)
    except IOError:
       print("Error in write to file.")
   
    while(True):
        stdscr.clear()
        stdscr.addstr("1. Add information of Student.\n")
        stdscr.addstr("2. Add information of Course.\n")
        stdscr.addstr("3. Show the information.\n")
        stdscr.addstr("4. Fix mark.\n")
        stdscr.addstr("5. Add the mark in Course.\n")
        stdscr.addstr("6. Show mark of student in each Course.\n")
        stdscr.addstr("7. Delete data.\n")
        stdscr.addstr("8. Show mark of each Student.\n")
        stdscr.addstr("9. Rank of GPA.\n")
        stdscr.addstr("*. Clear all data.\n")
        stdscr.addstr("0. Exit\n")
        stdscr.addstr("Please choice: ")
        stdscr.refresh()
        try:
          choose = stdscr.getch()
        
          if (choose == ord('1')):
            student=ip.case_1(student,stdscr)
          elif choose == ord('2'):
            course = ip.case_2(course,stdscr)
          elif choose == ord('3'):
              fc.show_choice(stdscr,student,course)
          elif choose == ord('4'): 
               fc.Fix_point(stdscr,course,student)
          elif choose == ord('5'):
                    while(len(course) == 0):
                         stdscr.addstr(1,10,"There no Course, please input data of course.")
                         course = ip.case_2(course,stdscr)
                    while (len(student)==0):
                         stdscr.addstr(1,10,"There no Student, please input data of Student.")
                         student = ip.case_1(student,stdscr)
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
                    try:
                      want = stdscr.getch()
                      if want == ord('1'):
                          stdscr.clear()
                          idstudent = Box.makebox(stdscr,"ID of student",1,20,2,2)
                          stdscr.refresh()
                          idstudent.edit()
                          dem = 0
                          for x in range(len(student)):
                              if student[x].id == idstudent.gather():
                                  fc.remove_student(student[x],course)
                                  student = np.delete(student,x)
                                  stdscr.addstr(6,20,"This Student was remove done!")
                                  break
                              else:
                                  dem +=1
                          if dem > len(student):
                              stdscr.addstr(10,20,"This ID is not exists!")
                      elif want == ord('2'):
                          stdscr.clear()
                          idcourse = Box.makebox(stdscr,"ID of course",1,20,2,2)
                          stdscr.refresh()
                          idcourse.edit()
                          dow = 0
                          for m in range(len(course)):
                              if course[m].id == idcourse.gather():
                                  fc.remove_course(course[m],student)
                                  course = np.delete(course,m)
                                  stdscr.addstr(6,20,"This Course was remove done!")
                                  break
                              else:
                                  dow +=1
                          if dow > len(course):
                              stdscr.addstr(10,20,"This ID of course is not exists!")
                      else:
                          stdscr.addstr(10,20,"Wrong input, please try again from frist menu!")
                    except ValueError:
                         stdscr.addstr(5,5,"Something wrong, it's not work!")
                         stdscr.refresh()
                         stdscr.addstr(18,25,"Press any key to continue ...")
                         stdscr.getch()
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
                            with open('marks.txt','w') as file:
                                pass
                    elif sure == ord("N") or sure == ord("n"):  
                            stdscr.addstr(20,30,"OK, fine!")
                            stdscr.refresh()
                            stdscr.addstr(18,25,"Press any key to continue ...")
                            stdscr.getch()
                    else:
                          break
                    stdscr.refresh()
                    stdscr.addstr(18,25,"Press any key to continue ...")
                    stdscr.getch()
          elif choose == ord('0'):
                     try:
                       fc.write_file(student)
                       fc.print_file(course)
                       fc.write_mark(course)
                       fc.zip_file()
                     except IOError:
                          print("Error in write to file.")
                     break     
        except KeyboardInterrupt:
             try:
                 fc.write_file(student)
                 fc.print_file(course)
                 fc.write_mark(course)
             except IOError:
                   print("Error in write to file.")
             fc.zip_file()
             break

if __name__=="__main__":
   wrapper(main)
   
   
