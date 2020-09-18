import pandas as pd
import sklearn
import matplotlib.pyplot as plt
import sys
import scipy
import numpy as np
import matplotlib

names = ['serial_no','Student No','Name of Candidate','Registration','Grade' ,'Gender','Name of school' ,'Date of Birth' ,'City of Residence','Date and time of test','Country of Residence','Extra time assistance','Question No.','Time Spent on question (sec)','Score if correct','Score if incorrect','Attempt status' ,'What you marked','Correct Answer','Outcome','Your score']
df = pd.read_csv('Assignment.csv',names=names)

df1 = df.drop(columns= 'serial_no')
df2 = df1.drop([0],axis=0)

total_score = df2['Your score'].tolist()
s1 = total_score[0:4]
s1_s = sum(s1)
s2 = total_score[5:10]
s2_s = sum(s2)
s3 = total_score[10:15]
s3_s = sum(s3)
s4 = total_score[15:20]
s4_s = sum(s4)
s5 = total_score[20:25]
s5_s = sum(s5)
s6 = total_score[25:30]
s6_s = sum(s6)
s7 = total_score[25:30]
s7_s = sum(s7)
s8 = total_score[30:35]
s8_s = sum(s8)
s9 = total_score[35:40]
s9_s = sum(s9)
s10 = total_score[40:45]
s10_s = sum(s10)
total = [s1_s,s2_s,s3_s,s4_s,s5_s,s6_s,s7_s,s8_s,s9_s,s10_s]
sorted = total.sort()
c = sum(x < s6_s for x in total)
percen = c*100/10

df3 = df2[25:30]

name = df3['Name of Candidate'].tolist()

#grade
grade = df3['Grade'].tolist()

#school name
school_name = df3['Name of school'].tolist()

#city of residence
residence = df3['City of Residence'].tolist()

#country of residence
country = df3['Country of Residence'].tolist()


#Registration
Registration = df3['Registration'].tolist()

#gender
gender = df3['Gender'].tolist()

#DOB
DOB = df3['Date of Birth'].tolist()

#DOT
DOT = df3['Date and time of test'].tolist()

#ETA
ETA =df3['Extra time assistance'].tolist()

#time spend
time_spent = df3['Time Spent on question (sec)'].tolist()

#attempt
attempt_status = df3['Attempt status'].tolist()

#what you marked
what_you_marked = df3['What you marked'].tolist()

#outcome
outcome = df3['Outcome'].tolist()

#your score
Your_Score = df3['Your score'].tolist()


#qus no
Qus = df3['Question No.'].tolist()
