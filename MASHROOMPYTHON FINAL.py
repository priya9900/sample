import tkinter as tk
import tkinter.messagebox
import pandas as p
from tkinter import *

import mysql.connector

import mysql.connector as mysql


#from tkinter import filedialog as fd 
import tkinter.filedialog
from tkinter import ttk

from datetime import datetime
from dateutil import relativedelta
from PIL import ImageTk,Image  

import pandas as p
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from array import *
from pandas import DataFrame
import matplotlib.pyplot as plt

class NewWin():
    
   def __init__(self):
       self.win = tk.Tk()

       self.win.geometry("1000x600+300+100");
       self.win.title(" Mushroom Disease Prediction System ")
       self.win.configure(bg="#912388")
       self.canvas = tk.Canvas(self.win, width = 1000, height = 600)  
       self.canvas.place(x=0,y=0);

       self.img1 = ImageTk.PhotoImage(Image.open("mb2.jpg"))  
       l1 = tk.Label(self.win, image=self.img1,width=1000,relief="ridge",fg="#323223",font=("cambria",14,"bold"))
       l1.place(x=0,y=00)

       l2 = tk.Label(self.win,text=" Mushroom Data Data Analysis for Disease Prediction  ",width=50,relief="raised",bg="#220022",fg="cyan",font=("cambria",14,"bold"))
       l2.place(x=30,y=30)
                    
       #self.fn=StringVar()

                   
       
#       self.l2 = tk.Label(self.win,text=" Select Data Set File ",width=20,relief="flat",bg="#912388",fg="white",font=("cambria",14,"bold"))
#       self.l2.place(x=70,y=120)
       
       
       self.b2 = tk.Button(self.win,text=" Select Mushroom Data Set File  ",width=34,bg="darkblue",fg="yellow",relief="raised",font=("cambria",14,"bold"),command=self.callback)
       self.b2.place(x=100,y=120)
       
       
       self.win.mainloop()

   def callback(self):
       self.name=tkinter.filedialog.askopenfilename()
       #name=fd.askopenfilename() 
       print(self.name)
       self.t1 = tk.Label(self.win,text="",width=25,relief="solid",bg="#783327",fg="white",font=("cambria",14,"bold"))
       self.t1.place(x=140,y=190)
       self.t1.configure(text=self.name)
       self.b1 = tk.Button(self.win,text=" Open Data Set  ",width=38,bg="#782323",fg="yellow",relief="raised",font=("cambria",13,"bold"),command=self.loading)
       self.b1.place(x=100,y=250)
              

   def loading(self):
       
       fname=self.name
       print("File Name="+fname)
       if(fname==""):       
           tkinter.messagebox.showinfo(" Mushroom Disease Prediction"," Please Enter File Name....");
       else:
           tkinter.messagebox.showinfo(" Mushroom  Diesease Prediction"," Data set of File="+fname+" is Loading ...Please Wait...");
           self.dataload()
#       self.win.destroy()
 #      app=Test()
 
   def dataload(self):
       tkinter.messagebox.showinfo(" Mushroom Diesease Prediction"," Data Loading Functio is Called...");
       fname=self.name
       data=p.read_csv(fname)
#       print(data);
       data.columns=[col.lower() for col in data];  # Makes all columns To Lower Case
#       print(data[['employee_name','ssn','dept','salary','doj','no_of_project_assigned','completed']]);
       n=data.shape
       print(" Total Record=")
       max=n[0]
       print(max)
       
  #     for i in range(max):
#           print(i)
 #          print("\t Record")
    
       rec=data.iloc[3];
       print(rec)
       print(rec[0])
       
       #[['employee name','gender','age','location']]);
       
       mdb = mysql.connect(host = "localhost",user = "root",passwd = "mj",database="mashroom",use_pure= "True",charset='utf8')
       cursor = mdb.cursor()
       #mdb=mysql.connector.connect(user="root",password="mj",database="crop",host="localhost",charset='utf8')
       #cursor=mdb.cursor()
       cursor.execute("delete from mashroomdataset");
       mdb.commit()
#       sql="insert into emp values('jjj','222','Tester','12000','2015-2-2','40','25')";
 #      cursor.execute(sql);
 #      sql="select * from emp"



       for i in range(max):
           rec=data.iloc[i]
           f1=str(rec[0])
           f2=str(rec[1])
           f3=str(rec[2])
           f4=str(rec[3])
           f5=str(rec[4])
           f6=str(rec[5])
           f7=str(rec[6])
           f8=str(rec[7])
           f9=str(rec[8])
           f10=str(rec[9])
           f11=str(rec[10])
           f12=str(rec[11])
           f13=str(rec[12])
           f14=str(rec[13])
           f15=str(rec[14])
           f16=str(rec[15])
           f17=str(rec[16])
           f18=str(rec[17])
           f19=str(rec[18])
           f20=str(rec[19])
           f21=str(rec[20])

           f22=str(rec[21])
           
       #    print(cshape,csurface,ccolor,brus,odor,gilla,gillspa,gillsize,gcolor,sspace,sroot,ssaring,ssbring,ssacolor,ssbcolor,vtype,vcolor,ringno,ringtype,spcolor,pop,hab);
           print(f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12,f13,f14,f15,f16,f17,f18,f19,f20,f21,f22);
           sql="insert into mashroomdataset values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
           cursor.execute(sql,(f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12,f13,f14,f15,f16,f17,f18,f19,f20,f21,f22));
           mdb.commit()
     
       print(" All Data Transfered And Stored in Data Base....");    
       tkinter.messagebox.showinfo(" Mushroom Disease Prediction"," All Data Transfered And Stored in Data Base....");
       self.win.destroy()
       app=Load();
       
     #  rows=cursor.fetchall()
      # total=cursor.rowcount
      # print("\n Total Data Records=\t"+str(total));


 
 
class Load():
   def __init__(self):
       self.load = tk.Tk()
       self.load.geometry("1200x600+100+100");
