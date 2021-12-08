import tkinter as tk
from tkinter import Button, Entry, Frame, Label, Message, StringVar,IntVar,messagebox
from tkinter import font
from tkinter.constants import SOLID, X
from function import control




def add():   
    root = tk.Tk(className="student manage system")
    root.minsize(500,360)
    root.maxsize(500,360)

    nm = StringVar()
    phno = IntVar()
    ct = StringVar()

    # title 
    title_frame = Frame(root)
    title = Label(title_frame,text="Add Student",font=("arial",30,))
    title.pack(fill=X)
    title_frame.pack()

    main_frame = Frame(root)

    std_name = Label(main_frame,text="Name :",font=("arial",15))
    std_name.grid(row=1,column=1,pady=20)
    std = Entry(main_frame,font=("arial",15),textvariable=nm)
    std.grid(row=1,column=2,pady=20)

    std_no = Label(main_frame,text="Phone No :",font=("arial",15))
    std_no.grid(row=2,column=1,pady=20)
    std_no_textbox = Entry(main_frame,font=("arial",15),textvariable=phno)
    std_no_textbox.grid(row=2,column=2,pady=20)

    std_ct = Label(main_frame,text="City :",font=("arial",15))
    std_ct.grid(row=3,column=1,pady=20)
    std_ct_textbox = Entry(main_frame,font=("arial",15),textvariable=ct)
    std_ct_textbox.grid(row=3,column=2,pady=20)



    def save():
        print(std.get())
        print(std_no_textbox.get())
        print(std_ct_textbox.get())

        control.save(std.get(),std_no_textbox.get(),std_ct_textbox.get())



    add_btn = Button(main_frame,text="Add Student",font=("arial",15),relief='groove',border=6,command=save)
    add_btn.grid(row=4,column=2,pady=20)

    

    main_frame.pack(pady=20)





    root.mainloop()

