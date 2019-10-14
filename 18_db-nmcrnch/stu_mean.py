# Team J.Homework
# SoftDev1 pd9
# K #18: Average
# 2019-10-14

import sqlite3  # enable control of an sqlite database
import csv  # facilitate CSV I/O


DB_FILE = "school.db"
db = sqlite3.connect(DB_FILE)
c = db.cursor()  # facilitate db ops

##################

def stu_avg():
    #look up each students grades
    command = "SELECT courses.id, name, mark FROM students, courses WHERE students.id = courses.id;"
    data = c.execute(command)

    #create dictionary of each students grades, num of classes, average
    #dict: ID = [Total Grade, Num of Classes, Average, Name]
    stu_data = {}
    for row in data:
        ID = row[0]
        grade = row[2]
        if ID in stu_data:
            totalGrade = stu_data.get(ID)[0] + grade
            freq = stu_data.get(ID)[1] + 1
            stu_data[ ID ] = [totalGrade, freq, totalGrade / freq, row[1]]
        else:
            stu_data[ ID ] = [grade, 1, grade, row[1]]
    print(stu_data)

    #create table of students and averages
    command = "CREATE TABLE stu_avg(ID INT PRIMARY KEY, NAME TEXT NO NULL, AVERAGE INT NO NULL);"
    c.execute(command)

    # populating stu_avg table
    # information ::: id, average
    for key in stu_data.keys():
        command = "INSERT INTO stu_avg VALUES(" + str(key) + ", '" + stu_data.get(key)[3] + "', " + str( stu_data.get(key)[2] ) + ");"
        c.execute(command)

##################

def add_Rows(ID, code, mark):
    command = "SELECT * FROM courses"
    courses = c.execute(command)

    #add vales into courses table
    command = "INSERT INTO courses VALUES (" + str(ID) + ", '" + code + "', " + str(mark) + ");"
    c.execute(command)


##################

stu_avg()
add_Rows(11, 'calculus', 100)


# saving and exiting
db.commit()
db.close()