#       self.load.configure(bg="#912388")
       self.load.configure(bg="#232342")
       self.load.title(" Mushroom Disease Prediction System ")
     


       mdb = mysql.connect(host = "localhost",user = "root",passwd = "mj",database="mashroom",use_pure= "True",charset='utf8')
       cursor = mdb.cursor()
       
       sql="select * from mashroomdataset"
       cursor.execute(sql);
       rows=cursor.fetchall()
       total=cursor.rowcount
       print("\n Total Data Records=\t"+str(total));

       self.canvas = tk.Canvas(self.load, width = 1200, height = 60,bg="#232342")
       self.canvas.place(x=20,y=100);
       self.canvas.pack();

       l1 = tk.Label(self.canvas,text=" Mushroom Disease Prediction  ",width=50,relief="solid",bg="brown",fg="yellow",font=("cambria",14,"bold"))
       l1.place(x=300,y=20)
       
 
       self.tv=ttk.Treeview(self.load,column=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22),show="headings",height="15")

       self.ysb = ttk.Scrollbar(self.tv, orient=tk.VERTICAL, command=self.tv.yview)
       self.xsb = ttk.Scrollbar(self.tv, orient=tk.HORIZONTAL, command=self.tv.xview)
       ttk.Style().configure("Treeview", background="#a82782",foreground="white", fieldbackground="red",font=('cambria', 10,'bold'))
       self.tv.configure(yscroll=self.ysb.set, xscroll=self.xsb.set)
       self.tv.column('22', minwidth=150, stretch=False)
       self.tv.heading('22', text='Folder')

       self.ysb.pack(anchor=tk.E, fill=tk.Y, side=tk.RIGHT)
       self.xsb.pack(anchor=tk.S, fill=tk.X, side=tk.BOTTOM)
       self.tv.pack(expand=True, fill=tk.BOTH)
    
    
       self.tv.heading("#1",text="Cape Shape")
       self.tv.heading("#2",text="cap-surface")
       self.tv.heading("#3",text="Cap-color")
       self.tv.heading("#4",text="Bruises")
       self.tv.heading("#5",text="Odor")
       self.tv.heading("#6",text="Gill-attachment")
       self.tv.heading("#7",text="Gill-spacing")
       self.tv.heading("#8",text="Gill-size")
       self.tv.heading("#9",text="Gill-color")
       self.tv.heading("#10",text="Stalk-shape")
       self.tv.heading("#11",text="Stalk-root")
       self.tv.heading("#12",text="Stalk-surface-above-ring") 
       self.tv.heading("#13",text="Stalk-surface-below-ring")
       self.tv.heading("#14",text="Stalk-color-above-ring")
       self.tv.heading("#15",text="stalk-color-below-ring")
       self.tv.heading("#16",text="Veil-type")
       self.tv.heading("#17",text="Veil-color")
       self.tv.heading("#18",text="Ring-number")
       self.tv.heading("#19",text="Ring-type")
       self.tv.heading("#20",text="Spore-print-color")
       self.tv.heading("#21",text="Population")
       self.tv.heading("#22",text="Habitat")
                              
       

       for i in rows:
           self.tv.insert('','end',values=i)

       self.canvas1 = tk.Canvas(self.load, width = 1200, height = 60,bg="#232342")  
       self.canvas1.place(x=20,y=500);
       self.canvas1.pack();

       b1 = tk.Button(self.canvas1,text=" Attribute Identification  ",width=25,relief="solid",bg="yellow",fg="blue",font=("cambria",14,"bold"),command=self.dataload1)
       b1.place(x=400,y=14)

       self.load.mainloop()
 
   def dataload1(self):
       tkinter.messagebox.showinfo(" Mushroom Diesease Prediction"," Data Attribute Identification Begins...");

       mdb = mysql.connect(host = "localhost",user = "root",passwd = "mj",database="mashroom",use_pure= "True",charset='utf8')
       cursor = mdb.cursor()

       cursor.execute("delete from mashroomdataset1");

       sql="select * from mashroomdataset"
       cursor.execute(sql);
       rows=cursor.fetchall()

       for rec in rows:
           f1=str(rec[0])
           f2=str(rec[1])
           f3=str(rec[2])
           f4=str(rec[3])
           f5=str(rec[4])
           f6=str(rec[5])
           f7=str(rec[6])
           f8=str(rec[7])
           f9=str(rec[8])
           f10=str(rec[9])
           f11=str(rec[10])
           f12=str(rec[11])
           f13=str(rec[12])
           f14=str(rec[13])
           f15=str(rec[14])
           f16=str(rec[15])
           f17=str(rec[16])
           f18=str(rec[17])
           f19=str(rec[18])
           f20=str(rec[19])
           f21=str(rec[20])
           f22=str(rec[21])
           
           if(str(rec[0])=="b"):
               cshape="Bell"
           elif(str(rec[0])=="c"):
               cshape="Conical"
           elif(str(rec[0])=="x"):
               cshape="Convex"
           elif(str(rec[0])=="f"):
               cshape="Flat"
           elif(str(rec[0])=="k"):
               cshape="Knobbed"
           elif(str(rec[0])=="s"):
               cshape="Sunken"
  
           if(str(rec[1])=="f"):
               csurface="Fibrous"
           elif(str(rec[1])=="g"):
               csurface="Grooves"
           elif(str(rec[1])=="y"):
               csurface="Scale"
           elif(str(rec[1])=="s"):
               csurface="Smooth"
  
           if(str(rec[2])=="n"):
               ccolor="Brown"
           elif(str(rec[2])=="b"):
               ccolor="Buff"
           elif(str(rec[2])=="c"):
               ccolor="Cinnamon"
           elif(str(rec[2])=="g"):
               ccolor="Gray"
           elif(str(rec[2])=="r"):
               ccolor="Green"
           elif(str(rec[2])=="p"):
               ccolor="Pink"
           elif(str(rec[2])=="u"):
               ccolor="Purple"
           elif(str(rec[2])=="e"):
               ccolor="Red"
           elif(str(rec[2])=="w"):
               ccolor="White"
           elif(str(rec[2])=="y"):
               ccolor="Yellow"
    
           if(str(rec[3])=="t"):
               brus="Bruises"
           elif(str(rec[3])=="f"):
               brus="No"
               
           if(str(rec[4])=="a"):
               odor="Almond"
           elif(str(rec[4])=="l"):
               odor="Anise"
           elif(str(rec[4])=="c"):
               odor="Creosote"
           elif(str(rec[4])=="y"):
               odor="Fishy"
           elif(str(rec[4])=="f"):
               odor="Foul"
           elif(str(rec[4])=="m"):
               odor="Musty"
           elif(str(rec[4])=="n"):
               odor="None"
           elif(str(rec[4])=="p"):
               odor="Pungent"
           elif(str(rec[4])=="s"):
               odor="Spicy"

           if(str(rec[5])=="a"):
               gilla="Attached"
           elif(str(rec[5])=="d"):
               gilla="Descending"
           elif(str(rec[5])=="f"):
               gilla="Free"
           elif(str(rec[5])=="n"):
               gilla="Notched"

           if(str(rec[6])=="c"):
               gillspa="Close"
           elif(str(rec[6])=="w"):
               gillspa="Crowed"
           elif(str(rec[6])=="d"):
               gillspa="Distant"

           if(str(rec[7])=="b"):
               gillsize="Broad"
           elif(str(rec[7])=="n"):
               gillsize="Narrow"

           if(str(rec[8])=="n"):
               gcolor="Brown"
           elif(str(rec[8])=="b"):
               gcolor="Buff"
           elif(str(rec[8])=="c"):
               gcolor="Cinnamon"
           elif(str(rec[8])=="g"):
               gcolor="Gray"
           elif(str(rec[8])=="r"):
               gcolor="Green"
           elif(str(rec[8])=="p"):
               gcolor="Pink"
           elif(str(rec[8])=="u"):
               gcolor="Purple"
           elif(str(rec[8])=="e"):
               gcolor="Red"
           elif(str(rec[8])=="w"):
               gcolor="White"
           elif(str(rec[8])=="y"):
               gcolor="Yellow"
           elif(str(rec[8])=="k"):
               gcolor="Black"
           elif(str(rec[8])=="h"):
               gcolor="Chocolate"
           elif(str(rec[8])=="o"):
               gcolor="Orange"

           if(str(rec[9])=="e"):
               sspace="Enlarging"
           elif(str(rec[9])=="t"):
               sspace="Tapering"

           if(str(rec[10])=="b"):
               sroot="Bulbous"
           elif(str(rec[10])=="c"):
               sroot="Cup"
           elif(str(rec[10])=="e"):
               sroot="Equal"
           elif(str(rec[10])=="z"):
               sroot="Rhizomorphs"
           elif(str(rec[10])=="r"):
               sroot="Rooted"
           elif(str(rec[10])=="?"):
               sroot="Missing"

           if(str(rec[11])=="f"):
               ssaring="Fibrous"
           elif(str(rec[11])=="y"):
               ssaring="Scaly"
           elif(str(rec[11])=="k"):
               ssaring="Silky"
           elif(str(rec[11])=="s"):
               ssaring="Smooths"
           elif(str(rec[11])=="b"):
               ssaring="Bubbles"
           elif(str(rec[11])=="p"):
               ssaring="Patches"
 
           if(str(rec[12])=="f"):
               ssbring="Fibrous"
           elif(str(rec[12])=="y"):
               ssbring="Scaly"
           elif(str(rec[12])=="k"):
               ssbring="Silky"
           elif(str(rec[12])=="s"):
               ssbring="Smooths"
           elif(str(rec[12])=="b"):
               ssbring="Bubbles"
           elif(str(rec[12])=="p"):
               ssbring="Patches"
 
           if(str(rec[13])=="n"):
               ssacolor="Brown"
           elif(str(rec[13])=="b"):
               ssacolor="Buff"
           elif(str(rec[13])=="c"):
               ssacolor="Cinnamon"
           elif(str(rec[13])=="g"):
               ssacolor="Gray"
           elif(str(rec[13])=="r"):
               ssacolor="Green"
           elif(str(rec[13])=="p"):
               ssacolor="Pink"
           elif(str(rec[13])=="u"):
               ssacolor="Purple"
           elif(str(rec[13])=="e"):
               ssacolor="Red"
           elif(str(rec[13])=="w"):
               ssacolor="White"
           elif(str(rec[13])=="y"):
               ssacolor="Yellow"
           elif(str(rec[13])=="k"):
               ssacolor="Black"
           elif(str(rec[13])=="h"):
               ssacolor="Chocolate"
           elif(str(rec[13])=="o"):
               ssacolor="Orange"
  
           if(str(rec[14])=="n"):
               ssbcolor="Brown"
           elif(str(rec[14])=="b"):
               ssbcolor="Buff"
           elif(str(rec[14])=="c"):
               ssbcolor="Cinnamon"
           elif(str(rec[14])=="g"):
               ssbcolor="Gray"
           elif(str(rec[14])=="r"):
               ssbcolor="Green"
           elif(str(rec[14])=="p"):
               ssbcolor="Pink"
           elif(str(rec[14])=="u"):
               ssbcolor="Purple"
           elif(str(rec[14])=="e"):
               ssbcolor="Red"
           elif(str(rec[14])=="w"):
               ssbcolor="White"
           elif(str(rec[14])=="y"):
               ssbcolor="Yellow"
           elif(str(rec[14])=="k"):
               ssbcolor="Black"
           elif(str(rec[14])=="h"):
               ssbcolor="Chocolate"
           elif(str(rec[14])=="o"):
               ssbcolor="Orange"

           if(str(rec[15])=="p"):
               vtype="Partial"
           elif(str(rec[15])=="u"):
               vtype="Universal"

           if(str(rec[16])=="n"):
               vcolor="Brown"
           elif(str(rec[16])=="b"):
               vcolor="Buff"
           elif(str(rec[16])=="c"):
               vcolor="Cinnamon"
           elif(str(rec[16])=="g"):
               vcolor="Gray"
           elif(str(rec[16])=="r"):
               vcolor="Green"
           elif(str(rec[16])=="p"):
               vcolor="Pink"
           elif(str(rec[16])=="u"):
               vcolor="Purple"
           elif(str(rec[16])=="e"):
               vcolor="Red"
           elif(str(rec[16])=="w"):
               vcolor="White"
           elif(str(rec[16])=="y"):
               vcolor="Yellow"
           elif(str(rec[16])=="k"):
               vcolor="Black"
           elif(str(rec[16])=="h"):
               vcolor="Chocolate"
           elif(str(rec[16])=="o"):
               vcolor="Orange"
  
           if(str(rec[17])=="n"):
               ringno="None"
           elif(str(rec[17])=="o"):
               ringno="one"
           elif(str(rec[17])=="t"):
               ringno="Two"

           if(str(rec[18])=="c"):
               ringtype="Cobwebby"
           elif(str(rec[18])=="e"):
               ringtype="Ebaneascent"
           elif(str(rec[18])=="f"):
               ringtype="Flaring"
           elif(str(rec[18])=="l"):
               ringtype="Large"
           elif(str(rec[18])=="n"):
               ringtype="None"
           elif(str(rec[18])=="p"):
               ringtype="Pendant"
           elif(str(rec[18])=="s"):
               ringtype="Sheathing"
           elif(str(rec[18])=="z"):
               ringtype="Zone"
    
           if(str(rec[19])=="n"):
               spcolor="Brown"
           elif(str(rec[19])=="b"):
               spcolor="Buff"
           elif(str(rec[19])=="c"):
               spcolor="Cinnamon"
           elif(str(rec[19])=="g"):
               spcolor="Gray"
           elif(str(rec[19])=="r"):
               spcolor="Green"
           elif(str(rec[19])=="p"):
               spcolor="Pink"
           elif(str(rec[19])=="u"):
               spcolor="Purple"
           elif(str(rec[19])=="e"):
               spcolor="Red"
           elif(str(rec[19])=="w"):
               spcolor="White"
           elif(str(rec[19])=="y"):
               spcolor="Yellow"
           elif(str(rec[19])=="k"):
               spcolor="Black"
           elif(str(rec[19])=="h"):
               spcolor="Chocolate"
           elif(str(rec[19])=="o"):
               spcolor="Orange"

           if(str(rec[20])=="a"):
               pop="Abundant"
           elif(str(rec[20])=="c"):
               pop="Clustered"
           elif(str(rec[20])=="n"):
               pop="Numerous"
           elif(str(rec[20])=="s"):
               pop="Scattered"
           elif(str(rec[20])=="v"):
               pop="Several"
           elif(str(rec[20])=="y"):
               pop="Solitary"

           if(str(rec[21])=="u"):
               hab="Urban"
           elif(str(rec[21])=="g"):
               hab="Grasses"
           elif(str(rec[21])=="m"):
               hab="Meadows"
           elif(str(rec[21])=="l"):
               hab="Leaves"
           elif(str(rec[21])=="p"):
               hab="Paths"
           elif(str(rec[21])=="w"):
               hab="Waste"
           elif(str(rec[21])=="d"):
               hab="Woods"

       #    print(cshape,csurface,ccolor,brus,odor,gilla,gillspa,gillsize,gcolor,sspace,sroot,ssaring,ssbring,ssacolor,ssbcolor,vtype,vcolor,ringno,ringtype,spcolor,pop,hab);
           print(f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12,f13,f14,f15,f16,f17,f18,f19,f20,f21,f22);
           sql="insert into mashroomdataset1 values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
           cursor.execute(sql,(cshape,csurface,ccolor,brus,odor,gilla,gillspa,gillsize,gcolor,sspace,sroot,ssaring,ssbring,ssacolor,ssbcolor,vtype,vcolor,ringno,ringtype,spcolor,pop,hab));
           mdb.commit()
     
       print(" All Dataset Values are Converted To Their Attribute Features....");    
       tkinter.messagebox.showinfo(" Mushroom Disease Prediction"," All Dataset Values are Converted To Their Attribute Features....");
       self.load.destroy()
       app=Load1();


