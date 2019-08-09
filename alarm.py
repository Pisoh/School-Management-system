# Alarm clock using Python Tkinter module by Rajkumar Selvaraj
from tkinter import *
from tkinter import ttk
import time
import os
from tkinter import messagebox


# def main():
root = Tk()
root.title("School Management")


def SubmitButton():
    global AlarmTime1
    global AlarmTime2
    global AlarmTime3
    AlarmTime1 = entry2.get()
    #AlarmTime2 = entry3.get()
    #AlarmTime3 = entry4.get()
    Message1(AlarmTime1)
    # label2.config(text ="The Alarm will Ring at {} ".format(AlarmTime))  #delayed in execution
    CurrentTime = time.strftime("%H:%M")
    print("the alarm time is: ")
    # label2.config(text="")
    while AlarmTime1 != CurrentTime:
        # label2.config(text ="The Alarm will Ring at {} ".format(AlarmTime))
        print("Alarm not yet on")
        CurrentTime = time.strftime("%H:%M")
        time.sleep(1)
    if AlarmTime1 == CurrentTime:
        print("now Alarm Music 1 Playing")
        #os.system("start alarm-music.mp3")
        label2.config(text="Alarm music playing.....")
        messagebox.showinfo(title='Alarm Message', message="{}".format(entry2.get()))
        #INSERT RASPBERRY FUNCTION  FOR RELAYS
        
def Break_alarm():   #This alarm button is for the start of break
    AlarmTime2 = entry3.get()
    Message1(AlarmTime2)
    # label2.config(text ="The Alarm will Ring at {} ".format(AlarmTime))  #delayed in execution
    CurrentTime = time.strftime("%H:%M")
    print("the alarm time is: {}".format(AlarmTime2))
    # label2.config(text="")
    while AlarmTime2 != CurrentTime:
        # label2.config(text ="The Alarm will Ring at {} ".format(AlarmTime))
        CurrentTime = time.strftime("%H:%M")
        time.sleep(1)
    if AlarmTime2 == CurrentTime:
        print("now Alarm Musing Playing")
        #os.system("start alarm-music.mp3")
        label2.config(text="Alarm music playing.....")
        messagebox.showinfo(title='Alarm Message', message="{}".format(entry3.get()))
        #INSERT RASPBERRY FUNCTION FOR SWITCHING ALARM RELAY
        
def submitButton():  #This alarm button is for the end of the day
    AlarmTime3 = entry4.get()
    Message1(AlarmTime3)
    # label2.config(text ="The Alarm will Ring at {} ".format(AlarmTime))  #delayed in execution
    CurrentTime = time.strftime("%H:%M")
    print("the alarm time is: {}".format(AlarmTime3))
    # label2.config(text="")
    while AlarmTime3 != CurrentTime:
        # label2.config(text ="The Alarm will Ring at {} ".format(AlarmTime))
        CurrentTime = time.strftime("%H:%M")
        time.sleep(1)
    if AlarmTime3 == CurrentTime:
        print("now Alarm Musing Playing")
        #os.system("start alarm-music.mp3")
        label2.config(text="Alarm music playing.....")
        messagebox.showinfo(title='Alarm Message', message="{}".format(entry4.get()))
        #INSERT RASPBERRY FUNCTION FOR SWITCHING ALARM RELAYS
    


def Message1(AlarmTimeLable):
    #AlarmTimeLable = entry1.get()
    label2.config(text="the Alarm time is Counting...")
    # label2.config(text= "the Alarm will ring at {}".format(AlarmTimeLable))
    messagebox.showinfo(title='Alarm clock', message='Alarm will Ring at {}'.format(AlarmTimeLable))


frame1 = ttk.Frame(root)
frame1.pack()
frame1.config(height=200, width=200)

l1 = ttk.Label(frame1, text="SCHOOL CONTROL PANEL")
l1.pack()

def Lighting():
    label = ttk.Label(frame1, text="LIGHTING OPTIONS")
    label.pack()
    Button1 = ttk.Button(frame1, text="Corridors")
    Button1.pack()
    Button2 = ttk.Button(frame1, text="Classrooms")
    Button2.pack()
    Button3 = ttk.Button(frame1, text="Security")
    Button3.pack()
    #INSERT RASPBERRY FUNCTIONS FOR SWITCHING RELAYS FOR LIGHTING

def Alarm_tab():

    label1 = ttk.Label(frame1, text="Enter the Alarm times :")
    label1.pack()

    entry1 = ttk.Entry(frame1, width=30)
    entry1.pack()
    entry1.insert(3, "example - 13:15")

    labelAlarmMessage = ttk.Label(frame1, text="Start of classes:")
    labelAlarmMessage.pack()

    entry2 = ttk.Entry(frame1, width=30)
    entry2.pack()

    labelAlarmMessage = ttk.Label(frame1, text="Break Time:")
    labelAlarmMessage.pack()

    entry3 = ttk.Entry(frame1, width=30)
    entry3.pack()

    labelAlarmMessage = ttk.Label(frame1, text="End of Classes:")
    labelAlarmMessage.pack()

    entry4 = ttk.Entry(frame1, width=30)
    entry4.pack()

    button1 = ttk.Button(frame1, text="submit", command=SubmitButton)
    button1.pack()
    button2 = ttk.Button(frame1, text="Break", command=Break_alarm)
    button2.pack()
    button3 = ttk.Button(frame1, text="end", command=submitButton)
    button3.pack()
    # this Label2 will show the Last Alarm Time
    label2 = ttk.Label(frame1)
    label2.pack()

b1 = ttk.Button(frame1, text="ALARMS", command=Alarm_tab)
b1.pack()

b2 = ttk.Button(frame1, text="LIGHTING", command=Lighting)
b2.pack()
# label2.config(text="hello")

root.mainloop()