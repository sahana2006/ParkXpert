from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import mysql.connector
import datetime

#Signup form for new user
def register():
    window1 = Tk()
    window1.title('Signup')
    window1.configure(bg = "light blue")
    window1.geometry('500x400')
    def submit():
        phno = username.get()
        pwds = pwd.get()
        cpwds = cpwd.get()
        nm = name.get()

        mycur.execute('select username from signup')
        users = mycur.fetchall()
        len_users = len(users)
        count = 0
        for i in users:
            if phno == str(i[0]):
                count = 1
                break

        if count == 1:
            messagebox.showerror("showerror", "Username already registered, Use different Username")
            username.delete(0, END)
            pwd.delete(0, END)
            cpwd.delete(0, END)
            name.delete(0, END)
        elif len((str)(phno)) != 10 or not((str)(phno)).isdigit():
            messagebox.showerror("showerror", "Invalid Username, Enter valid 10 digit Mobile number")
            username.delete(0, END)
            pwd.delete(0, END)
            cpwd.delete(0, END)
            name.delete(0, END)
        elif (str)(pwds) != (str)(cpwds):
            messagebox.showerror("showerror", "Password and Confirm Password not matching. Try again!")
            pwd.delete(0, END)
            cpwd.delete(0, END)
            name.delete(0, END)
        elif (str)(pwds) == "":
            messagebox.showerror("showerror", "Password cannot be empty. Try again!")
            pwd.delete(0, END)
            cpwd.delete(0, END)
            name.delete(0, END)
        elif (str)(nm) == "":
            messagebox.showerror("showerror", "Name cannot be empty. Try again!")
        elif ((str)(nm)).isdigit():
            messagebox.showerror("showerror", "Invalid Name. Enter valid Name")
            name.delete(0, END)
        else:
            mycur.execute('insert into signup(username, password, confirmpassword, name) values(%s, %s, %s, %s)', (phno, pwds, cpwds, nm))
            mycon.commit()
            messagebox.showinfo("Message", "You have signed up successfully")
            window1.destroy()

    label = Label(window1, text = "Username", font = ("times", 16), bg = "light blue")
    label.place(x = 10, y = 20)
    label = Label(window1, text = "(Mobile Number)", font = ("times", 10), bg = "light blue")
    label.place(x = 10, y = 45)
    label = Label(window1, text = "Password", font = ("times", 16), bg = "light blue")
    label.place(x = 10, y = 75)
    label = Label(window1, text = "Confirm", font = ("times", 16), bg = "light blue")
    label.place(x = 10, y = 125)
    label = Label(window1, text = "Password", font = ("times", 16), bg = "light blue")
    label.place(x = 10, y = 150)
    label = Label(window1, text = "Name", font = ("times", 16), bg = "light blue")
    label.place(x = 10, y = 190)

    username = Entry(window1, width = 40)
    username.pack(pady = 20)

    pwd = Entry(window1, width = 40, show = '*')
    pwd.pack(pady = 20)

    cpwd = Entry(window1, width = 40, show = '*')
    cpwd.pack(pady = 20)

    name = Entry(window1, width = 40)
    name.pack(pady = 20)

    button = Button(window1, text = 'Submit', command = submit)
    button.pack(pady = 10)