class Load1():
   def __init__(self):
       self.load1 = tk.Tk()
       self.load1.geometry("1200x600+100+100");
#       self.load.configure(bg="#912388")
       self.load1.configure(bg="#985676")
       self.load1.title(" Mushroom Disease Prediction System ")
     


       mdb = mysql.connect(host = "localhost",user = "root",passwd = "mj",database="mashroom",use_pure= "True",charset='utf8')
       cursor = mdb.cursor()
       
       sql="select * from mashroomdataset1"
       cursor.execute(sql);
       rows=cursor.fetchall()
       total=cursor.rowcount
       print("\n Total Data Records=\t"+str(total));

       self.canvas = tk.Canvas(self.load1, width = 1200, height = 60,bg="#232342")
       self.canvas.place(x=20,y=100);
       self.canvas.pack();

       l1 = tk.Label(self.canvas,text=" Mushroom Disease Prediction  ",width=50,relief="raised",bg="#625332",fg="yellow",font=("cambria",13,"bold"))
       l1.place(x=300,y=15)
       
 
       self.tv=ttk.Treeview(self.load1,column=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22),show="headings",height="15")

       self.ysb = ttk.Scrollbar(self.tv, orient=tk.VERTICAL, command=self.tv.yview)
       self.xsb = ttk.Scrollbar(self.tv, orient=tk.HORIZONTAL, command=self.tv.xview)
       ttk.Style().configure("Treeview", background="#625332",foreground="yellow", fieldbackground="red",font=('cambria', 10,'bold'))
       self.tv.configure(yscroll=self.ysb.set, xscroll=self.xsb.set)
       self.tv.column('22', minwidth=150, stretch=False)
       self.tv.heading('22', text='Folder')

       self.ysb.pack(anchor=tk.E, fill=tk.Y, side=tk.RIGHT)
       self.xsb.pack(anchor=tk.S, fill=tk.X, side=tk.BOTTOM)
       self.tv.pack(expand=True, fill=tk.BOTH)
    
    
       self.tv.heading("#1",text="Cape Shape")
       self.tv.heading("#2",text="cap-surface")
       self.tv.heading("#3",text="Cap-color")
       self.tv.heading("#4",text="Bruises")
       self.tv.heading("#5",text="Odor")
       self.tv.heading("#6",text="Gill-attachment")
       self.tv.heading("#7",text="Gill-spacing")
       self.tv.heading("#8",text="Gill-size")
       self.tv.heading("#9",text="Gill-color")
       self.tv.heading("#10",text="Stalk-shape")
       self.tv.heading("#11",text="Stalk-root")
       self.tv.heading("#12",text="Stalk-surface-above-ring") 
       self.tv.heading("#13",text="Stalk-surface-below-ring")
       self.tv.heading("#14",text="Stalk-color-above-ring")
       self.tv.heading("#15",text="stalk-color-below-ring")
       self.tv.heading("#16",text="Veil-type")
       self.tv.heading("#17",text="Veil-color")
       self.tv.heading("#18",text="Ring-number")
       self.tv.heading("#19",text="Ring-type")
       self.tv.heading("#20",text="Spore-print-color")
       self.tv.heading("#21",text="Population")
       self.tv.heading("#22",text="Habitat")
                              
       

       for i in rows:
           self.tv.insert('','end',values=i)

       self.canvas1 = tk.Canvas(self.load1, width = 1200, height = 60,bg="#232342")  
       self.canvas1.place(x=20,y=500);
       self.canvas1.pack();


       b2 = tk.Button(self.canvas1,text=" Data Pre-Process  ",width=25,relief="solid",bg="brown",fg="yellow",font=("cambria",13,"bold"),command=self.loading)
       b2.place(x=600,y=12)

       self.load1.mainloop()

   def loading(self):
       self.load1.destroy()
       app=Classification()


