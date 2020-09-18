
# Import tkinter as tk
import tkinter as tk
from tkinter import *
from data_call import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

# creating a new tkinter window
master = tk.Tk()

# assigning a title
master.title("MARKSHEET")

# specifying geomtery for window size
master.geometry("700x250")

#master.wm_attributes('-transparentcolor','black')

#C = Canvas(master, bg="blue", height=250, width=300)
#filename = PhotoImage(file = "bg.png")
#background_label = Label(master, image=filename)
#background_label.place(x=0, y=0, relwidth=1, relheight=1)
#C.grid()
bgimage = PhotoImage(file = r"bg.png")
Label(master, image = bgimage).place(relwidth = 1, relheight = 1)


l1 = tk.Label(text="Wisdom Tests and Math Challenge", fg="black", bg="LightBlue1",font='helvetica 12')
l1.config(font=('Arial', 20))
l1.grid(row = 1, column = 7)


photo = PhotoImage(file = '10.png')
lablephoto = Label(master, image = photo)
lablephoto.grid(row = 2, column = 11)





tk.Label(master, text="Name of candidate",bg="LightBlue1").grid(row=20,column=3)
tk.Label(master, text=name[0],bg="LightBlue1").grid(row=20, column=4)


tk.Label(master, text="Grade",bg="LightBlue1").grid(row=21, column=3)
tk.Label(master, text=grade[0],bg="LightBlue1").grid(row=21, column=4)


tk.Label(master, text="School Name",bg="LightBlue1").grid(row=22, column=3)
tk.Label(master, text=school_name[0],bg="LightBlue1").grid(row=22, column=4)

tk.Label(master, text="City of Residence",bg="LightBlue1").grid(row=23, column=3)
tk.Label(master, text=residence[0],bg="LightBlue1").grid(row=23, column=4)

tk.Label(master, text="Country of Residence",bg="LightBlue1").grid(row=24, column=3)
tk.Label(master, text=country[0],bg="LightBlue1").grid(row=24, column=4)


#next clounm
tk.Label(master, text="Reg.No",bg="LightBlue1").grid(row=20, column=7)
tk.Label(master, text=Registration[0],bg="LightBlue1").grid(row=20, column=8)


tk.Label(master, text="Gender",bg="LightBlue1").grid(row=21, column=7)
tk.Label(master, text=gender[0],bg="LightBlue1").grid(row=21, column=8)


tk.Label(master, text="Date of Birth",bg="LightBlue1").grid(row=22, column=7)
tk.Label(master, text=DOB[0],bg="LightBlue1").grid(row=22, column=8)


tk.Label(master, text="Date of Test",bg="LightBlue1").grid(row=23, column=7)
tk.Label(master, text=DOT[0],bg="LightBlue1").grid(row=23, column=8)


tk.Label(master, text="Extra Time assistance",bg="LightBlue1").grid(row=24, column=7)
tk.Label(master, text=ETA[0],bg="LightBlue1").grid(row=24, column=8)


#for extra space
tk.Label(master, text="            ",bg="LightBlue1").grid(row=25, column=7)

#send heading student performance
l2 = tk.Label(text="Student Performance", fg="black",bg="LightBlue1",font='helvetica 12')
l2.config(font=('Arial', 20))
l2.grid(row = 26, column = 7)

#table
tk.Label(master,text = 'Question number',bg="LightBlue1").grid(row=27,column=3)
#question numbers
tk.Label(master,text = 'Q1',bg="LightBlue1").grid(row=28,column=3)
tk.Label(master,text = 'Q2',bg="LightBlue1").grid(row=29,column=3)
tk.Label(master,text = 'Q3',bg="LightBlue1").grid(row=30,column=3)
tk.Label(master,text = 'Q4',bg="LightBlue1").grid(row=31,column=3)
tk.Label(master,text = 'Q5',bg="LightBlue1").grid(row=32,column=3)

#Time Spent on question (sec)
tk.Label(master,text ='Time Spent on question (sec)',bg="LightBlue1").grid(row=27,column=4)
tk.Label(master,text =time_spent[0],bg="LightBlue1").grid(row=28,column=4)
tk.Label(master,text =time_spent[1],bg="LightBlue1").grid(row=29,column=4)
tk.Label(master,text =time_spent[2],bg="LightBlue1").grid(row=30,column=4)
tk.Label(master,text =time_spent[3],bg="LightBlue1").grid(row=31,column=4)
tk.Label(master,text ='35',bg="LightBlue1").grid(row=32,column=4)


#Score if correct
tk.Label(master,text ='Score if correct',bg="LightBlue1").grid(row=27,column=5)
tk.Label(master,text = '2',bg="LightBlue1").grid(row=28,column=5)
tk.Label(master,text = '2',bg="LightBlue1").grid(row=29,column=5)
tk.Label(master,text = '2',bg="LightBlue1").grid(row=30,column=5)
tk.Label(master,text = '2',bg="LightBlue1").grid(row=31,column=5)
tk.Label(master,text = '2',bg="LightBlue1").grid(row=32,column=5)

