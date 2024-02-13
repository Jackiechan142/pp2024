import math
def round_down(number):
    a = number*10
    newnumber= float(math.floor(a)/10)
    return newnumber
# calculate the GPA 
def cla_GPA(mark, credict):
    result = float(mark * credict)
    return result

# remove student
def remove_student(stud):
    a = input("ID of student you want to remove: ")
    cout = 0
    for i in range(len(stud)):
        if (a == stud[i].id):
            stud.remove(stud[i])
        else:
            cout = cout +1
    if (cout == len(stud)):
        print("This ID is not found.")

def clear():
    print("\033c")

def exit():
    input("\nPress Enter to exit ...")
    clear()