class Classification():
   def __init__(self):
       
       self.classify = tk.Tk()
       self.classify.geometry("1000x380+300+100");
       self.classify.title(" Mushroom Disease Prediction System ")
       self.classify.configure(bg="#912388")
                          
       self.canvas = tk.Canvas(self.classify, width = 1000, height = 380)  
       self.canvas.place(x=0,y=0);

       self.img1 = ImageTk.PhotoImage(Image.open("mb2.jpg"))  
       l1 = tk.Label(self.classify, image=self.img1,width=1000,relief="ridge",fg="#323223",font=("cambria",14,"bold"))
       l1.place(x=0,y=00)

       l2 = tk.Label(self.classify,text=" Classification of Mushroom Data On Different Criteria  ",width=50,relief="groove",bg="#092193",fg="yellow",font=("cambria",14,"bold"))
       l2.place(x=30,y=30)

 
       b1 = tk.Button(self.classify,text=" Cap Shape  ",width=30,bg="#c82210",fg="white",relief="groove",font=("cambria",12,"bold"),command=self.cshape)
       b1.place(x=150,y=120)
       
       b2 = tk.Button(self.classify,text=" Cap Surface ",width=30,bg="#c82210",fg="yellow",relief="groove",font=("cambria",12,"bold"),command=self.csurface)
       b2.place(x=150,y=180)

       b3 = tk.Button(self.classify,text=" Cap Color ",width=30,bg="#c82210",fg="yellow",relief="groove",font=("cambria",12,"bold"),command=self.ccolor)
       b3.place(x=150,y=240)

       b4 = tk.Button(self.classify, text=" Prediction of Disease's ",width=30,bg="#c82210",fg="white",relief="groove",font=("cambria",12,"bold"),command=self.exit)
       b4.place(x=150,y=310)
       

       self.classify.mainloop()

   def cshape(self):
       tkinter.messagebox.showinfo(" Mushroom Disease Prediction"," Classfication of Data Based On Cap Shape...")
       self.classify.destroy()
       app=Cshape()
       
   def csurface(self):
       tkinter.messagebox.showinfo(" Mushroom Disease Prediction"," Classficaation of Data Based On Rain Fall...")
       self.classify.destroy()
       app=Csurface()

   def ccolor(self):
       tkinter.messagebox.showinfo(" Mushroom Disease Prediction"," Classficaation of Data Based On Location...")
       self.classify.destroy()
       app=Ccolor()

   def exit(self):
       self.classify.destroy()
       app=Analysis()








class Cshape():
   def __init__(self):
       self.dept = tk.Tk()
       self.dept.geometry("1000x600+100+100");
       self.dept.configure(bg="#912388")
       self.dept.configure(bg="#783478")
       self.dept.title(" Mushroom Disease Prediction System ")
     
       self.canvas = tk.Canvas(self.dept, width = 1000, height = 600)  
       self.canvas.place(x=0,y=0);

       self.img1 = ImageTk.PhotoImage(Image.open("mb1.jpg"))  
       l1 = tk.Label(self.dept, image=self.img1,width=1000,relief="ridge",fg="#323223",font=("cambria",14,"bold"))
       l1.place(x=0,y=00)

       l2 = tk.Label(self.dept,text=" Classification of Data Based On Cap Shape   ",width=50,relief="solid",bg="#452343",fg="yellow",font=("cambria",14,"bold"))
       l2.place(x=100,y=25)


       mdb = mysql.connect(host = "localhost",user = "root",passwd = "mj",database="mashroom",use_pure= "True",charset='utf8')
       cursor = mdb.cursor()

       sql="select cshape,count(*) from mashroomdataset1 group by cshape"
       cursor.execute(sql);
       rows=cursor.fetchall()
       total=cursor.rowcount
       print("\n Total Data Records=\t"+str(total));

       print(" All Main Data Is Extracted from Overall Data....");    
       tkinter.messagebox.showinfo(" Mushroom Data Analysis "," Data Classified Based On Cap Shape ... As Result....");
       
#       style1 = ttk.Style()
#       style1.configure("mystyle1.Treeview", highlightthickness=2, bd=1, font=('times new roman', 10),bg="#383838",fg="white") # Modify the font of the body
##       style1.configure("mystyle1.Treeview.Heading", font=('cambria', 10,'bold'),bg="red",fg="red", fieldbackground="red") # Modify the font of the headings
  #     style1.layout("mystyle1.Treeview", [('mystyle1.Treeview.treearea', {'sticky': 'nswe'})]) # Remove the borders

       self.tv1=ttk.Treeview(self.dept,style="mystyle1.Treeview",column=(1,2),show="headings",height="5")
       ttk.Style().configure("Treeview", background="#c83838",foreground="white", fieldbackground="red",font=('cambria', 10,'bold'))
       
#       ysb = ttk.Scrollbar(self.load, orient='vertical', command=self.tv.yview)
#       self.tv.grid(row=10, column=10, sticky='nsew')
 #      ysb.grid(row=10, column=10, sticky='ns')
  #     self.tv.configure(yscroll=ysb.set) 
    
       self.tv1.heading(1,text="Cap Shape")
       self.tv1.heading(2,text="NO OF SAMPLE TAKEN")
 
       for i in rows:
           self.tv1.insert('','end',values=i)

       self.tv1.place(x=140,y=100);
       b1 = tk.Button(self.dept,text=" Back ",width=20,relief="solid",font=("cambria",12,"bold"),command=self.back)
       b1.place(x=250,y=300)

       self.dept.mainloop()

   def back(self):
       self.dept.destroy()
       app=Classification()


