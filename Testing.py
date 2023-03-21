from tkinter import *
from tkinter import messagebox
import  mysql.connector 

mycon=mysql.connector.connect(host='localhost',user='root',password='abcd',database='parking')
if mycon.is_connected():
         print("Success")
mycur=mycon.cursor()





window = Tk()
window.title('ParkXpert')
window.configure(bg = "light blue")
window.geometry('800x700')
username=0
password=0
#Signup form for new user
def register():
   window1 = Tk()
   window1.title('ParkXpert')
   window1.configure(bg = "light blue")
   window1.geometry('500x600')

   def ex():
     window1.destroy()

   def confirm():
    
    window1.destroy()
    
   #username label and text entry box
   usernameLabel = Label(window1, text="User Name").grid(row=15, column=0)
   username = StringVar()
   usernameEntry = Entry(window1, textvariable=username).grid(row=15, column=1)
   
   

   #password label and password entry box
   passwordLabel = Label(window1,text="Password").grid(row=16, column=0)  
   password = StringVar()
   passwordEntry = Entry(window1, textvariable=password, show='*').grid(row=16, column=1)

   #mobile no label and mobile no entry box
   mobileLabel = Label(window1,text="Mobile Number").grid(row=17, column=0)  
   mobile = IntVar()
   passwordEntry = Entry(window1, textvariable=mobile).grid(row=17, column=1)

   #Location label and Location entry box
   locationLabel = Label(window1,text="Location").grid(row=18, column=0)  
   #location = StringVar()
   #passwordEntry = Entry(window1, textvariable=location).grid(row=18, column=1)
   variable = StringVar(window1)
   variable.set("Select the area") # default value
   w = OptionMenu(window1, variable, "Electronic City", "Jayanagar").grid(row=18, column=1)
   #confirm button
   Button(window1,text = 'Confirm', font = "times",bg = "light pink",command=confirm).place(x = 100, y =400)
   #Exit button
   Button(window1,text = 'Exit', font = "times",bg = "light pink",command=ex).place(x = 200, y =400)
