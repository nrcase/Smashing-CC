import mysql.connector
import csv
import pandas as pd

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="toyfactory",
)
mycursor = mydb.cursor()

mycursor.execute("USE cc")

with open("/Users/nrcase/research/cc-repo/cc/processing/mapping.txt", "r") as file:
  lines = file.read().splitlines() #read in lines
    
with open("/Users/nrcase/research/cc-repo/cc/processing/patterns.csv", "r") as file:
  patterns_list = file.readlines() #read in as line, so each index is a pattern

for mapping in lines: #for each tuple in mapping.txt
    array = mapping.split(",") 
    real = array[0]
    anon = array[1] #split it into the real name, the anon name and the pattern numerb
    pattern = array[2]

    long_pattern = patterns_list[int(pattern)] #get the written out pattern for the pattern ID
    long_pattern = long_pattern.strip() #strip the newline character
    
    long_pattern = long_pattern.split(",") #split the pattern into a list of the each letter and whether EQ or NEQ

    mycursor.execute("INSERT INTO repos(anon, pattern, A, B, C, D, E, F, G, H) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (anon, pattern, long_pattern[1], long_pattern[2], long_pattern[3], long_pattern[4], long_pattern[5], long_pattern[6], long_pattern[7], long_pattern[8])) 
    mycursor.execute("INSERT INTO anon(anon, unityID) VALUES (%s, %s)", (anon, real))
    
mydb.commit()
    
    
    