class Ccolor():
   def __init__(self):
       self.dept = tk.Tk()
       self.dept.geometry("1000x600+100+100");
       self.dept.configure(bg="#912388")
       self.dept.configure(bg="#783478")
       self.dept.title(" Mushroom Disease Prediction System ")
     
       self.canvas = tk.Canvas(self.dept, width = 1000, height = 600)  
       self.canvas.place(x=0,y=0);

       self.img1 = ImageTk.PhotoImage(Image.open("mb1.jpg"))  
       l1 = tk.Label(self.dept, image=self.img1,width=1000,relief="ridge",fg="#323223",font=("cambria",14,"bold"))
       l1.place(x=0,y=00)

       l2 = tk.Label(self.dept,text=" Classification of Data Based On Cap Shape   ",width=50,relief="solid",bg="#452343",fg="yellow",font=("cambria",14,"bold"))
       l2.place(x=100,y=25)


       mdb = mysql.connect(host = "localhost",user = "root",passwd = "mj",database="mashroom",use_pure= "True",charset='utf8')
       cursor = mdb.cursor()

       sql="select ccolor,count(*) from mashroomdataset1 group by ccolor"
       cursor.execute(sql);
       rows=cursor.fetchall()
       total=cursor.rowcount
       print("\n Total Data Records=\t"+str(total));

       print(" All Main Data Is Extracted from Overall Data....");    
       tkinter.messagebox.showinfo(" Mushroom Data Analysis "," Data Classified Based On Cap Shape ... As Result....");
       
#       style1 = ttk.Style()
#       style1.configure("mystyle1.Treeview", highlightthickness=2, bd=1, font=('times new roman', 10),bg="#383838",fg="white") # Modify the font of the body
##       style1.configure("mystyle1.Treeview.Heading", font=('cambria', 10,'bold'),bg="red",fg="red", fieldbackground="red") # Modify the font of the headings
  #     style1.layout("mystyle1.Treeview", [('mystyle1.Treeview.treearea', {'sticky': 'nswe'})]) # Remove the borders

       self.tv1=ttk.Treeview(self.dept,style="mystyle1.Treeview",column=(1,2),show="headings",height="5")
       ttk.Style().configure("Treeview", background="#c83838",foreground="white", fieldbackground="red",font=('cambria', 10,'bold'))
       
#       ysb = ttk.Scrollbar(self.load, orient='vertical', command=self.tv.yview)
#       self.tv.grid(row=10, column=10, sticky='nsew')
 #      ysb.grid(row=10, column=10, sticky='ns')
  #     self.tv.configure(yscroll=ysb.set) 
    
       self.tv1.heading(1,text="Cap Color")
       self.tv1.heading(2,text="NO OF SAMPLE TAKEN")
 
       for i in rows:
           self.tv1.insert('','end',values=i)

       self.tv1.place(x=140,y=100);
       b1 = tk.Button(self.dept,text=" Back ",width=20,relief="solid",font=("cambria",12,"bold"),command=self.back)
       b1.place(x=250,y=300)

       self.dept.mainloop()

   def back(self):
       self.dept.destroy()
       app=Classification()


class Csurface():
   def __init__(self):
       self.dept = tk.Tk()
       self.dept.geometry("1000x600+100+100");
       self.dept.configure(bg="#912388")
       self.dept.configure(bg="#783478")
       self.dept.title(" Mushroom Disease Prediction System ")
     
       self.canvas = tk.Canvas(self.dept, width = 1000, height = 600)  
       self.canvas.place(x=0,y=0);

       self.img1 = ImageTk.PhotoImage(Image.open("mb1.jpg"))  
       l1 = tk.Label(self.dept, image=self.img1,width=1000,relief="ridge",fg="#323223",font=("cambria",14,"bold"))
       l1.place(x=0,y=00)

       l2 = tk.Label(self.dept,text=" Classification of Data Based On Cap Surface   ",width=50,relief="solid",bg="#452343",fg="yellow",font=("cambria",14,"bold"))
       l2.place(x=100,y=25)


       mdb = mysql.connect(host = "localhost",user = "root",passwd = "mj",database="mashroom",use_pure= "True",charset='utf8')
       cursor = mdb.cursor()

       sql="select csurface,count(*) from mashroomdataset1 group by csurface"
       cursor.execute(sql);
       rows=cursor.fetchall()
       total=cursor.rowcount
       print("\n Total Data Records=\t"+str(total));

       print(" All Main Data Is Extracted from Overall Data....");    
       tkinter.messagebox.showinfo(" Mushroom Data Analysis "," Data Classified Based On Cap Surface ... As Result....");
       
#       style1 = ttk.Style()
#       style1.configure("mystyle1.Treeview", highlightthickness=2, bd=1, font=('times new roman', 10),bg="#383838",fg="white") # Modify the font of the body
##       style1.configure("mystyle1.Treeview.Heading", font=('cambria', 10,'bold'),bg="red",fg="red", fieldbackground="red") # Modify the font of the headings
  #     style1.layout("mystyle1.Treeview", [('mystyle1.Treeview.treearea', {'sticky': 'nswe'})]) # Remove the borders

       self.tv1=ttk.Treeview(self.dept,style="mystyle1.Treeview",column=(1,2),show="headings",height="5")
       ttk.Style().configure("Treeview", background="#c83838",foreground="white", fieldbackground="red",font=('cambria', 10,'bold'))
       
#       ysb = ttk.Scrollbar(self.load, orient='vertical', command=self.tv.yview)
#       self.tv.grid(row=10, column=10, sticky='nsew')
 #      ysb.grid(row=10, column=10, sticky='ns')
  #     self.tv.configure(yscroll=ysb.set) 
    
       self.tv1.heading(1,text="Cap Surface")
       self.tv1.heading(2,text="NO OF SAMPLE TAKEN")
 
       for i in rows:
           self.tv1.insert('','end',values=i)

       self.tv1.place(x=140,y=100);
       b1 = tk.Button(self.dept,text=" Back ",width=20,relief="solid",font=("cambria",12,"bold"),command=self.back)
       b1.place(x=250,y=300)

       self.dept.mainloop()

   def back(self):
       self.dept.destroy()
       app=Classification()


class Analysis():
   def __init__(self):

       self.ana = tk.Tk()
       self.ana.geometry("1000x380+300+100");
       self.ana.title(" Mushroom Disease Prediction System ")
       self.ana.configure(bg="#912388")
                          
       self.canvas = tk.Canvas(self.ana, width = 1000, height = 380)  
       self.canvas.place(x=0,y=0);

       self.img1 = ImageTk.PhotoImage(Image.open("mb2.jpg"))  
       l1 = tk.Label(self.ana, image=self.img1,width=1000,relief="ridge",fg="#323223",font=("cambria",14,"bold"))
       l1.place(x=0,y=00)

       l2 = tk.Label(self.ana,text=" Mushroom Disease Data Analysis System For Growth Prediction  ",width=50,relief="groove",bg="#092193",fg="yellow",font=("cambria",14,"bold"))
       l2.place(x=30,y=30)

       
       b1 = tk.Button(self.ana,text=" Extract Featured Attribute  ",width=30,bg="#c82210",fg="white",relief="groove",font=("cambria",12,"bold"),command=self.featureextraction)
       b1.place(x=150,y=120)
       
#       b2 = tk.Button(self.ana,text=" Classification ",width=25,bg="#782323",fg="yellow",relief="raised",font=("cambria",12,"bold"),command=self.classify)
#       b2.place(x=220,y=180)

#       b3 = tk.Button(self.ana,text=" Prediction Of Crop ",width=30,bg="#c82210",fg="yellow",relief="groove",font=("cambria",12,"bold"),command=self.prediction)
 #      b3.place(x=150,y=180)

       b4 = tk.Button(self.ana, text=" Exit ",width=30,bg="#c82210",fg="white",relief="groove",font=("cambria",12,"bold"),command=self.exit)
       b4.place(x=150,y=240)

       self.ana.mainloop()

   def featureextraction(self):
       tkinter.messagebox.showinfo(" Mushroom Disease Prediction"," Extraction of Required Data from Oveall Data Set Information...")
       self.ana.destroy()
       app=Feature()
       
 #  def classify(self):
