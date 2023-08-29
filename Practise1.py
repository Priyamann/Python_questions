## Obtain a list of students who passed and failed out in a class of 10 students with unique student ids from 1 to 10 and their marks for 5 different subjects out of 100.
## The overall passing grade is 75% and any student having overall marks below 75 fails.
import math 

StudentID = int(input("Enter student ID from 1 to 10" ))
marks = [int(input("Enter the marks of student separated by spaces: "))]
marks = marks.split()
total = sum(marks) / 5
D= {StudentID: total}
print("Student id & their total percentage out of 100", D)





