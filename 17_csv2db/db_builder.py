# Team SulTan - Ahmed Sultan and Manfred Tan
# SoftDev1 pd9
# K17 -- No Trouble
# 2019-10-08

import sqlite3  # enable control of an sqlite database
import csv  # facilitate CSV I/O

# creating/accessing SQLite3 database file
DB_FILE = "school.db"
db = sqlite3.connect(DB_FILE)
c = db.cursor()  # facilitate db ops

# creating students table
command = "CREATE TABLE students(ID INT PRIMARY KEY, NAME TEXT NO NULL, AGE INT NO NULL);"
c.execute(command)

# reading through students.csv, populating students table
# information ::: id, name, age
with open('students.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        command = "INSERT INTO students VALUES(" + row['id'] + ", '" + row['name'] + "', " + row['age'] + ");"
        c.execute(command)

###########################################################

# creating courses table
command = "CREATE TABLE courses(ID INT, CODE TEXT NO NULL, MARK INT NO NULL);"
c.execute(command)

# reading through course.csv, populating courses table
# information ::: id, code, mark

with open('courses.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        command = "INSERT INTO courses VALUES(" + row['id'] + ", '" + row['code'] + "', " + row['mark'] + ");"
        c.execute(command)

q = "SELECT name, students.id, mark FROM students, courses WHERE students.id = courses.id;"
foo = c.execute( q )

print(foo)

for bar in foo:
    print(bar)

# saving and exiting
db.commit()
db.close()
