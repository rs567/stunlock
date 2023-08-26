import sqlite3
import csv #adds csv library to read csv files
conn = sqlite3.connect('metals.db') #Creates database called gold
cursor = conn.cursor() #apparently you need this to execute SQL commands
cursor.execute('''CREATE TABLE IF NOT EXISTS Gold (
                    Date,
                    Close_Last,
                    Volume,
                    Open,
                    High,
                    Low
                 )''') #first sql commands make table called gold, collums will be csv categories
#r is a prefix that goes before file paths, i'm a dumbass
temp = cursor.execute('''
Select *
From Gold
;
''')
rows = cursor.fetchall()
i = 0
while (i < 10):
    print(rows[i])
    i=i+1

conn.commit() #commits all the shit into itself and makes it permanant 
conn.close() #kills itself

































