# 1 top scoring student by subject using
import csv
subj = {}
with open("demo.csv", "r")as file:
    r = csv.reader(file)
    next(r)
    for roll, name, subject, marks in r:
        marks = int(marks)
        if subject not in subj or marks> subj[subject][1]:
            subj[subject] = (name, marks)
for subject,(name, marks) in subj.items():
    print(f"subject : {subject} {name} {marks}")