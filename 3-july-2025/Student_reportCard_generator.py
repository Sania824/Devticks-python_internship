# Student Report Card Generator

def average(marks,subjects):
    return sum(marks)/len(subjects)*100

def total(marks):
    return sum(marks)

def grading(marks):
    if sum(marks) >= 90:
        return "A"
    elif sum(marks) >= 80 and (sum(marks)<90):
        return ""
    elif sum(marks) >= 70 and (sum(marks) < 80):
        return "C"
    elif sum(marks) >= 60 and (sum(marks) < 70):
        return "D"
    else:
        return "F"


def student_details():
    name = input('Enter your name: ')
    ID = input('Enter your Student ID: ')
    subjects = list(map(str, input('Enter your subjects: ').split()))
    marks = list(map(int, input('Enter your marks:').split()))

    print("\nStudent Progess Report")
    print("\nYour Total is: ", total(marks))
    print("Your Average is: ", average(marks,subjects))
    print("Your Grade is: ",grading(marks))
    if grading(marks) == "A":
        print("\nCongratulations! Your academic performance has been incredible")
    elif grading(marks) == "B":
            print("Congratulations! Your academic performance has been good")
    elif grading(marks) == "C":
                print("Your academic performance needs improvement")
    elif grading(marks) == "D":
                print("You barely passed! Work on your academics")
    else:
        print("*Sorry! You Failed!*")
    return name, ID, subjects, marks


name, id, subjects, marks = student_details()