#Login form
def login():
    window.destroy()
    window1 = Tk()
    window1.title('Login')
    window1.configure(bg = "light blue")
    window1.geometry('500x300')

    def con():
        def mes():
            mycur.execute('insert into login(username, password) values(%s, %s)', (phno, pwd))
            mycon.commit()
            messagebox.showinfo("Message", "You have logged in successfully")
            window1.destroy()
            window3 = Tk()
            window3.title('SLOTS')
            window3.configure(bg = "light blue")
            window3.geometry('900x500')

            def slot_m():
                window3.destroy()
                window2 = Tk()
                window2.title('MORNING')
                window2.configure(bg = "light blue")
                window2.geometry('1200x700')
                LocationLabel = Label(window2, text = "Type Of Vehicle", font = ("times", 20), bg = "light blue").grid(row = 18, column = 0)
                def billing():
                    window2.destroy()
                    window4 = Tk()
                    window4.title('BILLING')
                    window4.configure(bg = "light blue")
                    window4.geometry('745x600')
                    mycur.execute('Select * from booking where username = %s and paid = %s', (phno, 'Unpaid'))
                    a = mycur.fetchall()
                    amt = 0
                    for i in a:
                        if i[1] == 'Car':
                            amt += 125
                        else:
                            amt += 50
                    ig = PhotoImage(file = "C:/Users/sahan/OneDrive/Desktop/ParkXpert/ty.png")
                    window4.ig = ig
                    l = Label(window4, image = ig)
                    l.place(x = 0, y = 0)
                    t = []
                    for i in a:
                        t.append(i[1])
                    x_len = X_len = 0
                    if 'Car' in t and 'Bike' in t:
                        label = Label(window4, text = ("Car", ":"), font = ("times", 16, 'italic'), bg = "light blue", fg = "black").place(x = 125, y = 320)
                        x_len = 125
                        label = Label(window4, text = ("Bike", ":"), font = ("times", 16, 'italic'), bg = "light blue", fg = "black").place(x = 125, y = 350)
                        X_len = 125
                    elif 'Car' in t:
                        label = Label(window4, text = ("Car", ":"), font = ("times", 16, 'italic'), bg = "light blue", fg = "black").place(x = 125, y = 320)
                        x_len = 125
                    elif 'Bike' in t:
                        label = Label(window4, text = ("Bike", ":"), font = ("times", 16, 'italic'), bg = "light blue", fg = "black").place(x = 125, y = 350)
                        X_len = 125
                    else:
                        label = Label(window4, text = ("No", "Slot", "is", "booked"), font = ("times", 16, 'bold'), bg = "light blue", fg = "maroon").place(x = 100, y = 300)

                    for i in a:
                        if i[1] == 'Car':
                            x_len += 50
                            label = Label(window4, text = (i[2]), font = ("times", 16, 'italic'), bg = "light blue", fg = "black").place(x = x_len, y = 320)
                        else:
                            X_len += 50
                            label = Label(window4, text = (i[2]), font = ("times", 16, 'italic'), bg = "light blue", fg = "black").place(x = X_len, y = 350)

                    label = Label(window4, text = ("Booked", "Slots", ":"), font = ("times", 16, 'bold'), bg = "light blue", fg = "maroon").place(x = 100, y = 275)
                    label = Label(window4, text = ("Amount", ":", "Rs", amt), font = ("times", 16, 'italic'), bg = "light green", fg = "black", relief = RAISED).place(x = 100, y = 400)
                    label = Label(window4, text = "Thanks for visiting, HAPPY PARKING", font = ("times", 16, 'italic'), bg = "light green", fg = "black", relief = RAISED).place(x = 100, y = 450)
                    mycur.execute('Update booking set paid = %s where username = %s and paid = %s', ('Paid', phno, 'Unpaid'))
                    mycon.commit()

                def book1(v, j):
                    Button(window2, text = ('Slot ', v), bg = 'red', padx = 20, pady = 20).place(x = 100 * j, y = 100)
                    mycur.execute('insert into booking(username, type, slot, time) values(%s, %s, %s, %s)', (phno, 'Car', v, 'M'))
                    mycon.commit()
                    mycur.execute('Update morning_slot set Avl = %s where slot = %s and type = %s', ('B', v, 'Car'))
                    mycon.commit()

                def book2(v, j):
                    Button(window2, text = ('Slot ', v), bg = 'red', padx = 20, pady = 20).place(x = 100 * j, y = 175)
                    mycur.execute('insert into booking(username, type, slot, time) values(%s, %s, %s, %s)', (phno, 'Car', v, 'M'))
                    mycon.commit()
                    mycur.execute('Update morning_slot set Avl = %s where slot = %s and type = %s', ('B', v, 'Car'))
                    mycon.commit()

                def book3(v, j):
                    Button(window2, text = ('Slot ', v), bg = 'red', padx = 20, pady = 20).place(x = 100 * j, y = 250)
                    mycur.execute('insert into booking(username, type, slot, time) values(%s, %s, %s, %s)', (phno, 'Car', v, 'M'))
                    mycon.commit()
                    mycur.execute('Update morning_slot set Avl = %s where slot = %s and type = %s', ('B', v, 'Car'))
                    mycon.commit()

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
                    mycur.execute('insert into booking(username, type, slot, time) values(%s, %s, %s, %s)', (phno, 'Bike', v, 'M'))
                    mycon.commit()
                    mycur.execute('Update morning_slot set Avl = %s where slot = %s and type = %s', ('B', v, 'Bike'))
                    mycon.commit()

                def book5(v, j):
                    Button(window2, text = ('Slot ', v), bg = 'red', padx = 20, pady = 20).place(x = 100 * j, y = 475)
                    mycur.execute('insert into booking(username, type, slot, time) values(%s, %s, %s, %s)', (phno, 'Bike', v, 'M'))
                    mycon.commit()
                    mycur.execute('Update morning_slot set Avl = %s where slot = %s and type = %s', ('B', v, 'Bike'))
                    mycon.commit()

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

                #To re-establish the red boxes of already booked slots
                mycur.execute("select * from morning_slot where Avl = 'B'")
                tupl = mycur.fetchall()
                for i in tupl:
                    if i[0] == 'Car':
                        if i[1] <= 10:
                            Button(window2, text = ('Slot ', i[1]), bg = 'red', padx = 20, pady = 20, state = DISABLED).place(x = i[1] * 100, y = 100)
                        elif i[1] <= 20:
                            d = i[1] % 10
                            if d == 0:
                                Button(window2, text = ('Slot ', i[1]), bg = 'red', padx = 20, pady = 20, state = DISABLED).place(x = 10 * 100, y = 175)
                            else:
                                Button(window2, text = ('Slot ', i[1]), bg = 'red', padx = 20, pady = 20, state = DISABLED).place(x = d * 100, y = 175)
                        else:
                            d = i[1] % 10
                            if d == 0:
                                Button(window2, text = ('Slot ', i[1]), bg = 'red', padx = 20, pady = 20, state = DISABLED).place(x = 10 * 100, y = 250)
                            else:
                                Button(window2, text = ('Slot ', i[1]), bg = 'red', padx = 20, pady = 20, state = DISABLED).place(x = d * 100, y = 250)
                    else:
                        if i[1] <= 10:
                            Button(window2, text = ('Slot ', i[1]), bg = 'red', padx = 20, pady = 20, state = DISABLED).place(x = i[1] * 100, y = 400)
                        else:
                            d = i[1] % 10
                            if d == 0:
                                Button(window2, text = ('Slot ', i[1]), bg = 'red', padx = 20, pady = 20, state = DISABLED).place(x = 10 * 100, y = 475)
                            else:
                                Button(window2, text = ('Slot ', i[1]), bg = 'red', padx = 20, pady = 20, state = DISABLED).place(x = d * 100, y = 475)

                Button(window2, text = 'Car', font = "times", bg = "light pink").place(x = 25, y = 200)
                Button(window2, text = 'Bike', font = "times", bg = "light pink").place(x = 25, y = 450)
                Button(window2, text = 'Proceed to Payment', font = "times", bg = "light pink", command = billing).place(x = 500, y = 600)

            def slot_a():
                window3.destroy()
                window2 = Tk()
                window2.title('AFTERNOON')
                window2.configure(bg = "light blue")
                window2.geometry('1200x700')
                LocationLabel = Label(window2, text = "Type Of Vehicle", font = ("times", 20), bg = "light blue").grid(row = 18, column = 0)
                def billing():
                    window2.destroy()
                    window4 = Tk()
                    window4.title('BILLING')
                    window4.configure(bg = "light blue")
                    window4.geometry('745x600')
                    mycur.execute('Select * from booking where username = %s and paid = %s', (phno, 'Unpaid'))
                    a = mycur.fetchall()
                    amt = 0
                    for i in a:
                        if i[1] == 'Car':
                            amt += 150
                        else:
                            amt += 75
                    ig = PhotoImage(file = "C:/Users/sahan/OneDrive/Desktop/ParkXpert/ty.png")
                    window4.ig = ig
                    l = Label(window4, image = ig)
                    l.place(x = 0, y = 0)
                    t = []
                    for i in a:
                        t.append(i[1])
                    x_len = X_len = 0
                    if 'Car' in t and 'Bike' in t:
                        label = Label(window4, text = ("Car", ":"), font = ("times", 16, 'italic'), bg = "light blue", fg = "black").place(x = 125, y = 320)
                        x_len = 125
                        label = Label(window4, text = ("Bike", ":"), font = ("times", 16, 'italic'), bg = "light blue", fg = "black").place(x = 125, y = 350)
                        X_len = 125
                    elif 'Car' in t:
                        label = Label(window4, text = ("Car", ":"), font = ("times", 16, 'italic'), bg = "light blue", fg = "black").place(x = 125, y = 320)
                        x_len = 125
                    elif 'Bike' in t:
                        label = Label(window4, text = ("Bike", ":"), font = ("times", 16, 'italic'), bg = "light blue", fg = "black").place(x = 125, y = 350)
                        X_len = 125
                    else:
                        label = Label(window4, text = ("No", "Slot", "is", "booked"), font = ("times", 16, 'bold'), bg = "light blue", fg = "maroon").place(x = 100, y = 300)

                    for i in a:
                        if i[1] == 'Car':
                            x_len += 50
                            label = Label(window4, text = (i[2]), font = ("times", 16, 'italic'), bg = "light blue", fg = "black").place(x = x_len, y = 320)
                        else:
                            X_len += 50
                            label = Label(window4, text = (i[2]), font = ("times", 16, 'italic'), bg = "light blue", fg = "black").place(x = X_len, y = 350)

                    label = Label(window4, text = ("Booked", "Slots", ":"), font = ("times", 16, 'bold'), bg = "light blue", fg = "maroon").place(x = 100, y = 275)
                    label = Label(window4, text = ("Amount", ":", "Rs", amt), font = ("times", 16, 'italic'), bg = "light green", fg = "black", relief = RAISED).place(x = 100, y = 400)
                    label = Label(window4, text = "Thanks for visiting, HAPPY PARKING", font = ("times", 16, 'italic'), bg = "light green", fg = "black", relief = RAISED).place(x = 100, y = 450)
                    mycur.execute('Update booking set paid = %s where username = %s and paid = %s', ('Paid', phno, 'Unpaid'))
                    mycon.commit()

                def book1(v, j):
                    Button(window2, text = ('Slot ', v), bg = 'red', padx = 20, pady = 20).place(x = 100 * j, y = 100)
                    mycur.execute('insert into booking(username, type, slot, time) values(%s, %s, %s, %s)', (phno, 'Car', v, 'A'))
                    mycon.commit()
                    mycur.execute('Update afternoon_slot set Avl = %s where slot = %s and type = %s', ('B', v, 'Car'))
                    mycon.commit()

                def book2(v, j):
                    Button(window2, text = ('Slot ', v), bg = 'red', padx = 20, pady = 20).place(x = 100 * j, y = 175)
                    mycur.execute('insert into booking(username, type, slot, time) values(%s, %s, %s, %s)', (phno, 'Car', v, 'A'))
                    mycon.commit()
                    mycur.execute('Update afternoon_slot set Avl = %s where slot = %s and type = %s', ('B', v, 'Car'))
                    mycon.commit()

                def book3(v, j):
                    Button(window2, text = ('Slot ', v), bg = 'red', padx = 20, pady = 20).place(x = 100 * j, y = 250)
                    mycur.execute('insert into booking(username, type, slot, time) values(%s, %s, %s, %s)', (phno, 'Car', v, 'A'))
                    mycon.commit()
                    mycur.execute('Update afternoon_slot set Avl = %s where slot = %s and type = %s', ('B', v, 'Car'))
                    mycon.commit()

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
                    mycur.execute('insert into booking(username, type, slot, time) values(%s, %s, %s, %s)', (phno, 'Bike', v, 'A'))
                    mycon.commit()
                    mycur.execute('Update afternoon_slot set Avl = %s where slot = %s and type = %s', ('B', v, 'Bike'))
                    mycon.commit()

                def book5(v, j):
                    Button(window2, text = ('Slot ', v), bg = 'red', padx = 20, pady = 20).place(x = 100 * j, y = 475)
                    mycur.execute('insert into booking(username, type, slot, time) values(%s, %s, %s, %s)', (phno, 'Bike', v, 'A'))
                    mycon.commit()
                    mycur.execute('Update afternoon_slot set Avl = %s where slot = %s and type = %s', ('B', v, 'Bike'))
                    mycon.commit()

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

                #To re-establish the red boxes of already booked slots
                mycur.execute("select * from afternoon_slot where Avl = 'B'")
                tupl = mycur.fetchall()
                for i in tupl:
                    if i[0] == 'Car':
                        if i[1] <= 10:
                            Button(window2, text = ('Slot ', i[1]), bg = 'red', padx = 20, pady = 20, state = DISABLED).place(x = i[1] * 100, y = 100)
                        elif i[1] <= 20:
                            d = i[1] % 10
                            if d == 0:
                                Button(window2, text = ('Slot ', i[1]), bg = 'red', padx = 20, pady = 20, state = DISABLED).place(x = 10 * 100, y = 175)
                            else:
                                Button(window2, text = ('Slot ', i[1]), bg = 'red', padx = 20, pady = 20, state = DISABLED).place(x = d * 100, y = 175)
                        else:
                            d = i[1] % 10
                            if d == 0:
                                Button(window2, text = ('Slot ', i[1]), bg = 'red', padx = 20, pady = 20, state = DISABLED).place(x = 10 * 100, y = 250)
                            else:
                                Button(window2, text = ('Slot ', i[1]), bg = 'red', padx = 20, pady = 20, state = DISABLED).place(x = d * 100, y = 250)
                    else:
                        if i[1] <= 10:
                            Button(window2, text = ('Slot ', i[1]), bg = 'red', padx = 20, pady = 20, state = DISABLED).place(x = i[1] * 100, y = 400)
                        else:
                            d = i[1] % 10
                            if d == 0:
                                Button(window2, text = ('Slot ', i[1]), bg = 'red', padx = 20, pady = 20, state = DISABLED).place(x = 10 * 100, y = 475)
                            else:
                                Button(window2, text = ('Slot ', i[1]), bg = 'red', padx = 20, pady = 20, state = DISABLED).place(x = d * 100, y = 475)

                Button(window2, text = 'Car', font = "times", bg = "light pink").place(x = 25, y = 200)
                Button(window2, text = 'Bike', font = "times", bg = "light pink").place(x = 25, y = 450)
                Button(window2, text = 'Proceed to Payment', font = "times", bg = "light pink", command = billing).place(x = 500, y = 600)

            def slot_e():
                window3.destroy()
                window2 = Tk()
                window2.title('EVENING')
                window2.configure(bg = "light blue")
                window2.geometry('1200x700')
                LocationLabel = Label(window2, text = "Type Of Vehicle", font = ("times", 20), bg = "light blue").grid(row = 18, column = 0)
                def billing():
                    window2.destroy()
                    window4 = Tk()
                    window4.title('BILLING')
                    window4.configure(bg = "light blue")
                    window4.geometry('745x600')
                    mycur.execute('Select * from booking where username = %s and paid = %s', (phno, 'Unpaid'))
                    a = mycur.fetchall()
                    amt = 0
                    for i in a:
                        if i[1] == 'Car':
                            amt += 125
                        else:
                            amt += 50
                    ig = PhotoImage(file = "C:/Users/sahan/OneDrive/Desktop/ParkXpert/ty.png")
                    window4.ig = ig
                    l = Label(window4, image = ig)
                    l.place(x = 0, y = 0)
                    t = []
                    for i in a:
                        t.append(i[1])
                    x_len = X_len = 0
                    if 'Car' in t and 'Bike' in t:
                        label = Label(window4, text = ("Car", ":"), font = ("times", 16, 'italic'), bg = "light blue", fg = "black").place(x = 125, y = 320)
                        x_len = 125
                        label = Label(window4, text = ("Bike", ":"), font = ("times", 16, 'italic'), bg = "light blue", fg = "black").place(x = 125, y = 350)
                        X_len = 125
                    elif 'Car' in t:
                        label = Label(window4, text = ("Car", ":"), font = ("times", 16, 'italic'), bg = "light blue", fg = "black").place(x = 125, y = 320)
                        x_len = 125
                    elif 'Bike' in t:
                        label = Label(window4, text = ("Bike", ":"), font = ("times", 16, 'italic'), bg = "light blue", fg = "black").place(x = 125, y = 350)
                        X_len = 125
                    else:
                        label = Label(window4, text = ("No", "Slot", "is", "booked"), font = ("times", 16, 'bold'), bg = "light blue", fg = "maroon").place(x = 100, y = 300)

                    for i in a:
                        if i[1] == 'Car':
                            x_len += 50
                            label = Label(window4, text = (i[2]), font = ("times", 16, 'italic'), bg = "light blue", fg = "black").place(x = x_len, y = 320)
                        else:
                            X_len += 50
                            label = Label(window4, text = (i[2]), font = ("times", 16, 'italic'), bg = "light blue", fg = "black").place(x = X_len, y = 350)

                    label = Label(window4, text = ("Booked", "Slots", ":"), font = ("times", 16, 'bold'), bg = "light blue", fg = "maroon").place(x = 100, y = 275)
                    label = Label(window4, text = ("Amount", ":", "Rs", amt), font = ("times", 16, 'italic'), bg = "light green", fg = "black", relief = RAISED).place(x = 100, y = 400)
                    label = Label(window4, text = "Thanks for visiting, HAPPY PARKING", font = ("times", 16, 'italic'), bg = "light green", fg = "black", relief = RAISED).place(x = 100, y = 450)
                    mycur.execute('Update booking set paid = %s where username = %s and paid = %s', ('Paid', phno, 'Unpaid'))
                    mycon.commit()

                def book1(v, j):
                    Button(window2, text = ('Slot ', v), bg = 'red', padx = 20, pady = 20).place(x = 100 * j, y = 100)
                    mycur.execute('insert into booking(username, type, slot, time) values(%s, %s, %s, %s)', (phno, 'Car', v, 'E'))
                    mycon.commit()
                    mycur.execute('Update evening_slot set Avl = %s where slot = %s and type = %s', ('B', v, 'Car'))
                    mycon.commit()

                def book2(v, j):
                    Button(window2, text = ('Slot ', v), bg = 'red', padx = 20, pady = 20).place(x = 100 * j, y = 175)
                    mycur.execute('insert into booking(username, type, slot, time) values(%s, %s, %s, %s)', (phno, 'Car', v, 'E'))
                    mycon.commit()
                    mycur.execute('Update evening_slot set Avl = %s where slot = %s and type = %s', ('B', v, 'Car'))
                    mycon.commit()

                def book3(v, j):
                    Button(window2, text = ('Slot ', v), bg = 'red', padx = 20, pady = 20).place(x = 100 * j, y = 250)
                    mycur.execute('insert into booking(username, type, slot, time) values(%s, %s, %s, %s)', (phno, 'Car', v, 'E'))
                    mycon.commit()
                    mycur.execute('Update evening_slot set Avl = %s where slot = %s and type = %s', ('B', v, 'Car'))
                    mycon.commit()

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
                    mycur.execute('insert into booking(username, type, slot, time) values(%s, %s, %s, %s)', (phno, 'Bike', v, 'E'))
                    mycon.commit()
                    mycur.execute('Update evening_slot set Avl = %s where slot = %s and type = %s', ('B', v, 'Bike'))
                    mycon.commit()

                def book5(v, j):
                    Button(window2, text = ('Slot ', v), bg = 'red', padx = 20, pady = 20).place(x = 100 * j, y = 475)
                    mycur.execute('insert into booking(username, type, slot, time) values(%s, %s, %s, %s)', (phno, 'Bike', v, 'E'))
                    mycon.commit()
                    mycur.execute('Update evening_slot set Avl = %s where slot = %s and type = %s', ('B', v, 'Bike'))
                    mycon.commit()

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

                #To re-establish the red boxes of already booked slots
                mycur.execute("select * from evening_slot where Avl = 'B'")
                tupl = mycur.fetchall()
                for i in tupl:
                    if i[0] == 'Car':
                        if i[1] <= 10:
                            Button(window2, text = ('Slot ', i[1]), bg = 'red', padx = 20, pady = 20, state = DISABLED).place(x = i[1] * 100, y = 100)
                        elif i[1] <= 20:
                            d = i[1] % 10
                            if d == 0:
                                Button(window2, text = ('Slot ', i[1]), bg = 'red', padx = 20, pady = 20, state = DISABLED).place(x = 10 * 100, y = 175)
                            else:
                                Button(window2, text = ('Slot ', i[1]), bg = 'red', padx = 20, pady = 20, state = DISABLED).place(x = d * 100, y = 175)
                        else:
                            d = i[1] % 10
                            if d == 0:
                                Button(window2, text = ('Slot ', i[1]), bg = 'red', padx = 20, pady = 20, state = DISABLED).place(x = 10 * 100, y = 250)
                            else:
                                Button(window2, text = ('Slot ', i[1]), bg = 'red', padx = 20, pady = 20, state = DISABLED).place(x = d * 100, y = 250)
                    else:
                        if i[1] <= 10:
                            Button(window2, text = ('Slot ', i[1]), bg = 'red', padx = 20, pady = 20, state = DISABLED).place(x = i[1] * 100, y = 400)
                        else:
                            d = i[1] % 10
                            if d == 0:
                                Button(window2, text = ('Slot ', i[1]), bg = 'red', padx = 20, pady = 20, state = DISABLED).place(x = 10 * 100, y = 475)
                            else:
                                Button(window2, text = ('Slot ', i[1]), bg = 'red', padx = 20, pady = 20, state = DISABLED).place(x = d * 100, y = 475)

                Button(window2, text = 'Car', font = "times", bg = "light pink").place(x = 25, y = 200)
                Button(window2, text = 'Bike', font = "times", bg = "light pink").place(x = 25, y = 450)
                Button(window2, text = 'Proceed to Payment', font = "times", bg = "light pink", command = billing).place(x = 500, y = 600)

            def slot_f():
                window3.destroy()
                window2 = Tk()
                window2.title('ONE FULL DAY')
                window2.configure(bg = "light blue")
                window2.geometry('1200x700')
                LocationLabel = Label(window2, text = "Type Of Vehicle", font = ("times", 20), bg = "light blue").grid(row = 18, column = 0)
                def billing():
                    window2.destroy()
                    window4 = Tk()
                    window4.title('BILLING')
                    window4.configure(bg = "light blue")
                    window4.geometry('745x600')
                    mycur.execute('Select * from booking where username = %s and paid = %s', (phno, 'Unpaid'))
                    a = mycur.fetchall()
                    amt = 0
                    for i in a:
                        if i[1] == 'Car':
                            amt += 250
                        else:
                            amt += 100
                    ig = PhotoImage(file = "C:/Users/sahan/OneDrive/Desktop/ParkXpert/ty.png")
                    window4.ig = ig
                    l = Label(window4, image = ig)
                    l.place(x = 0, y = 0)
                    t = []
                    for i in a:
                        t.append(i[1])
                    x_len = X_len = 0
                    if 'Car' in t and 'Bike' in t:
                        label = Label(window4, text = ("Car", ":"), font = ("times", 16, 'italic'), bg = "light blue", fg = "black").place(x = 125, y = 320)
                        x_len = 125
                        label = Label(window4, text = ("Bike", ":"), font = ("times", 16, 'italic'), bg = "light blue", fg = "black").place(x = 125, y = 350)
                        X_len = 125
                    elif 'Car' in t:
                        label = Label(window4, text = ("Car", ":"), font = ("times", 16, 'italic'), bg = "light blue", fg = "black").place(x = 125, y = 320)
                        x_len = 125
                    elif 'Bike' in t:
                        label = Label(window4, text = ("Bike", ":"), font = ("times", 16, 'italic'), bg = "light blue", fg = "black").place(x = 125, y = 350)
                        X_len = 125
                    else:
                        label = Label(window4, text = ("No", "Slot", "is", "booked"), font = ("times", 16, 'bold'), bg = "light blue", fg = "maroon").place(x = 100, y = 300)

                    for i in a:
                        if i[1] == 'Car':
                            x_len += 50
                            label = Label(window4, text = (i[2]), font = ("times", 16, 'italic'), bg = "light blue", fg = "black").place(x = x_len, y = 320)
                        else:
                            X_len += 50
                            label = Label(window4, text = (i[2]), font = ("times", 16, 'italic'), bg = "light blue", fg = "black").place(x = X_len, y = 350)

                    label = Label(window4, text = ("Booked", "Slots", ":"), font = ("times", 16, 'bold'), bg = "light blue", fg = "maroon").place(x = 100, y = 275)
                    label = Label(window4, text = ("Amount", ":", "Rs", amt), font = ("times", 16, 'italic'), bg = "light green", fg = "black", relief = RAISED).place(x = 100, y = 400)
                    label = Label(window4, text = "Thanks for visiting, HAPPY PARKING", font = ("times", 16, 'italic'), bg = "light green", fg = "black", relief = RAISED).place(x = 100, y = 450)
                    mycur.execute('Update booking set paid = %s where username = %s and paid = %s', ('Paid', phno, 'Unpaid'))
                    mycon.commit()

                def book1(v, j):
                    Button(window2, text = ('Slot ', v), bg = 'red', padx = 20, pady = 20).place(x = 100 * j, y = 100)
                    mycur.execute('insert into booking(username, type, slot, time) values(%s, %s, %s, %s)', (phno, 'Car', v, 'D'))
                    mycon.commit()
                    mycur.execute('Update morning_slot set Avl = %s where slot = %s and type = %s', ('B', v, 'Car'))
                    mycon.commit()
                    mycur.execute('Update afternoon_slot set Avl = %s where slot = %s and type = %s', ('B', v, 'Car'))
                    mycon.commit()
                    mycur.execute('Update evening_slot set Avl = %s where slot = %s and type = %s', ('B', v, 'Car'))
                    mycon.commit()

                def book2(v, j):
                    Button(window2, text = ('Slot ', v), bg = 'red', padx = 20, pady = 20).place(x = 100 * j, y = 175)
                    mycur.execute('insert into booking(username, type, slot, time) values(%s, %s, %s, %s)', (phno, 'Car', v, 'D'))
                    mycon.commit()
                    mycur.execute('Update morning_slot set Avl = %s where slot = %s and type = %s', ('B', v, 'Car'))
                    mycon.commit()
                    mycur.execute('Update afternoon_slot set Avl = %s where slot = %s and type = %s', ('B', v, 'Car'))
                    mycon.commit()
                    mycur.execute('Update evening_slot set Avl = %s where slot = %s and type = %s', ('B', v, 'Car'))
                    mycon.commit()

                def book3(v, j):
                    Button(window2, text = ('Slot ', v), bg = 'red', padx = 20, pady = 20).place(x = 100 * j, y = 250)
                    mycur.execute('insert into booking(username, type, slot, time) values(%s, %s, %s, %s)', (phno, 'Car', v, 'D'))
                    mycon.commit()
                    mycur.execute('Update morning_slot set Avl = %s where slot = %s and type = %s', ('B', v, 'Car'))
                    mycon.commit()
                    mycur.execute('Update afternoon_slot set Avl = %s where slot = %s and type = %s', ('B', v, 'Car'))
                    mycon.commit()
                    mycur.execute('Update evening_slot set Avl = %s where slot = %s and type = %s', ('B', v, 'Car'))
                    mycon.commit()

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
                    mycur.execute('insert into booking(username, type, slot, time) values(%s, %s, %s, %s)', (phno, 'Bike', v, 'D'))
                    mycon.commit()
                    mycur.execute('Update morning_slot set Avl = %s where slot = %s and type = %s', ('B', v, 'Bike'))
                    mycon.commit()
                    mycur.execute('Update afternoon_slot set Avl = %s where slot = %s and type = %s', ('B', v, 'Bike'))
                    mycon.commit()
                    mycur.execute('Update evening_slot set Avl = %s where slot = %s and type = %s', ('B', v, 'Bike'))
                    mycon.commit()

                def book5(v, j):
                    Button(window2, text = ('Slot ', v), bg = 'red', padx = 20, pady = 20).place(x = 100 * j, y = 475)
                    mycur.execute('insert into booking(username, type, slot, time) values(%s, %s, %s, %s)', (phno, 'Bike', v, 'D'))
                    mycon.commit()
                    mycur.execute('Update morning_slot set Avl = %s where slot = %s and type = %s', ('B', v, 'Bike'))
                    mycon.commit()
                    mycur.execute('Update afternoon_slot set Avl = %s where slot = %s and type = %s', ('B', v, 'Bike'))
                    mycon.commit()
                    mycur.execute('Update evening_slot set Avl = %s where slot = %s and type = %s', ('B', v, 'Bike'))
                    mycon.commit()

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

                #To re-establish the red boxes of MORNING SLOTS
                mycur.execute("select * from morning_slot where Avl = 'B'")
                tupl = mycur.fetchall()
                for i in tupl:
                    if i[0] == 'Car':
                        if i[1] <= 10:
                            Button(window2, text = ('Slot ', i[1]), bg = 'red', padx = 20, pady = 20, state = DISABLED).place(x = i[1] * 100, y = 100)
                        elif i[1] <= 20:
                            d = i[1] % 10
                            if d == 0:
                                Button(window2, text = ('Slot ', i[1]), bg = 'red', padx = 20, pady = 20, state = DISABLED).place(x = 10 * 100, y = 175)
                            else:
                                Button(window2, text = ('Slot ', i[1]), bg = 'red', padx = 20, pady = 20, state = DISABLED).place(x = d * 100, y = 175)
                        else:
                            d = i[1] % 10
                            if d == 0:
                                Button(window2, text = ('Slot ', i[1]), bg = 'red', padx = 20, pady = 20, state = DISABLED).place(x = 10 * 100, y = 250)
                            else:
                                Button(window2, text = ('Slot ', i[1]), bg = 'red', padx = 20, pady = 20, state = DISABLED).place(x = d * 100, y = 250)
                    else:
                        if i[1] <= 10:
                            Button(window2, text = ('Slot ', i[1]), bg = 'red', padx = 20, pady = 20, state = DISABLED).place(x = i[1] * 100, y = 400)
                        else:
                            d = i[1] % 10
                            if d == 0:
                                Button(window2, text = ('Slot ', i[1]), bg = 'red', padx = 20, pady = 20, state = DISABLED).place(x = 10 * 100, y = 475)
                            else:
                                Button(window2, text = ('Slot ', i[1]), bg = 'red', padx = 20, pady = 20, state = DISABLED).place(x = d * 100, y = 475)

                #To re-establish the red boxes of AFTERNOON SLOTS
                mycur.execute("select * from afternoon_slot where Avl = 'B'")
                tupl = mycur.fetchall()
                for i in tupl:
                    if i[0] == 'Car':
                        if i[1] <= 10:
                            Button(window2, text = ('Slot ', i[1]), bg = 'red', padx = 20, pady = 20, state = DISABLED).place(x = i[1] * 100, y = 100)
                        elif i[1] <= 20:
                            d = i[1] % 10
                            if d == 0:
                                Button(window2, text = ('Slot ', i[1]), bg = 'red', padx = 20, pady = 20, state = DISABLED).place(x = 10 * 100, y = 175)
                            else:
                                Button(window2, text = ('Slot ', i[1]), bg = 'red', padx = 20, pady = 20, state = DISABLED).place(x = d * 100, y = 175)
                        else:
                            d = i[1] % 10
                            if d == 0:
                                Button(window2, text = ('Slot ', i[1]), bg = 'red', padx = 20, pady = 20, state = DISABLED).place(x = 10 * 100, y = 250)
                            else:
                                Button(window2, text = ('Slot ', i[1]), bg = 'red', padx = 20, pady = 20, state = DISABLED).place(x = d * 100, y = 250)
                    else:
                        if i[1] <= 10:
                            Button(window2, text = ('Slot ', i[1]), bg = 'red', padx = 20, pady = 20, state = DISABLED).place(x = i[1] * 100, y = 400)
                        else:
                            d = i[1] % 10
                            if d == 0:
                                Button(window2, text = ('Slot ', i[1]), bg = 'red', padx = 20, pady = 20, state = DISABLED).place(x = 10 * 100, y = 475)
                            else:
                                Button(window2, text = ('Slot ', i[1]), bg = 'red', padx = 20, pady = 20, state = DISABLED).place(x = d * 100, y = 475)

                #To re-establish the red boxes of EVENING SLOTS
                mycur.execute("select * from evening_slot where Avl = 'B'")
                tupl = mycur.fetchall()
                for i in tupl:
                    if i[0] == 'Car':
                        if i[1] <= 10:
                            Button(window2, text = ('Slot ', i[1]), bg = 'red', padx = 20, pady = 20, state = DISABLED).place(x = i[1] * 100, y = 100)
                        elif i[1] <= 20:
                            d = i[1] % 10
                            if d == 0:
                                Button(window2, text = ('Slot ', i[1]), bg = 'red', padx = 20, pady = 20, state = DISABLED).place(x = 10 * 100, y = 175)
                            else:
                                Button(window2, text = ('Slot ', i[1]), bg = 'red', padx = 20, pady = 20, state = DISABLED).place(x = d * 100, y = 175)
                        else:
                            d = i[1] % 10
                            if d == 0:
                                Button(window2, text = ('Slot ', i[1]), bg = 'red', padx = 20, pady = 20, state = DISABLED).place(x = 10 * 100, y = 250)
                            else:
                                Button(window2, text = ('Slot ', i[1]), bg = 'red', padx = 20, pady = 20, state = DISABLED).place(x = d * 100, y = 250)
                    else:
                        if i[1] <= 10:
                            Button(window2, text = ('Slot ', i[1]), bg = 'red', padx = 20, pady = 20, state = DISABLED).place(x = i[1] * 100, y = 400)
                        else:
                            d = i[1] % 10
                            if d == 0:
                                Button(window2, text = ('Slot ', i[1]), bg = 'red', padx = 20, pady = 20, state = DISABLED).place(x = 10 * 100, y = 475)
                            else:
                                Button(window2, text = ('Slot ', i[1]), bg = 'red', padx = 20, pady = 20, state = DISABLED).place(x = d * 100, y = 475)

                Button(window2, text = 'Car', font = "times", bg = "light pink").place(x = 25, y = 200)
                Button(window2, text = 'Bike', font = "times", bg = "light pink").place(x = 25, y = 450)
                Button(window2, text = 'Proceed to Payment', font = "times", bg = "light pink", command = billing).place(x = 500,  y = 600)

            park = ttk.Treeview(window3, column = ("S.No", "Slots", "Timings", "Car Rates", "Bike Rates"), show = 'headings', height = 5)
            park.column("S.No", anchor = CENTER, width = 40)
            park.column("Slots", anchor = CENTER, width = 100)
            park.column("Timings", anchor = CENTER, width = 100)
            park.column("Car Rates", anchor = CENTER, width = 80)
            park.column("Bike Rates", anchor = CENTER, width = 80)

            park.heading("S.No", text = "#", anchor = CENTER)
            park.heading("Slots", text = "Slots", anchor = CENTER)
            park.heading("Timings", text = "Timings", anchor = CENTER)
            park.heading("Car Rates", text = "Car Rates", anchor = CENTER)
            park.heading("Bike Rates", text = "Bike Rates", anchor = CENTER)

            park.insert(parent = '', index = 'end', iid = 0, text = '', values = ('1', 'Morning', '7am to 12pm', '125', '50'))
            park.insert(parent = '', index = 'end', iid = 1, text = '', values = ('2', 'Afternoon', '12pm to 5pm', '150', '75'))
            park.insert(parent = '', index = 'end', iid = 2, text = '', values = ('3', 'Evening', '5pm to 10pm', '125', '50'))
            park.insert(parent = '', index = 'end', iid = 3, text = '', values = ('4', 'One Full Day', '7am to 10pm', '250', '100'))
            park.place(x=475,y=50)

            Button(window3, text = 'MORNING', font = "times", bg = "light pink", padx = 60, pady = 0, command = slot_m).place(x = 225, y = 50)
            Button(window3, text = 'AFTERNOON', font = "times", bg = "light pink", padx = 47, pady = 0, command = slot_a).place(x = 225, y = 80)
            Button(window3, text = 'EVENING ', font = "times", bg = "light pink", padx = 61, pady = 0, command = slot_e).place(x = 225, y = 110)
            Button(window3, text = 'ONE FULL DAY', font = "times", bg = "light pink", padx = 37, pady = 0, command = slot_f).place(x = 225, y = 140)

            #Flexible Time Slot
            label = Label(window3, text = ("Park", "Xpert"), font = ("times", 25, 'bold'), bg = "light blue", fg = "maroon").place(x = 350,  y = 0)
            label = Label(window3, text = ("Fixed", "Time","Slots", ":"), font = ("times", 16, 'bold'), bg = "light blue", fg = "maroon").place(x = 30,  y = 100)
            label = Label(window3, text = ("Flexible", "Time","Slots", ":"), font = ("times", 16, 'bold'), bg = "light blue", fg = "maroon").place(x = 30, y = 275)
            label = Label(window3, text = ( "(", "7", "a.m", "-","10", "p.m", ")"), font = ("times", 16, 'bold'), bg = "light blue", fg = "maroon").place(x = 30, y = 300)
            label = Label(window3, text = ("Car/hr", ":", "Rs","50"), font = ("times", 16, 'bold'), bg = "light blue", fg = "maroon").place(x = 475, y = 250)
            label = Label(window3, text = ("Bike/hr", ":", "Rs", "30"), font = ("times", 16, 'bold'), bg = "light blue", fg = "maroon").place(x = 475, y = 300)

            global ehrs, emins, entry_hvar, entry_mvar, xhr, xmi, exit_hvar, exit_mvar
            ehrs = StringVar(window3)
            ehrs.set("Entry hr")
            emins = StringVar(window3)
            emins.set("Entry mins")
            entry_hvar = StringVar(window3)
            entry_mvar = StringVar(window3)

            xhr = StringVar(window3)
            xhr.set("Exit hr  ")
            xmi = StringVar(window3)
            xmi.set("Exit mins   ")
            exit_hvar = StringVar(window3)
            exit_mvar = StringVar(window3)

            def flex_slot():
                window3.destroy()
                window2 = Tk()
                window2.title('FLEXIBLE SLOTS')
                window2.configure(bg = "light blue")
                window2.geometry('1200x700')
                LocationLabel = Label(window2, text = "Type Of Vehicle", font = ("times", 20), bg = "light blue").grid(row = 18, column = 0)
                def billing():
                    window2.destroy()
                    window4 = Tk()
                    window4.title('BILLING')
                    window4.configure(bg = "light blue")
                    window4.geometry('745x600')
                    mycur.execute('Select name from signup where username = %s', (phno,))
                    name = mycur.fetchall()

                    # Calculation of the number of hrs
                    if entry_hvar == exit_hvar:
                        diff_hr = 1
                    else:
                        diff_hr = exit_hvar - entry_hvar
                        if (exit_mvar - entry_mvar) > 0:
                            diff_hr += 1

                    # Calculation on Number of Vehicles booked    
                    mycur.execute('Select * from booking where username = %s and paid = %s', (phno, 'Unpaid'))
                    a = mycur.fetchall()
                    amt = c_count = b_count = 0
                    for i in a:
                        if i[1] == 'Car':
                            c_count += 1
                        else:
                            b_count += 1

                    # Final amount on the number of hrs
                    amt = c_count * diff_hr * 50 + b_count * diff_hr * 30
                    
                    ig = PhotoImage(file = "C:/Users/sahan/OneDrive/Desktop/ParkXpert/ty.png")
                    window4.ig = ig
                    l = Label(window4, image = ig)
                    l.place(x = 0, y = 0)
                    t = []
                    for i in a:
                        t.append(i[1])
                    x_len = X_len = 0
                    if 'Car' in t and 'Bike' in t:
                        label = Label(window4, text = ("Car", ":"), font = ("times", 16, 'bold'), bg = "light blue", fg = "black").place(x = 125, y = 320)
                        x_len = 125
                        label = Label(window4, text = ("Bike", ":"), font = ("times", 16, 'bold'), bg = "light blue", fg = "black").place(x = 125, y = 350)
                        X_len = 125
                    elif 'Car' in t:
                        label = Label(window4, text = ("Car", ":"), font = ("times", 16, 'bold'), bg = "light blue", fg = "black").place(x = 125, y = 320)
                        x_len = 125
                    elif 'Bike' in t:
                        label = Label(window4, text = ("Bike", ":"), font = ("times", 16, 'bold'), bg = "light blue", fg = "black").place(x = 125, y = 350)
                        X_len = 125
                    else:
                        label = Label(window4, text = ("No", "Slot", "is", "booked"), font = ("times", 16, 'bold'), bg = "light blue", fg = "maroon").place(x = 100, y = 300)

                    for i in a:
                        if i[1] == 'Car':
                            x_len += 50
                            label = Label(window4, text = (i[2]), font = ("times", 16, 'italic'), bg = "light blue", fg = "black").place(x = x_len, y = 320)
                        else:
                            X_len += 50
                            label = Label(window4, text = (i[2]), font = ("times", 16, 'italic'), bg = "light blue", fg = "black").place(x = X_len, y = 350)

                    label = Label(window4, text = ("Park", "Xpert"), font = ("times", 25, 'bold'), bg = "light blue", fg = "maroon").place(x = 300,  y = 240)
                    label = Label(window4, text = ("Booked", "Slots", ":"), font = ("times", 16, 'bold'), bg = "light blue", fg = "maroon").place(x = 100, y = 275)
                    label = Label(window4, text = ("Name", ":",  name), font = ("times", 16, 'bold'), bg = "light blue", fg = "maroon").place(x = 100,  y = 400)                   
                    label = Label(window4, text = ("Entry", "Time", ":", entry_hvar,":", entry_mvar), font = ("times", 16, 'bold'), bg = "light blue", fg = "maroon").place(x = 100, y = 425)
                    label = Label(window4, text = ("Exit", "Time", ":", exit_hvar,":", exit_mvar), font = ("times", 16, 'bold'), bg = "light blue", fg = "maroon").place(x = 100, y = 450)
                    label = Label(window4, text = ("Amount", ":", "Rs", amt), font = ("times", 16, 'italic'), bg = "light green", fg = "black", relief = RAISED).place(x = 100, y = 500)
                    label = Label(window4, text = "Thanks for visiting, HAPPY PARKING", font = ("times", 16, 'italic'), bg = "light green", fg = "black", relief = RAISED).place(x = 100, y = 525)
                    mycur.execute('Update booking set paid = %s where username = %s and paid = %s', ('Paid', phno, 'Unpaid'))
                    mycon.commit()

                def book1(v, j):
                    Button(window2, text = ('Slot ', v), bg = 'red', padx = 20, pady = 20).place(x = 100 * j, y = 100)
                    mycur.execute('insert into booking(username, type, slot, time) values(%s, %s, %s, %s)', (phno, 'Car', v, 'F'))
                    mycon.commit()
                    mycur.execute('Update flexi_slot set Avl = %s where slot = %s and type = %s', ('B', v, 'Car'))
                    mycon.commit()

                def book2(v, j):
                    Button(window2, text = ('Slot ', v), bg = 'red', padx = 20, pady = 20).place(x = 100 * j, y = 175)
                    mycur.execute('insert into booking(username, type, slot, time) values(%s, %s, %s, %s)', (phno, 'Car', v, 'F'))
                    mycon.commit()
                    mycur.execute('Update flexi_slot set Avl = %s where slot = %s and type = %s', ('B', v, 'Car'))
                    mycon.commit()

                def book3(v, j):
                    Button(window2, text = ('Slot ', v), bg = 'red', padx = 20, pady = 20).place(x = 100 * j, y = 250)
                    mycur.execute('insert into booking(username, type, slot, time) values(%s, %s, %s, %s)', (phno, 'Car', v, 'F'))
                    mycon.commit()
                    mycur.execute('Update flexi_slot set Avl = %s where slot = %s and type = %s', ('B', v, 'Car'))
                    mycon.commit()

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
                    mycur.execute('insert into booking(username, type, slot, time) values(%s, %s, %s, %s)', (phno, 'Bike', v, 'F'))
                    mycon.commit()
                    mycur.execute('Update flexi_slot set Avl = %s where slot = %s and type = %s', ('B', v, 'Bike'))
                    mycon.commit()

                def book5(v, j):
                    Button(window2, text = ('Slot ', v), bg = 'red', padx = 20, pady = 20).place(x = 100 * j, y = 475)
                    mycur.execute('insert into booking(username, type, slot, time) values(%s, %s, %s, %s)', (phno, 'Bike', v, 'F'))
                    mycon.commit()
                    mycur.execute('Update flexi_slot set Avl = %s where slot = %s and type = %s', ('B', v, 'Bike'))
                    mycon.commit()

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

                #To re-establish the red boxes of already booked slots
                mycur.execute("select * from flexi_slot where Avl = 'B'")
                tupl = mycur.fetchall()
                for i in tupl:
                    if i[0] == 'Car':
                        if i[1] <= 10:
                            Button(window2, text = ('Slot ', i[1]), bg = 'red', padx = 20, pady = 20, state = DISABLED).place(x = i[1] * 100, y = 100)
                        elif i[1] <= 20:
                            d = i[1] % 10
                            if d == 0:
                                Button(window2, text = ('Slot ', i[1]), bg = 'red', padx = 20, pady = 20, state = DISABLED).place(x = 10 * 100, y = 175)
                            else:
                                Button(window2, text = ('Slot ', i[1]), bg = 'red', padx = 20, pady = 20, state = DISABLED).place(x = d * 100, y = 175)
                        else:
                            d = i[1] % 10
                            if d == 0:
                                Button(window2, text = ('Slot ', i[1]), bg = 'red', padx = 20, pady = 20, state = DISABLED).place(x = 10 * 100, y = 250)
                            else:
                                Button(window2, text = ('Slot ', i[1]), bg = 'red', padx = 20, pady = 20, state = DISABLED).place(x = d * 100, y = 250)
                    else:
                        if i[1] <= 10:
                            Button(window2, text = ('Slot ', i[1]), bg = 'red', padx = 20, pady = 20, state = DISABLED).place(x = i[1] * 100, y = 400)
                        else:
                            d = i[1] % 10
                            if d == 0:
                                Button(window2, text = ('Slot ', i[1]), bg = 'red', padx = 20, pady = 20, state = DISABLED).place(x = 10 * 100, y = 475)
                            else:
                                Button(window2, text = ('Slot ', i[1]), bg = 'red', padx = 20, pady = 20, state = DISABLED).place(x = d * 100, y = 475)

                Button(window2, text = 'Car', font = "times", bg = "light pink").place(x = 25, y = 200)
                Button(window2, text = 'Bike', font = "times", bg = "light pink").place(x = 25, y = 450)
                Button(window2, text = 'Proceed to Payment', font = "times", bg = "light pink", command = billing).place(x = 500, y = 600)

            def entryh(h_ent):
                global entry_hvar
                entry_hvar = (int) (h_ent)
                print(entry_hvar)

            def entrym(m_ent):
                global entry_mvar
                entry_mvar = (int) (m_ent)
                print(entry_hvar, entry_mvar)

            def exith(h_exi):
                global exit_hvar
                exit_hvar = (int) (h_exi)
                print(exit_hvar)

            def exitm(m_exi):
                global exit_mvar
                exit_mvar = (int) (m_exi)
                print(exit_hvar, exit_mvar)
                if entry_hvar > exit_hvar:
                    messagebox.showerror("showerror", "Exit time should be greater than entry time")
                elif (entry_hvar == exit_hvar) and (entry_mvar >=  exit_mvar):
                    messagebox.showerror("showerror", "Exit time should be greater than entry time")
                else:
                    flex_slot()

            entry_h = OptionMenu(window3, ehrs, "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", command = entryh)
            entry_h.configure(bg = "cyan", font = ("times", 13))
            entry_h.place(x = 225, y = 250)

            entry_m = OptionMenu(window3, emins,"5", "10", "15", "20", "25", "30", "35", "40", "45", "50", "55", "00", command = entrym)
            entry_m.configure(bg = "aqua", font = ("times", 13))
            entry_m.place(x = 330, y = 250)

            exit_h = OptionMenu(window3, xhr,"8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22",  command = exith)
            exit_h.configure(bg = "cyan", font = ("times", 13))
            exit_h.place(x = 225, y = 300)

            exit_m = OptionMenu(window3, xmi, "5", "10", "15", "20", "25", "30", "35", "40", "45", "50", "55", "00", command = exitm)
            exit_m.configure(bg = "aqua", font = ("times", 13))
            exit_m.place(x = 330, y = 300)
            #Flexible Time Slot ends

        phno = username.get()
        pwd = password.get()
        mycur.execute('select username from signup')
        users = mycur.fetchall()
        mycur.execute('select username, password from signup')
        lpwd = mycur.fetchall()
        len_users = len(users)
        count = 0
        for i in users:
            if phno != str(i[0]):
                count += 1
            else:
                continue

        if count == len_users or not((str)(phno)).isdigit():
            messagebox.showerror("showerror", "Invalid Username, Enter valid 10 digit Mobile number")
            username.delete(0, END)
            password.delete(0, END)
        else:
            for i in lpwd:
                if phno != str(i[0]):
                    continue
                else:
                    if pwd != i[1]:
                        messagebox.showerror("showerror", "Invalid Password, Try again!")
                        password.delete(0, END)
                    else:
                        mes()

    label = Label(window1, text = "Username ", font = ("times", 16), bg = "light blue")
    label.place(x = 10, y = 20)
    username = Entry(window1, width = 40)
    username.pack(pady = 20)

    label = Label(window1, text = "Password", font = ("times", 16), bg = "light blue")
    label.place(x = 10, y = 75)
    password = Entry(window1, width = 40, show = '*')
    password.pack(pady = 20)

    #confirm button
    button = Button(window1, text = 'Confirm', command = con)
    button.pack(pady = 10)