#       tkinter.messagebox.showinfo(" Employee Payroll"," Extraction of Required Data from Oveall Data Set Information...")
   #    self.ana.destroy()
  #     app=Classification()

   def prediction(self):
#       tkinter.messagebox.showinfo(" Employee Payroll"," Extraction of Required Data from Oveall Data Set Information...")
       self.ana.destroy()
       app=Prediction()

   def exit(self):
       self.ana.destroy()



class Feature():
   def __init__(self):
       self.feature = tk.Tk()                   
       self.feature.geometry("1200x600+100+100");
       self.feature.configure(bg="#912388")
       self.feature.configure(bg="#232342")
       self.feature.title(" Mushroom Disease Prediction System ")
     
       l1 = tk.Label(self.feature,text=" Extracted Neccessary Data From Mushroom Dataset   ",width=50,relief="raised",bg="#452343",fg="yellow",font=("cambria",14,"bold"))
       l1.place(x=300,y=50)


       mdb = mysql.connect(host = "localhost",user = "root",passwd = "mj",database="mashroom",use_pure= "True",charset='utf8')
       cursor = mdb.cursor()

       cursor.execute("delete from mashroomfeature");
        
       sql="select * from mashroomdataset1"
       cursor.execute(sql);
       rows=cursor.fetchall()
       total=cursor.rowcount
       print("\n Total Data Records=\t"+str(total));
  
       for row in rows:
           cshape=str(row[0])
           csurface=str(row[1])
           capcolor=str(row[2])
           brus=str(row[3])
           scar=str(row[11])
           scbr=str(row[12])
           vc=str(row[16])
           
           sql="insert into mashroomfeature values(%s,%s,%s,%s,%s,%s,%s)"
           cursor.execute(sql,(cshape,csurface,capcolor,brus,scar,scbr,vc));
           mdb.commit()
     
       print(" All Main Data Is Extracted from Overall Data....");    
       tkinter.messagebox.showinfo(" Mushroom Data Analysis "," All Main Data Is Extracted from Overall Data....");

 
       self.canvas = tk.Canvas(self.feature, width = 1200, height = 60,bg="#232342")
       self.canvas.place(x=20,y=100);
       self.canvas.pack();

       l1 = tk.Label(self.canvas,text=" Mushroom Disease Prediction  ",width=50,relief="solid",bg="brown",fg="yellow",font=("cambria",14,"bold"))
       l1.place(x=300,y=20)
       
 
       self.tv=ttk.Treeview(self.feature,column=(1,2,3,4,5,6,7),show="headings",height="15")

       self.ysb = ttk.Scrollbar(self.tv, orient=tk.VERTICAL, command=self.tv.yview)
       self.xsb = ttk.Scrollbar(self.tv, orient=tk.HORIZONTAL, command=self.tv.xview)
       ttk.Style().configure("Treeview", background="#a82782",foreground="white", fieldbackground="red",font=('cambria', 10,'bold'))
       self.tv.configure(yscroll=self.ysb.set, xscroll=self.xsb.set)
       self.tv.column('7', minwidth=150, stretch=False)
       self.tv.heading('7', text='Folder')

       self.ysb.pack(anchor=tk.E, fill=tk.Y, side=tk.RIGHT)
       self.xsb.pack(anchor=tk.S, fill=tk.X, side=tk.BOTTOM)
       self.tv.pack(expand=True, fill=tk.BOTH)
 
       sql="select * from mashroomfeature"
       cursor.execute(sql);
       rows=cursor.fetchall()
       
       self.tv.heading("#1",text="Cape Shape")
       self.tv.heading("#2",text="cap-surface")
       self.tv.heading("#3",text="Cap-color")
       self.tv.heading("#4",text="Bruises")
       self.tv.heading("#5",text="Stalk Surface Above Ring")
       self.tv.heading("#6",text="Stalk Surface Below Ring")
       self.tv.heading("#7",text="Viel Color")
      
       for i in rows:
           self.tv.insert('','end',values=i)

       self.canvas1 = tk.Canvas(self.feature, width = 1200, height = 60,bg="#232342")
       self.canvas1.place(x=20,y=100);
       self.canvas1.pack();

       b1 = tk.Button(self.canvas1,text=" Disease Prediction Begin.... ",width=30,bg="yellow",fg="red",relief="raised",font=("cambria",14,"bold"),command=self.back)
       b1.place(x=450,y=14)

       self.feature.mainloop()

   def back(self):
       self.feature.destroy()
      # app=Classification()
#       self.feature.destroy()
       app=Prediction()


class Prediction():
   def __init__(self):
       self.prediction = tk.Tk()
       self.prediction.geometry("700x400+250+100");
       self.prediction.title(" Mushroom Disease Prediction System ")
       self.prediction.configure(bg="#232342")

       self.canvas = tk.Canvas(self.prediction, width = 1000, height = 380)  
       self.canvas.place(x=0,y=0);

       self.img1 = ImageTk.PhotoImage(Image.open("mb2.jpg"))  
       l1 = tk.Label(self.prediction, image=self.img1,width=1000,relief="ridge",fg="#323223",font=("cambria",14,"bold"))
       l1.place(x=0,y=00)

       l2 = tk.Label(self.prediction,text=" Prediction of Disease   ",width=50,relief="groove",bg="#092193",fg="yellow",font=("cambria",14,"bold"))
       l2.place(x=30,y=30)

       
       b1 = tk.Button(self.prediction,text=" Disease Prediction ",width=35,bg="#782323",fg="yellow",relief="raised",font=("cambria",12,"bold"),command=self.croppred)
       b1.place(x=150,y=120)
       

#       b4 = tk.Button(self.prediction, text=" Exit ",width=35,bg="#782323",fg="yellow",relief="raised",font=("cambria",12,"bold"),command=self.exit)
 #      b4.place(x=150,y=200)

       self.prediction.mainloop()

   def croppred(self):
       tkinter.messagebox.showinfo(" Mushroom Disease Prediction"," Disease Prediction Begins...")
       tkinter.messagebox.showinfo(" Mushroom Disease Prediction "," Prediction of Mushroom Disease ...")

       now = datetime.now()
       print ("Current date and time : ")
       print(now)
       
       l_date=now.date();
       print("Date=",l_date)
       
       mdb = mysql.connect(host = "localhost",user = "root",passwd = "mj",database="mashroom",use_pure= "True",charset='utf8')
       cursor = mdb.cursor()
       
       cursor.execute("delete from mashroomdisease");
       sql="select * from mashroomdataset1"
       cursor.execute(sql);
       rows=cursor.fetchall()
       total=cursor.rowcount
       print("\n Total Data Records=\t"+str(total));
  
       for row in rows:
           cshape=str(row[0])
           csurface=str(row[1])
           capcolor=str(row[2])
           brus=str(row[3])
           scac=str(row[13])
           scbc=str(row[14])
           vc=str(row[16])
           
           capcolor=capcolor.lower()
           scac=scac.lower()
           scbc=scbc.lower()
           vc=vc.lower()
