# This program creates a GUI Where the administration can customize their times depending on the school.
from tkinter import *
from datetime import *
import time
from tkinter import ttk

window = Tk()

window.title("ALARM MANAGEMENT PLATFORM")

menu = Menu(window)
window.config(menu=menu)
filemenu = Menu(menu)

controlsMap = {}

options1 = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12",
            "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24")

options2 = ("00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12",
            "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24")

def getting_time():
    global hour
    global minute
    alarm_time = e.get()
    #minute = int(e1.get())
    #string_date = datetime.now()
    current_time = time.strptime("%H:%M")

    while alarm_time != current_time:
        print("THis time is not the same...")
        time.sleep(1)
    if alarm_time == current_time:
        print("THis time is the same")



def callbackFunc(name, index, mode):
    value = window.getvar(name)
    widget = controlsMap[name]
    widget.config(bg='SystemButtonFace', fg='SystemButtonText',
                  activatebackground='SystemButtonFace',
                  activateforeground='SystemButtonText')

#Creating the different labels
L1 = Label(window, text="Morning Class: ")
L1.grid(row=0, column=0)

L2 = Label(window, text="Break starts at: ")
L2.grid(row=1, column=0)

L3 = Label(window, text="Break ends at: ")
L3.grid(row=2, column=0)

L4 = Label(window, text="End of Classes: ")
L4.grid(row=3, column=0 )

L5 = Label(window, text=" : ")
L5.grid(row=1, column=2)

variable1 = StringVar(window, name='variable1')
set1 = OptionMenu(window, variable1, *options1)
set1.configure(width=2)
set1.grid(row=0, column=1)
controlsMap['variable1'] = set1
variable1.trace_variable('w', callbackFunc)

variable = StringVar
e = ttk.Entry(window, width = 14)
e.grid(row=1, column=1)

#variable2 = StringVar
#e1 = Entry(window, width = 4)
#e1.grid(row=1, column=3)

B1 = Button(window, text="SET", command= getting_time)
B1.grid(row=4, column=3)


window.mainloop()