#Score if incorrect
tk.Label(master,text ='Score if incorrect',bg="LightBlue1").grid(row=27,column=6)
tk.Label(master,text = '-1',bg="LightBlue1").grid(row=28,column=6)
tk.Label(master,text = '-1',bg="LightBlue1").grid(row=29,column=6)
tk.Label(master,text = '-1',bg="LightBlue1").grid(row=30,column=6)
tk.Label(master,text = '-1',bg="LightBlue1").grid(row=31,column=6)
tk.Label(master,text = '-1',bg="LightBlue1").grid(row=32,column=6)

#Attempt status
tk.Label(master,text ='Attempt Status',bg="LightBlue1").grid(row=27,column=7)
tk.Label(master,text = attempt_status[0],bg="LightBlue1").grid(row=28,column=7)
tk.Label(master,text = attempt_status[1],bg="LightBlue1").grid(row=29,column=7)
tk.Label(master,text = attempt_status[2],bg="LightBlue1").grid(row=30,column=7)
tk.Label(master,text = attempt_status[3],bg="LightBlue1").grid(row=31,column=7)
tk.Label(master,text = 'Attempted',bg="LightBlue1").grid(row=32,column=7)


#What you marked
tk.Label(master,text ='What You Marked',bg="LightBlue1").grid(row=27,column=8)
tk.Label(master,text =what_you_marked[0],bg="LightBlue1").grid(row=28,column=8)
tk.Label(master,text =what_you_marked[1],bg="LightBlue1").grid(row=29,column=8)
tk.Label(master,text =what_you_marked[2],bg="LightBlue1").grid(row=30,column=8)
tk.Label(master,text =what_you_marked[3],bg="LightBlue1").grid(row=31,column=8)
tk.Label(master,text ='E',bg="LightBlue1").grid(row=32,column=8)


#Correct Answer
tk.Label(master,text ='correct Answer',bg="LightBlue1").grid(row=27,column=9)
tk.Label(master,text = 'A',bg="LightBlue1").grid(row=28,column=9)
tk.Label(master,text = 'B',bg="LightBlue1").grid(row=29,column=9)
tk.Label(master,text = 'C',bg="LightBlue1").grid(row=30,column=9)
tk.Label(master,text = 'D',bg="LightBlue1").grid(row=31,column=9)
tk.Label(master,text = 'E',bg="LightBlue1").grid(row=32,column=9)

#Outcome (Correct/Incorrect/Not Attempted)
tk.Label(master,text ='Outcome',bg="LightBlue1").grid(row=27,column=10)
tk.Label(master,text =outcome[0],bg="LightBlue1").grid(row=28,column=10)
tk.Label(master,text =outcome[1],bg="LightBlue1").grid(row=29,column=10)
tk.Label(master,text =outcome[2],bg="LightBlue1").grid(row=30,column=10)
tk.Label(master,text =outcome[3],bg="LightBlue1").grid(row=31,column=10)
tk.Label(master,text ='Correct',bg="LightBlue1").grid(row=32,column=10)


#Your Score
tk.Label(master,text ='Your Score',bg="LightBlue1").grid(row=27,column=11)
tk.Label(master,text =Your_Score[0],bg="LightBlue1").grid(row=28,column=11)
tk.Label(master,text =Your_Score[1],bg="LightBlue1").grid(row=29,column=11)
tk.Label(master,text =Your_Score[2],bg="LightBlue1").grid(row=30,column=11)
tk.Label(master,text =Your_Score[3],bg="LightBlue1").grid(row=31,column=11)
tk.Label(master,text ='2.0',bg="LightBlue1").grid(row=32,column=11)

tk.Label(master,text ='     ',bg="LightBlue1").grid(row=33,column=11)

a = sum(Your_Score)
sum = a + 2
tk.Label(master,text ='Total Score',bg="LightBlue1").grid(row=35,column=3)
tk.Label(master,text =sum,bg="LightBlue1").grid(row=35,column=4)

#overall percentage
tk.Label(master,text ='Your overall percentile',bg="LightBlue1").grid(row=36,column=3)
tk.Label(master,text =percen,bg="LightBlue1").grid(row=36,column=4)

def time_spend_piechart():
    qus = ['Q1','Q2','Q3','Q4']

    data = df3['Time Spent on question (sec)']

    # Creating plot
    fig = plt.figure(figsize =(5, 4))
    plt.pie(data, labels = qus)
        # show plot
    plt.show().get_tk_widget().grid(row = 40,column =10)

button1 = Button(master, text = 'time spend on each question',command =time_spend_piechart )
button1.grid(row =37 , column = 3)


def attempted_Unattempted():
    a = attempt_status.count("Attempted")
    b = attempt_status.count("Unattempted")
    lable = ['attempted','Unattempted']
    data = [a,b]
    fig = plt.figure(figsize =(5, 4))
    plt.pie(data, labels = lable)
        # show plot
    plt.show().get_tk_widget().grid(row = 40,column =10)

button2 = Button(master, text = 'attempted/unattempted',command =attempted_Unattempted)
button2.grid(row =37 , column = 5)






def accuracy():
    a = outcome.count("Correct")
    b = 5 - a
    lable = ['Correct','Incorrect']
    data = [a,b]
    fig = plt.figure(figsize =(5, 4))
    plt.pie(data, labels = lable)
        # show plot
    plt.show().get_tk_widget().grid(row = 40,column =12)

button3 = Button(master, text = 'Accuray of attempted question',command =accuracy)
button3.grid(row =37 , column = 7)











master.mainloop()
