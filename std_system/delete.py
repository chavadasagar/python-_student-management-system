import tkinter as tk
from tkinter import Button, Entry, Frame, Label, Message, StringVar,IntVar,messagebox
from tkinter import font
from tkinter.constants import SOLID, X




def delete():   
    root = tk.Tk(className="Delete")
    root.minsize(500,450)
    root.maxsize(500,450)


    sid = IntVar()
    nm = StringVar()
    phno = IntVar()
    ct = StringVar()


    # title 
    title_frame = Frame(root)
    title = Label(title_frame,text="Delet Student",font=("arial",30,))
    title.pack(fill=X)
    title_frame.pack()

    main_frame = Frame(root)

    id = Label(main_frame,text="id :",font=("arial",15))
    id.grid(row=1,column=1,pady=20)
    id_textbox = Entry(main_frame,font=("arial",15),textvariable=sid)
    id_textbox.grid(row=1,column=2,pady=20)

    


    add_btn = Button(main_frame,text="delete",font=("arial",15),relief='groove',border=6)
    add_btn.grid(row=5,column=2,pady=20)

    main_frame.pack(pady=20)





    root.mainloop()

