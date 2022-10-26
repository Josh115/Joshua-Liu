#Clyde "Thluffy" Sinclair
#SoftDev  
#skeleton/stub :: SQLITE3 BASICS
#Oct 2022

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O


DB_FILE="discobandit.db"


db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

#==========================================================

c.execute("create table students(f1)")
# < < < INSERT YOUR TEAM'S POPULATE-THE-DB CODE HERE > > >
with open ("students.csv") as csvfile:
    Return_dict_reader = csv.DictReader(csvfile)
    #example row in students: {'name': 'alison', 'age': '23', 'id': '10'}
    for row in Return_dict_reader:
        c.executescript("insert into students values(" + row.get('name') + " );")




command = ""          # test SQL stmt in sqlite3 shell, save as string
c.execute(command)    # run SQL statement

#==========================================================

db.commit() #save changes
db.close()  #close database


