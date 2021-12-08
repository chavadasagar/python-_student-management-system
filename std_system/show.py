import tkinter as tk
from tkinter import Button, Entry, Frame, Label, Message, StringVar,IntVar,messagebox
from tkinter import font
from tkinter.constants import SOLID, X




def show():   
    root = tk.Tk(className="show student")
    root.minsize(500,360)
    root.maxsize(500,360)




    # title 
    title_frame = Frame(root)
    title = Label(title_frame,text="show",font=("arial",30,))
    title.pack(fill=X)
    title_frame.pack()

    main_frame = Frame(root)

    std_name = Label(main_frame,text="Search :",font=("arial",15))
    std_name.grid(row=1,column=1,pady=20)
    std = Entry(main_frame,font=("arial",15))
    search_btn = Button(main_frame,font=("arial",15),text="Search")
    std.grid(row=1,column=2,pady=20)
    search_btn.grid(row=1,column=3,pady=20,padx=10)



    main_frame.pack(pady=20)





    root.mainloop()
