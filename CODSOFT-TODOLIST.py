import random
from tkinter import *
from tkcalendar import *
root=Tk()
root.geometry('800x800')
root.minsize(700,600)
root.maxsize(700,600)
root.title('TO DO LIST')
import tkinter as tk
from tktimepicker import AnalogPicker, AnalogThemes



def next_step():

    for widget in root.winfo_children():


             widget.destroy()



    def pickdate(event):
        global cal,root2
        root2=Toplevel()
        root2.grab_set()
        root2.title('Choose date')
        root2.geometry('300x300')
        cal=Calendar(root2,selectmode='day',date_pattern='dd/mm/y')
        cal.place(x=20,y=50)
        submit=Button(root2,text='submit',command=getvals)
        submit.place(x=150,y=250)
    def picktime(event):
        global time_picker,root3
        root3=Toplevel()
        root3.geometry('350x350')
        time_picker = AnalogPicker(root3)
        theme = AnalogThemes(time_picker)
        theme.setDracula()
        time_picker.pack()
        Button(root3,text='Set',command=gettime).pack()

    def gettime():
        selected_hour = int(time_picker.hours())
        selected_minute = int(time_picker.minutes())
        selected_time = f"{selected_hour:02d}:{selected_minute:02d}"
        time.delete(0, END)
        time.insert(0, selected_time)
        root3.destroy()

    def delete_task():
        try:
            index = listbox.curselection()[0]
            listbox.delete(index)
        except IndexError:
            pass

    def getvals():
        date.delete(0,END)
        date.insert(0,cal.get_date())
        root2.destroy()
    def add():
        listbox.insert(tk.END,f' {name.get():<30} {date.get():<20} {time.get():<20}')
    Label(root,text='TO DO LIST',fg='red',font='comicsans 35 bold',bg='pink').pack()
    Label(root,text='Enter name of task',bg='pink',font='lucida 20 bold').pack()
    name=Entry(root)
    name.insert(0,'Enter name here')
    name.pack()
    Label(root,text='Select date and time',bg='pink',font='comicsans 20 bold').pack()
    date=Entry(root)
    date.insert(0,'dd/mm/y')
    date.bind('<1>',pickdate)
    date.pack()
    time=Entry(root)
    time.insert(0, '00:00')
    time.bind('<1>',picktime)
    time.pack()
    Button(root,text='ADD',command=add).pack()
    listbox=Listbox(root,height=20,width=90,bg='#C9A9A6',font='Courier 10')
    listbox.insert(tk.END, f'Task{" "*30} Date{" "*15} Time')
    listbox.insert(END,'-------------------------------------------------------------------')
    listbox.pack()
    button_delete_task = tk.Button(root, text="Delete Task", width=15, command=delete_task)
    button_delete_task.pack()




root.configure(background='pink')
Label(root,text='TO DO LIST',fg='red',font='comicsans 35 bold',bg='pink').pack()
kitty=PhotoImage(file='kitty.png')
Label(root,image=kitty).pack()
Label(root,text='Add new tasks',bg='pink',fg='red',font='comicsans 20 bold').pack()
new_image = PhotoImage(file='Plus image.png')
smaller_image = new_image.subsample(3, 3)
Button(root,image=smaller_image,command=next_step,padx=20,pady=20).pack()






root.mainloop()



