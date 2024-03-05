
import Box
# print information of all Student
def print_student_infor(stud,stdscr):
   stdscr.clear()
   stdscr.addstr(0,0,"Student information:\n ")
   stdscr.addstr(2,0,f"{'ID':<15}{'Name':<30}{'Dob':<15}")
   stdscr.addstr(3,0,"-"*60)
   row = 4
   for i in range(len(stud)):
        stdscr.addstr(row,0,f"{stud[i].id:<15}{stud[i].name:<30}{stud[i].Dob:<15}")
        row +=2
   stdscr.refresh()
   stdscr.addstr(row,0,"Press any key to continue ...")
   stdscr.getch()

# print information of all Course
def print_course_infor(Cour,stdscr):
   stdscr.clear()
   stdscr.addstr(0,0,"Course information:\n ")
   stdscr.addstr(2,0,f"{'ID':<15}{'Name':<30}{'Credict':<15}")
   stdscr.addstr(3,0,"-"*60)
   row = 4
   for i in range(len(Cour)):
        stdscr.addstr(row,0,f"{Cour[i].id:<15}{Cour[i].name:<30}{Cour[i].credict:<15}")
        row +=2
   stdscr.refresh()
   stdscr.addstr(row,0,"Press any key to continue ...")
   stdscr.getch()
# print mark of Course want to see
def print_mark_of_course(Cour,stdscr):
     stdscr.clear()
     stdscr.addstr(0,20,"Course you want to see mark\n")
     n = Box.makebox(stdscr,"ID",1,20,2,2)
     stdscr.refresh()
     n.edit()
     cont = 0
     for i in range(len(Cour)):
            if (n.gather() == Cour[i].id):
                Cour[i].print(stdscr)
            else:
                cont = cont+1
     if (cont == len(Cour)):
        stdscr.addstr(4,2,"Id of course not found.")
     stdscr.refresh()
     stdscr.addstr(18,25,"Press any key to continue ...")
     stdscr.getch()

# print mark of student
def print_mark_of_student(stud,stdscr):
    stdscr.clear()
    stdscr.addstr(0,10,"Student you want to see mark\n")
    ba = Box.makebox(stdscr,"ID",1,20,2,2)
    stdscr.refresh()
    ba.edit()
    cot = 0
    for i in range(len(stud)):
        if (ba.gather() == stud[i].id):
            stud[i].print(stdscr)
            stdscr.addstr(1,2,f"GPA :{stud[i].GPA()} ")
        else:
           cot = cot +1
    if (cot == len(stud)):
        stdscr.addstr(4,2,"This ID is not found.") 
    stdscr.refresh()
    stdscr.addstr(18,25,"Press any key to continue ...")
    stdscr.getch()
# print Rank of GPA
def print_GPA(stud,stdscr):
    stdscr.clear()
    if len(stud) == 0 :
       stdscr.addstr(1,2,"There no data of Student.")
    else:
       new_list = sorted(stud, key=lambda x: x.GPA(), reverse=True)
       row = 4
       for i in range(len(new_list)):
            new_list[i].rank(stdscr,row)
            row += 2
       stdscr.refresh()
       stdscr.addstr(18,25,"Press any key to continue ...")
       stdscr.getch()