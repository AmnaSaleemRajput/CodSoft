from tkinter import *
import random
import tkinter.messagebox as tmsg
root=Tk()
root.title('RANDOM PASSWORD GENERATOR')
root.geometry('350x350')
root.minsize(350,350)
root.maxsize(350,350)
root.config(background='grey')
def gen():
    length=E1.get()
    for widget in root.winfo_children():


             widget.destroy()
    listA=[]
    for i in range(int(length)):
        letters = 'QWERT!£YUIOP67890asdfghj$%klZXCVBNM^&*?/12345zxcvbnmpoiuytrewq'
        passw=random.choice(letters)
        listA.append(passw)
    password=''.join(listA)
    print(password)
    Label(root,text='PASSWORD',font='georgia 25 bold',padx=20,pady=20,bg='grey',fg='purple').pack()
    L2=Entry(root,font='georgia 15 bold')
    L2.insert(0,password)
    L2.pack()
    # Button(root,text='COPY',command=copy,font='lucida 10 bold',padx=10,pady=10).pack()



Label(root,text='PASSWORD',font='georgia 20 bold',bg='grey').pack()
Label1=Label(root,text='Specify the length of Password?',font='georgia 15 bold',fg='purple',bg='grey')
Label1.pack()
intege=IntVar
E1=Entry(root,text=intege)
E1.pack(padx=20,pady=20)


B1=Button(root,text='GENERATE',fg='purple',font='lucida 15 bold',command=gen,bg='grey')
B1.pack()










root.mainloop()


