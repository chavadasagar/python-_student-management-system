from os import name
import sqlite3 as sql

class std():

    name = ""
    no = ""
    ct = ""

    con = sql.connect("std.db")

    def __init__(self,name,no,ct):
        self.name = name
        self.no = no          
        self.ct = ct  

    def __init__(self):
        pass   

    def setnm(self,nm):
        self.name = name
    def setct(self,ct):
        self.ct = ct
    def setphno(self,no):
        self.no = no
    

    def save(self):
        try:
            data = (self.name,self.no,self.ct)
            self.con.execute(f"insert into info(name,phno,ct) values(?,?,?)",data)
            self.con.commit()
        except Exception as e:
            print(e)
    def update(self,id,name,phno,ct):
        val = (name,phno,ct,id)
        sql = "update info set name=?,phno=?,ct=? where id = ?"
        self.con.execute(sql,val)
        self.con.commit()

    def delete(self,id):
        try:
            self.con.execute(f"delete from info where id=?",id)
            self.con.commit()
        except Exception as e:
            print(e)  
    def showall(self):
        rec = self.con.execute("select * from info")
        return rec.fetchall()
    def show_specific(self,id):
        rec = self.con.execute("select * from info where id=?",id)
        return rec.fetchall()
    def search(self,search):
         rec = self.con.execute(f"select * from info where name like '%{search}%' or id like '%{search}%' or ct like '%{search}%' or phno like '%{search}%'")
         return rec.fetchall()