#           sql="insert into mashroomfeature values(%s,%s,%s,%s,%s,%s,%s)"
 #          cursor.execute(sql,(cshape,csurface,capcolor,brus,scar,scbr,vc));
  #         mdb.commit()
           if(capcolor=="Brown" or capcolor=="yellow"):
               disease="Mites"
               iname="mites.jpg"
           elif(scac=="Brown" or scac=="yellow"):
               disease="Mushroom Flies"
               iname="Flies.jpg"
           elif(scbc=="gray" or capcolor=="buff"):
               disease="Mummy Disease"
               iname="Mummy.jpg"
           elif(vc=="black" or vc=="yellow"):
               disease=" Hama Oyster Mushroom Disease"
               iname="Hama.jpg"
           elif(scac=="black"  or capcolor=="Black"):
               disease=" Wet Buuble Disease"
               iname="wet.jpg"
           else:
               disease=" No Disease "
               iname="BIG.jpg"
                   
           print("Disease=",disease);

           cshape=cshape.upper();
           csurface=csurface.upper()
           capcolor=capcolor.upper()
           scac=scac.upper()
           scbc=scbc.upper()
           vc=vc.upper()
           sql="insert into mashroomdisease values(%s,%s,%s,%s,%s,%s,%s,%s)"
           cursor.execute(sql,(cshape,csurface,capcolor,scac,scbc,vc,disease,iname));
           mdb.commit()
  #         print("\n Increment=",incr, "\n Total sal=",paysal);             
   #        per=round(per,2);
         #  sql="insert into croppre values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
         #  cursor.execute(sql,(city,loc,oname,gen,stype,rainfall,temp,hum,vel,ph,land,ctype));
         #  mdb.commit()
         #  sql="insert into croppre1 values(%s,%s,%s,%s,%s,%s,%s,%s)"
         #  cursor.execute(sql,(stype,rainfall,temp,hum,vel,ph,land,ctype));
         #  mdb.commit()
     
       print(" All Main Data Is Extracted from Overall Data....");    
       tkinter.messagebox.showinfo(" Mushroom Disease Prediction "," Mushroom Disease Prediction Process is Completed ....");
       self.prediction.destroy()
       app=Diseasepre()
       
   def exit(self):
       self.prediction.destroy()
       app=Analysis()

class Diseasepre():
   def __init__(self):
       self.pay = tk.Tk()
       self.pay.geometry("1200x600+100+100");
       self.pay.configure(bg="#912388")
       self.pay.configure(bg="#232342")
       self.pay.title(" Mushroom Disease Prediction System ")
     
       self.canvas = tk.Canvas(self.pay, width = 1200, height = 60,bg="#232342")
       self.canvas.place(x=20,y=100);
       self.canvas.pack();

       l1 = tk.Label(self.canvas,text=" Mushroom Disease's Predicted Details...  ",width=50,relief="solid",bg="brown",fg="yellow",font=("cambria",14,"bold"))
       l1.place(x=300,y=20)
       
#       l1 = tk.Label(self.pay,text=" Crop Yield Prediction Details  ",width=50,relief="solid",fg="#323223",font=("cambria",14,"bold"))
#       l1.place(x=300,y=50)


       mdb = mysql.connect(host = "localhost",user = "root",passwd = "mj",database="mashroom",use_pure= "True",charset='utf8')
       cursor = mdb.cursor()

       sql="select * from mashroomdisease"
       cursor.execute(sql);
       rows=cursor.fetchall()
       total=cursor.rowcount
       print("\n Total Data Records=\t"+str(total));
       
       self.tv=ttk.Treeview(self.pay,column=(1,2,3,4,5,6,7),show="headings",height="15")
       self.ysb = ttk.Scrollbar(self.tv, orient=tk.VERTICAL, command=self.tv.yview)
       self.xsb = ttk.Scrollbar(self.tv, orient=tk.HORIZONTAL, command=self.tv.xview)
       ttk.Style().configure("Treeview", background="#383838",foreground="white", fieldbackground="red",font=('cambria', 10,'bold'))
       self.tv.configure(yscroll=self.ysb.set, xscroll=self.xsb.set)
       self.tv.column('7', minwidth=150, stretch=False)
       self.tv.heading('7', text='Folder')

       self.ysb.pack(anchor=tk.E, fill=tk.Y, side=tk.RIGHT)
       self.xsb.pack(anchor=tk.S, fill=tk.X, side=tk.BOTTOM)
       self.tv.pack(expand=True, fill=tk.BOTH)

       self.tv.heading("#1",text="Cape Shape")
       self.tv.heading("#2",text="cap-surface")
       self.tv.heading("#3",text="Cap-color")
       self.tv.heading("#4",text="Stalk-color-above-ring")
       self.tv.heading("#5",text="stalk-color-below-ring")
       self.tv.heading("#6",text="Veil-color")
       self.tv.heading("#7",text="Disease")
       
       for i in rows:
           self.tv.insert('','end',values=i)

       self.canvas1 = tk.Canvas(self.pay, width = 1200, height = 60,bg="#232342")  
       self.canvas1.place(x=20,y=500);
       self.canvas1.pack();

#       b1 = tk.Button(self.canvas1,text=" Pre-Process ",width=20,relief="solid",bg="brown",fg="yellow",font=("cambria",14,"bold"),command=self.loading)
 #      b1.place(x=450,y=20)
 
       b2 = tk.Button(self.canvas1, text=" Graph ",width=35,bg="yellow",fg="red",relief="raised",font=("cambria",12,"bold"),command=self.graph)
       b2.place(x=600,y=20)

       b1 = tk.Button(self.canvas1,text=" Back ",width=20,relief="solid",font=("cambria",12,"bold"),command=self.loading)
       b1.place(x=150,y=20)

       self.pay.mainloop()

   def loading(self):
       self.pay.destroy()
       app=Analysis()

   def graph(self):
       self.pay.destroy()
       app=Graph()
      

class Graph():
   def __init__(self):
       graph= tk.Tk() 
       graph.configure(bg="#912388")
       graph.geometry("1600x1400+10+10")               
       graph.title(" Graphical Representation of Mushroom Disease Predicted Details....");                      

       mdb = mysql.connect(host = "localhost",user = "root",passwd = "mj",database="mashroom",use_pure= "True",charset='utf8')
       cursor = mdb.cursor()

       sql="select disease,count(*) from mashroomdisease group by disease"
       cursor.execute(sql);
       rows=cursor.fetchall()
       total=cursor.rowcount
#cnt=0
       df = p.DataFrame( [[ij for ij in i] for i in rows] )
       df.rename(columns={0: 'disease',1: 'cnt'}, inplace=True);

       print("\n Data Vaalues\n")
#print(df)
       disease=df['disease']
       disease=disease.values
       print(disease)

       for i in range(0, len(disease)): 
           disease[i] = str(disease[i])

       print("\n------------------\n")
       print(disease)
       print("\n------------------\n")


       cnt=df['cnt']
       cnt=cnt.values
#exp1=exp.tolist()
       print(cnt)
       
       for i in range(0, len(cnt)): 
           cnt[i] = int(cnt[i])
    
       print("\n------------------\n")
       print(cnt)
       print("\n------------------\n")

               #data=p.read_csv("E:\\empdataset1.txt")

       xx1=cnt
       print(xx1)

#yy=data['SSN']
#yy1=yy.values

       yy1=disease
       print(yy1)

       data2 = {'cnt': xx1,
                'Disease': yy1
                }
 
       figure3 = plt.Figure(figsize=(5,1), dpi=100)
       ax1 = figure3.add_subplot(222)
       bar1 = FigureCanvasTkAgg(figure3, graph)
       bar1.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH,expand=True)
   
       df2 = DataFrame(data2,columns=['cnt','Disease'])
       df2 = df2[['cnt','Disease']].groupby('Disease').sum()
       df2.plot(kind='barh', legend=True, ax=ax1,color="orange",fontsize=15)

       ax1.spines['bottom'].set_color('red')
       ax1.spines['top'].set_color('red')
       ax1.spines['left'].set_color('red')
       ax1.spines['right'].set_color('red')
       ax1.xaxis.label.set_color('red')
       ax1.yaxis.label.set_color('red')

       ax1.set_facecolor("#302010")
#ax1.set_axis_bgcolor("#908576")
       ax1.legend([' Disease Type']) 
       ax1.set_title(' Mushroom Disease ',fontsize=18, fontweight='bold')
       ax1.set_ylabel(' Disease ',fontsize=16, fontweight='bold')
       ax1.set_xlabel(' Total  Count ',fontsize=16, fontweight='bold')