def login():
   window.destroy()
   window1 = Tk()
   window1.title('ParkXpert')
   window1.configure(bg = "light blue")
   window1.geometry('500x600')
   
   def con():
       phno=username.get()
       pwd=password.get()
       print(phno)
       print(pwd)
       mycur.execute('insert into user_credentials(username, password) values(%s, %s)', (phno,pwd))
       mycon.commit()
       messagebox.showinfo("Message", "Your Information is stored in database")
       window1.destroy()
       window2 = Tk()
       window2.title('ParkXpert')
       window2.configure(bg = "light blue")
       window2.geometry('1200x700')
       LocationLabel = Label(window2,text="Type Of Vehicle", font = ("times",20),bg = "light blue").grid(row=18, column=0)
       
       
       def book1(v, j):
          Button(window2, text = ('Slot ', v), bg = 'red', padx = 20, pady = 20).place(x = 100 * j, y = 100)
              
       def book2(v, j):
          Button(window2, text = ('Slot ', v), bg = 'red', padx = 20, pady = 20).place(x = 100 * j, y = 175)
            
       
       def book3(v, j):
          Button(window2, text = ('Slot ', v), bg = 'red', padx = 20, pady = 20).place(x = 100 * j, y = 250)
            
                      
       i = 1; xlen = 20; ylen = 20; xloc = 100; yloc = 100
       Button(window2, text = ('Slot ', i), bg = 'light green', padx = xlen, pady = ylen, command = lambda:book1( 1,  1)).place(x = xloc, y = yloc); i += 1; xloc += 100
       Button(window2, text = ('Slot ', i), bg = 'light green', padx = xlen, pady = ylen, command = lambda:book1( 2,  2)).place(x = xloc, y = yloc); i += 1; xloc += 100
       Button(window2, text = ('Slot ', i), bg = 'light green', padx = xlen, pady = ylen, command = lambda:book1( 3,  3)).place(x = xloc, y = yloc); i += 1; xloc += 100
       Button(window2, text = ('Slot ', i), bg = 'light green', padx = xlen, pady = ylen, command = lambda:book1( 4,  4)).place(x = xloc, y = yloc); i += 1; xloc += 100
       Button(window2, text = ('Slot ', i), bg = 'light green', padx = xlen, pady = ylen, command = lambda:book1( 5,  5)).place(x = xloc, y = yloc); i += 1; xloc += 100
       Button(window2, text = ('Slot ', i), bg = 'light green', padx = xlen, pady = ylen, command = lambda:book1( 6,  6)).place(x = xloc, y = yloc); i += 1; xloc += 100
       Button(window2, text = ('Slot ', i), bg = 'light green', padx = xlen, pady = ylen, command = lambda:book1( 7,  7)).place(x = xloc, y = yloc); i += 1; xloc += 100
       Button(window2, text = ('Slot ', i), bg = 'light green', padx = xlen, pady = ylen, command = lambda:book1( 8,  8)).place(x = xloc, y = yloc); i += 1; xloc += 100
       Button(window2, text = ('Slot ', i), bg = 'light green', padx = xlen, pady = ylen, command = lambda:book1( 9,  9)).place(x = xloc, y = yloc); i += 1; xloc += 100
       Button(window2, text = ('Slot ', i), bg = 'light green', padx = xlen, pady = ylen, command = lambda:book1(10, 10)).place(x = xloc, y = yloc); i += 1;
       
       xloc = 100; yloc = 175
       Button(window2, text = ('Slot ', i), bg = 'light green', padx = xlen, pady = ylen, command = lambda:book2(11,  1)).place(x = xloc, y = yloc); i += 1; xloc += 100
       Button(window2, text = ('Slot ', i), bg = 'light green', padx = xlen, pady = ylen, command = lambda:book2(12,  2)).place(x = xloc, y = yloc); i += 1; xloc += 100
       Button(window2, text = ('Slot ', i), bg = 'light green', padx = xlen, pady = ylen, command = lambda:book2(13,  3)).place(x = xloc, y = yloc); i += 1; xloc += 100
       Button(window2, text = ('Slot ', i), bg = 'light green', padx = xlen, pady = ylen, command = lambda:book2(14,  4)).place(x = xloc, y = yloc); i += 1; xloc += 100
       Button(window2, text = ('Slot ', i), bg = 'light green', padx = xlen, pady = ylen, command = lambda:book2(15,  5)).place(x = xloc, y = yloc); i += 1; xloc += 100
       Button(window2, text = ('Slot ', i), bg = 'light green', padx = xlen, pady = ylen, command = lambda:book2(16,  6)).place(x = xloc, y = yloc); i += 1; xloc += 100
       Button(window2, text = ('Slot ', i), bg = 'light green', padx = xlen, pady = ylen, command = lambda:book2(17,  7)).place(x = xloc, y = yloc); i += 1; xloc += 100
       Button(window2, text = ('Slot ', i), bg = 'light green', padx = xlen, pady = ylen, command = lambda:book2(18,  8)).place(x = xloc, y = yloc); i += 1; xloc += 100
       Button(window2, text = ('Slot ', i), bg = 'light green', padx = xlen, pady = ylen, command = lambda:book2(19,  9)).place(x = xloc, y = yloc); i += 1; xloc += 100
       Button(window2, text = ('Slot ', i), bg = 'light green', padx = xlen, pady = ylen, command = lambda:book2(20, 10)).place(x = xloc, y = yloc); i += 1;
       
       xloc = 100; yloc = 250
       Button(window2, text = ('Slot ', i), bg = 'light green', padx = xlen, pady = ylen, command = lambda:book3(21,  1)).place(x = xloc, y = yloc); i += 1; xloc += 100
       Button(window2, text = ('Slot ', i), bg = 'light green', padx = xlen, pady = ylen, command = lambda:book3(22,  2)).place(x = xloc, y = yloc); i += 1; xloc += 100
       Button(window2, text = ('Slot ', i), bg = 'light green', padx = xlen, pady = ylen, command = lambda:book3(23,  3)).place(x = xloc, y = yloc); i += 1; xloc += 100
       Button(window2, text = ('Slot ', i), bg = 'light green', padx = xlen, pady = ylen, command = lambda:book3(24,  4)).place(x = xloc, y = yloc); i += 1; xloc += 100
       Button(window2, text = ('Slot ', i), bg = 'light green', padx = xlen, pady = ylen, command = lambda:book3(25,  5)).place(x = xloc, y = yloc); i += 1; xloc += 100
       Button(window2, text = ('Slot ', i), bg = 'light green', padx = xlen, pady = ylen, command = lambda:book3(26,  6)).place(x = xloc, y = yloc); i += 1; xloc += 100
       Button(window2, text = ('Slot ', i), bg = 'light green', padx = xlen, pady = ylen, command = lambda:book3(27,  7)).place(x = xloc, y = yloc); i += 1; xloc += 100
       Button(window2, text = ('Slot ', i), bg = 'light green', padx = xlen, pady = ylen, command = lambda:book3(28,  8)).place(x = xloc, y = yloc); i += 1; xloc += 100
       Button(window2, text = ('Slot ', i), bg = 'light green', padx = xlen, pady = ylen, command = lambda:book3(29,  9)).place(x = xloc, y = yloc); i += 1; xloc += 100
       Button(window2, text = ('Slot ', i), bg = 'light green', padx = xlen, pady = ylen, command = lambda:book3(30, 10)).place(x = xloc, y = yloc); i +1
       
       
       def book4(v, j):
         Button(window2, text = ('Slot ', v), bg = 'red', padx = 20, pady = 20).place(x = 100 * j, y = 400)
        
       def book5(v, j):
        Button(window2, text = ('Slot ', v), bg = 'red', padx = 20, pady = 20).place(x = 100 * j, y = 475)
        
       
                            
       i = 1; xlen = 20; ylen = 20; xloc = 100; yloc = 400
       Button(window2, text = ('Slot ', i), bg = 'light green', padx = xlen, pady = ylen, command = lambda:book4( 1,  1)).place(x = xloc, y = yloc); i += 1; xloc += 100
       Button(window2, text = ('Slot ', i), bg = 'light green', padx = xlen, pady = ylen, command = lambda:book4( 2,  2)).place(x = xloc, y = yloc); i += 1; xloc += 100
       Button(window2, text = ('Slot ', i), bg = 'light green', padx = xlen, pady = ylen, command = lambda:book4( 3,  3)).place(x = xloc, y = yloc); i += 1; xloc += 100
       Button(window2, text = ('Slot ', i), bg = 'light green', padx = xlen, pady = ylen, command = lambda:book4( 4,  4)).place(x = xloc, y = yloc); i += 1; xloc += 100
       Button(window2, text = ('Slot ', i), bg = 'light green', padx = xlen, pady = ylen, command = lambda:book4( 5,  5)).place(x = xloc, y = yloc); i += 1; xloc += 100
       Button(window2, text = ('Slot ', i), bg = 'light green', padx = xlen, pady = ylen, command = lambda:book4( 6,  6)).place(x = xloc, y = yloc); i += 1; xloc += 100
       Button(window2, text = ('Slot ', i), bg = 'light green', padx = xlen, pady = ylen, command = lambda:book4( 7,  7)).place(x = xloc, y = yloc); i += 1; xloc += 100
       Button(window2, text = ('Slot ', i), bg = 'light green', padx = xlen, pady = ylen, command = lambda:book4( 8,  8)).place(x = xloc, y = yloc); i += 1; xloc += 100
       Button(window2, text = ('Slot ', i), bg = 'light green', padx = xlen, pady = ylen, command = lambda:book4( 9,  9)).place(x = xloc, y = yloc); i += 1; xloc += 100
       Button(window2, text = ('Slot ', i), bg = 'light green', padx = xlen, pady = ylen, command = lambda:book4(10, 10)).place(x = xloc, y = yloc); i += 1;
       
       xloc = 100; yloc = 475
       Button(window2, text = ('Slot ', i), bg = 'light green', padx = xlen, pady = ylen, command = lambda:book5(11,  1)).place(x = xloc, y = yloc); i += 1; xloc += 100
       Button(window2, text = ('Slot ', i), bg = 'light green', padx = xlen, pady = ylen, command = lambda:book5(12,  2)).place(x = xloc, y = yloc); i += 1; xloc += 100
       Button(window2, text = ('Slot ', i), bg = 'light green', padx = xlen, pady = ylen, command = lambda:book5(13,  3)).place(x = xloc, y = yloc); i += 1; xloc += 100
       Button(window2, text = ('Slot ', i), bg = 'light green', padx = xlen, pady = ylen, command = lambda:book5(14,  4)).place(x = xloc, y = yloc); i += 1; xloc += 100
       Button(window2, text = ('Slot ', i), bg = 'light green', padx = xlen, pady = ylen, command = lambda:book5(15,  5)).place(x = xloc, y = yloc); i += 1; xloc += 100
       Button(window2, text = ('Slot ', i), bg = 'light green', padx = xlen, pady = ylen, command = lambda:book5(16,  6)).place(x = xloc, y = yloc); i += 1; xloc += 100
       Button(window2, text = ('Slot ', i), bg = 'light green', padx = xlen, pady = ylen, command = lambda:book5(17,  7)).place(x = xloc, y = yloc); i += 1; xloc += 100
       Button(window2, text = ('Slot ', i), bg = 'light green', padx = xlen, pady = ylen, command = lambda:book5(18,  8)).place(x = xloc, y = yloc); i += 1; xloc += 100
       Button(window2, text = ('Slot ', i), bg = 'light green', padx = xlen, pady = ylen, command = lambda:book5(19,  9)).place(x = xloc, y = yloc); i += 1; xloc += 100
       Button(window2, text = ('Slot ', i), bg = 'light green', padx = xlen, pady = ylen, command = lambda:book5(20, 10)).place(x = xloc, y = yloc); i += 1;
       
             
       Button(window2,text = 'Car', font = "times",bg = "light pink").place(x =25, y =200)
       Button(window2,text = 'Bike', font = "times",bg = "light pink").place(x = 25, y =450)
       Button(window2,text = 'proceed to pay', font = "times",bg = "light pink").place(x = 500, y =600)
       variable = StringVar(window2)
       variable.set("Select") # default value
       w = OptionMenu(window2, variable, "Car", "Bike")
       w.place(x=500,y=0)
       
      
 

   #username label and text entry box
   #usernameLabel = Label(window1, text="User Name").grid(row=15, column=0)
   #username = IntVar()
   username = Entry(window1,width=40)
   username.pack(pady= 20)
   #print(name)

   #password label and password entry box
   #passwordLabel = Label(window1,text="Password").grid(row=16, column=0)  
   #password = StringVar()
   password= Entry(window1, width=40)
   password.pack(pady= 20)   
	  
      
   #confirm button
   button= Button(window1,text = 'Confirm',command=con)
   button.pack(pady=10)

Button(window,text = 'Login', font = ("times",15),bg = "light pink",width=13,command=login).place(x = 450, y = 250)
Button(window,text = 'Signup', font = "times",bg = "light pink",command=register).place(x = 700, y = 0)
label=Label(window, text="Welcome to ", font = ("times",25), bg = "light blue")
label.place(x=200,y=240)
label=Label(window, text="E-City ParkXpert", font = ("times",20), bg = "light blue")
label.place(x=180,y=280)
label=Label(window, text="Login here", font = ("times",15), bg = "light blue")
label.place(x=490,y=220)
label=Label(window, text="Don't have an account? Sign up here", font = ("times",14), bg = "light blue")
label.place(x=450,y=300)


     



'''self.menuFile.addAction(self.actionNew)
self.menuFile.addAction(self.actionOpen)
self.menuFile.addAction(self.actionSave)
self.menuEdit.addAction(self.actionCut)
self.menuEdit.addAction(self.actionCopy)
self.menubar.addAction(self.menuFile.menuAction())
self.menubar.addAction(self.menuEdit.menuAction())
self.menubar.addAction(self.menuHelp.menuAction())'''
window.mainloop()

