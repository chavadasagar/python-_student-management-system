import tkinter as tk
from tkinter import Button, Entry, Frame, Label, Message, StringVar,IntVar,messagebox
from tkinter import font
from tkinter.constants import COMMAND, SOLID, X
import add
import update 
import delete
import show


control = tk.Tk(className="Operations")
control.minsize(500,360)
control.maxsize(500,360)

title_frame = Frame(control)
title = Label(title_frame,text="Manage Student",font=("arial",30,))
title.pack(fill=X)
title_frame.pack()

manage = Frame(control)

insert = Button(manage,font = ("arial",12),text="add student",command=add.add)
update = Button(manage,font = ("arial",12),text="Update",command=update.update)
delete = Button(manage,font = ("arial",12),text="delete",command=delete.delete)
show = Button(manage,font = ("arial",12),text="show all",command=show.show)

insert.grid(row=1,column=1,pady=20)
update.grid(row=1,column=2,pady=20)
delete.grid(row=1,column=3,pady=20)
show.grid(row=1,column=4,pady=20)

manage.pack()

control.mainloop()