#       Graph1();

       graph.mainloop()

         
class Graph1():
   def __init__(self):
       graph1= tk.Tk() 
       graph1.configure(bg="#912388")
       graph1.geometry("1200x1400+10+10")               
       graph1.title(" Graphical Representation of Data Analysis");                      

       mdb = mysql.connect(host = "localhost",user = "root",passwd = "mj",database="crop",use_pure= "True",charset='utf8')
       cursor = mdb.cursor()

       cursor.execute("delete from cropgraph");

       sql="select soil_type,ctype,count(*) from croppre  where ctype  not like 'No%' group by ctype";
       cursor.execute(sql);
       rows=cursor.fetchall()

       for row in rows:
           stype=str(row[0])
           ctype=str(row[1])
           cnt=str(row[2])
           sc=stype+"-"+ctype;
           sql="insert into cropgraph values(%s,%s)"
           cursor.execute(sql,(sc,cnt));
           mdb.commit()
           
       sql="select * from cropgraph";
       cursor.execute(sql);
       rows=cursor.fetchall()
       
       df = p.DataFrame( [[ij for ij in i] for i in rows] )
       df.rename(columns={0: 'stype',1: 'cnt'}, inplace=True);

       print("\n Data Vaalues\n")
#print(df)
       stype=df['stype']
       stype=stype.values
       print(stype)

       for i in range(0, len(stype)): 
           stype[i] = str(stype[i])

       print("\n------------------\n")
       print(stype)
       print("\n------------------\n")

       cnt=df['cnt']
       cnt=cnt.values
#exp1=exp.tolist()
       print(cnt)
       
       for i in range(0, len(cnt)): 
           cnt[i] = int(cnt[i])
    
       print("\n------------------\n")
       print(cnt)
       print("\n------------------\n")

               #data=p.read_csv("E:\\empdataset1.txt")

       xx1=cnt
       print(xx1)

#yy=data['SSN']
#yy1=yy.values

       yy1=stype
       print(yy1)

       data2 = {'cnt': xx1,
                'stype': yy1
                }
 
       figure3 = plt.Figure(figsize=(10,10), dpi=120)
       ax1 = figure3.add_subplot(222)
       bar1 = FigureCanvasTkAgg(figure3, graph1)
       bar1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH,expand=True)
   
       df2 = DataFrame(data2,columns=['cnt','stype'])
       df2 = df2[['cnt','stype']].groupby('stype').sum()
       df2.plot(kind='barh', legend=True, ax=ax1,color="yellow",fontsize=12)

       ax1.spines['bottom'].set_color('red')
       ax1.spines['top'].set_color('red')
       ax1.spines['left'].set_color('red')
       ax1.spines['right'].set_color('red')
       ax1.xaxis.label.set_color('red')
       ax1.yaxis.label.set_color('red')

       ax1.set_facecolor("#437867")
#ax1.set_axis_bgcolor("#908576")
       ax1.legend([' Total Sample Taken']) 
       ax1.set_title(' Soil Type Vs Total Sample',fontsize=18, fontweight='bold')
       ax1.set_xlabel(' Total Sample Count ',fontsize=16, fontweight='bold')
       ax1.set_ylabel(' Soil Type ',fontsize=16, fontweight='bold')

       Graph2(); 

       graph1.mainloop()


class Graph2():
   def __init__(self):
       graph2= tk.Tk() 
       graph2.configure(bg="#912388")
       graph2.geometry("1200x1400+10+10")               
       graph2.title(" Graphical Representation of Data Analysis");                      

       mdb = mysql.connect(host = "localhost",user = "root",passwd = "mj",database="crop",use_pure= "True",charset='utf8')
       cursor = mdb.cursor()

       sql="select crop,avg(cost) from cost group by crop"
       cursor.execute(sql);
       rows=cursor.fetchall()
       total=cursor.rowcount
#cnt=0
       df = p.DataFrame( [[ij for ij in i] for i in rows] )
       df.rename(columns={0: 'crop',1: 'cost'}, inplace=True);

       print("\n Data Vaalues\n")
#print(df)
       crop=df['crop']
       crop=crop.values
       print(crop)

       for i in range(0, len(crop)): 
           crop[i] = str(crop[i])

       print("\n------------------\n")
       print(crop)
       print("\n------------------\n")


       cost=df['cost']
       cost=cost.values
#exp1=exp.tolist()
       print(cost)
       
       for i in range(0, len(cost)): 
           cost[i] = float(cost[i])
    
       print("\n------------------\n")
       print(cost)
       print("\n------------------\n")

               #data=p.read_csv("E:\\empdataset1.txt")

       xx1=cost
       print(xx1)

#yy=data['SSN']
#yy1=yy.values

       yy1=crop
       print(yy1)

       data2 = {'cost': xx1,
                'crop': yy1
                }
 
       figure3 = plt.Figure(figsize=(8,5), dpi=100)
       ax1 = figure3.add_subplot(222)
       bar1 = FigureCanvasTkAgg(figure3, graph2)
       bar1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH,expand=True)
   
       df2 = DataFrame(data2,columns=['cost','crop'])
       df2 = df2[['cost','crop']].groupby('crop').sum()
       df2.plot(kind='bar', legend=True, ax=ax1,color="cyan",fontsize=12)

       ax1.spines['bottom'].set_color('red')
       ax1.spines['top'].set_color('red')
       ax1.spines['left'].set_color('red')
       ax1.spines['right'].set_color('red')
       ax1.xaxis.label.set_color('red')
       ax1.yaxis.label.set_color('red')

       ax1.set_facecolor("#674277")
#ax1.set_axis_bgcolor("#908576")
       ax1.legend([' Avg Cost of Crops in Market']) 
       ax1.set_title(' Avg Cost Vs Crops',fontsize=12, fontweight='bold')
       ax1.set_xlabel(' Crops ',fontsize=12, fontweight='bold')
       ax1.set_ylabel(' Avg Cost of Crops ',fontsize=12, fontweight='bold')

       graph2.mainloop()


class Test():
   def __init__(self):
       self.root = tk.Tk()
       self.root.geometry("1000x600+300+100");
       self.root.title(" Mushroom Disease Prediction System ")
       self.root.configure(bg="#912388")
       self.canvas = tk.Canvas(self.root, width = 1000, height = 600)  
       self.canvas.place(x=0,y=0);


       self.img1 = ImageTk.PhotoImage(Image.open("mb2.jpg"))  
       l1 = tk.Label(self.root, image=self.img1,width=1000,relief="ridge",fg="#323223",font=("cambria",14,"bold"))
       l1.place(x=0,y=00)

       l2 = tk.Label(self.root,text=" Mashroom Data Analysis for Disease Prediction  ",width=52,relief="raised",bg="#220022",fg="cyan",font=("cambria",14,"bold"))
       l2.place(x=30,y=30)

       self.img2 = ImageTk.PhotoImage(Image.open("mb5.jpg"))  
       self.canvas.create_image(0, 0, image=self.img2) 
       l11 = tk.Label(self.root, image=self.img2,width=320,height=285,relief="raised",fg="#323223",font=("cambria",14,"bold"))
       l11.place(x=00,y=100)

       b1 = tk.Button(self.root,text=" Begin Process.........",width=30,bg="#220022",fg="cyan",relief="raised",font=("cambria",14,"bold"),command=self.createNewWindow)
       b1.place(x=600,y=480)
       
       #b2 = tk.Button(self.root, text=" Exit ",width=25,bg="#782323",fg="yellow",relief="raised",font=("cambria",12,"bold"),command=self.exit)
      # b2.place(x=50,y=200)

       self.root.mainloop()

   def createNewWindow(self):
       self.root.destroy()
       app=NewWin()
       

   def exit(self):
       self.root.destroy()

#app=Classification()        

app=Test()
#app=Graph()
    #app=Analysis()