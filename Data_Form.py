from tkinter import *
import sqlite3 as sq #pysql,pymysql
from tkinter import messagebox as msg
import scrolling
r=Tk()
r.config(bg='#38031d')
r.geometry('900x700')
def main(r):
    f=Frame(r,width=900,height=700,bg='#2e2329')
    f.pack(expand=True)
    l1=Label(f,text='Name',bg='white',fg='black',font=('arial',20,'bold'))
    l1.place(x=70,y=50)
    e1=Entry(f,font=('arial',20,'bold'))
    e1.place(x=200,y=50)
    l2=Label(f,text='I\'D',bg='white',fg='black',font=('arial',20,'bold'))
    l2.place(x=70,y=100)
    e2=Entry(f,font=('arial',20,'bold'))
    e2.place(x=200,y=100)
    l3=Label(f,text='email',bg='white',fg='black',font=('arial',20,'bold'))
    l3.place(x=70,y=150)
    e3=Entry(f,font=('arial',20,'bold'))
    e3.place(x=200,y=150)
    l4=Label(f,text='Mob.No.',bg='white',fg='black',font=('arial',20,'bold'))
    l4.place(x=70,y=200)
    e4=Entry(f,font=('arial',20,'bold'))
    e4.place(x=200,y=200)
    l5=Label(f,text='Address',bg='white',fg='black',font=('arial',20,'bold'))
    l5.place(x=70,y=250)
    e5=Entry(f,font=('arial',20,'bold'))
    e5.place(x=200,y=250)
    l6=Label(f,text='Date',bg='white',fg='black',font=('arial',20,'bold'))
    l6.place(x=70,y=300)
    e6=Entry(f,font=('arial',20,'bold'))
    e6.place(x=200,y=300)
    b1=Button(f,text='Quit',bg='white',fg='black',font=('arial',20,'bold'),command=lambda:Quit(f,r))
    b1.place(x=70,y=600)
    b2=Button(f,text='Submit',bg='white',fg='black',font=('arial',20,'bold'),command=lambda:submit(e1,e2,e3,e4,e5,e6,var))
    b2.place(x=500,y=600)
    b3=Button(f,text='Show All',command=lambda:show(f,r),bg='white',fg='black',font=('arial',20,'bold'))
    b3.place(x=650,y=50)
    l7=Label(f,text='Field',bg='white',fg='black',font=('arial',20,'bold'))
    l7.place(x=70,y=350)
    #e6=Entry(f,font=('arial',20,'bold'))
    #e6.place(x=200,y=350)
    var=StringVar()
    var.set(None)

    op=OptionMenu(f,var,'CS','ECE','EE','CIVIL','IT','ME')
    op.config(bg='white',fg='#2e2329',font=('arial',20,'bold'))
    op.place(x=200,y=350)

def submit(e1,e2,e3,e4,e5,e6,var):
    t1=e1.get()
    t2=e2.get()
    t3=e3.get()
    t4=e4.get()
    t5=e5.get()
    t6=e6.get()
    t7=var.get()
    conn=sq.connect('XYZ.db')
    conn.execute('''create table if not exists sakshi1(Name Text,Id INTEGER, email INTVAR, Mobile INTEGER,Address INTVAR,Date TEXT,Field text)''')
    conn.execute('''insert into sakshi1 values (?,?,?,?,?,?,?)''',(t1,int(t2),t3,int(t4),t5,t6,t7))
    conn.commit()
    conn.close()
    msg.showinfo('title','successfully updated!!')
def show(f,r):
    conn=sq.connect('XYZ.db')
    cur=conn.execute('''SELECT * from sakshi1 ''')
    for i in cur:
        print(i)
        f.destroy()
        f1=Frame(r,bg='black',width=900,height=700)
        f1.pack(expand=True)
        scl=scrolling.Scrolling_Area(f1,width=900,height=600)
        scl.place(x=0,y=0)
        table=scrolling.Table(scl.innerframe,['Name','Id','email','Mobile','Address','Date','Field'],column_minwidths=[140,140,140,140,140,140])
        table.pack(expand=True,fill=X)
        table.on_change_data(scl.update_viewport)
        data=[]
        for row in cur:
            column=[]
            data.append(column)
            for r in row:
                column.append(r)
        table.set_data(data)

def Quit(f,r):
    f.destroy()
    r.destroy()
    

main(r)