#--------------------------------------------------------#
#                 program starts here
#--------------------------------------------------------#
mycon = mysql.connector.connect(host = 'localhost', user = 'root', password = 'abcd', database = 'parking')
mycur = mycon.cursor()

window = Tk()
window.title('ParkXpert')
window.configure(bg = "light blue")
window.geometry('800x500')
username = 0
password = 0
p1 = PhotoImage(file = 'C:/Users/sahan/OneDrive/Desktop/ParkXpert/ph.png')
window.iconphoto(True, p1)

canvas = Canvas(window, width = 1500, height = 1500, bg = "light blue")
canvas.pack()
img = PhotoImage(file = "C:/Users/sahan/OneDrive/Desktop/ParkXpert/car.png")
canvas.create_image(10, 10, anchor = NW, image = img)
label = Label(window, text = "Welcome to ", font = ("times", 25), bg = "light blue")
label.place(x = 550, y = 100)
label = Label(window, text = "CAJC ParkXpert", font = ("times", 23), bg = "light blue")
label.place(x = 530, y = 140)
label = Label(window, text = "No more running in circles", font = ("times", 18, 'italic'), bg = "light blue", fg = "maroon")
label.place(x = 500, y = 300)
label = Label(window, text = "to find parking", font = ("times", 18, 'italic'), bg = "light blue", fg = "maroon")
label.place(x = 550, y = 330)
'''label = Label(window, text = "Book one day in advance", font = ("times", 18, 'italic'), bg = "light blue", fg = "maroon")
label.place(x = 510, y = 380)'''
Button(window, text = 'Login', font = ("times", 15), bg = "light pink", width = 13, command = login).place(x = 560, y = 210)
Button(window, text = 'New User? SignUp', font = ("times", 15), bg = "light pink", command = register).place(x = 625, y = 5)
window.mainloop()
