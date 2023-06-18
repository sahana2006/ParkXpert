from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import mysql.connector
import datetime
#from datetime import datetime
import time

global exitdt
global curr_time, curr_date
#Login Credentials
def entry():
    global entrydt
    window1 = Tk()
    window1.title('Login')
    window1.configure(bg = "light blue")
    window1.geometry('500x400')
    def submit():
            def slot():
                window2 = Tk()
                window2.title('SLOTS')
                window2.configure(bg = "light blue")
                window2.geometry('1200x700')
                LocationLabel = Label(window2, text = "Type Of Vehicle", font = ("times", 20), bg = "light blue").grid(row = 18, column = 0)
                def nxt():
                    window2.destroy()
                    window3 = Tk()
                    window3.title('RECEIPT')
                    window3.configure(bg = "light blue")
                    window3.geometry('500x450')
                    mycur.execute('select vehicle, mobno, name, type, slot,entry_date_time from details where vehicle = %s', (vno,))
                    t = mycur.fetchall()
                    e_split = (str)(t[0][5]).split()
                    label = Label(window3, text = "CACJ PARK XPERT", font = ("times", 14), bg = "light blue")
                    label.place(x = 300, y = 0)
                    label = Label(window3, text = "Hullahalli, Begur - Koppa Road", font = ("times", 10), bg = "light blue")
                    label.place(x = 300, y = 20)
                    label = Label(window3, text = "Bengaluru - 560083", font = ("times", 10), bg = "light blue")
                    label.place(x = 300, y = 40)
                    label = Label(window3, text = "------------------------------------------------------------", font = ("times", 16), bg = "light blue")
                    label.place(x = 50, y = 60)
                    label = Label(window3, text = "Entry Receipt", font = ("times", 18), bg = "light blue", fg = "maroon")
                    label.place(x = 200, y = 80)
                    label = Label(window3, text = "------------------------------------------------------------", font = ("times", 16), bg = "light blue")
                    label.place(x = 50, y = 110)
                    label = Label(window3, text = ("Name:", t[0][2]), font = ("times", 16), bg = "light blue")
                    label.place(x = 100, y = 135)
                    label = Label(window3, text = ("Vehicle", "No:", t[0][0]), font = ("times", 16), bg = "light blue")
                    label.place(x = 100, y = 160)
                    label = Label(window3, text = ("Mobile", "No:", t[0][1]), font = ("times", 16), bg = "light blue")
                    label.place(x = 100, y = 185)
                    label = Label(window3, text = ("Type:", t[0][3]), font = ("times", 16), bg = "light blue")
                    label.place(x = 100, y = 210)
                    label = Label(window3, text = ("Slot:", t[0][4]), font = ("times", 16), bg = "light blue")
                    label.place(x = 100, y = 235)
                    label = Label(window3, text = ("From:", e_split[0],"/", e_split[1]), font = ("times", 16), bg = "light blue")
                    label.place(x = 100, y = 260)
                    label = Label(window3, text = "HAPPY PARKING!", font = ("times", 20), bg = "light blue", fg = "maroon")
                    label.place(x = 100, y = 320)

                def disable(v, ty):
                    cars = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
                    bike = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
                    if ty == 'Car':
                        cars.remove(v)
                    else:
                        bike.remove(v)
                    for i in cars:
                        if 1 <= i <= 10:
                            Button(window2, text = ('Slot ', i), bg = 'grey', padx = 20, pady = 20, state = DISABLED).place(x = 100 * i, y = 100)
                        elif 11 <= i <= 20:
                            Button(window2, text = ('Slot ', i), bg = 'grey', padx = 20, pady = 20, state = DISABLED).place(x = 100 * (i - 10), y = 175)
                        else:
                            Button(window2, text = ('Slot ', i), bg = 'grey', padx = 20, pady = 20, state = DISABLED).place(x = 100 * (i - 20), y = 250)
                    for i in bike:
                        if 1 <= i <= 10:
                            Button(window2, text = ('Slot ', i), bg = 'grey', padx = 20, pady = 20, state = DISABLED).place(x = 100 * i, y = 400)
                        else:
                            Button(window2, text = ('Slot ', i), bg = 'grey', padx = 20, pady = 20, state = DISABLED).place(x = 100 * (i - 10), y = 475)

                def book1(v, j):
                    from datetime import timedelta
                    global entrydt
                    entrydt = datetime.datetime.now()
                    Button(window2, text = ('Slot ', v), bg = 'red', padx = 20, pady = 20).place(x = 100 * j, y = 100)
                    mycur.execute('insert into details(vehicle, mobno, name, type, slot, entry_date_time) values(%s, %s, %s, %s, %s, %s)', (vno, mno, nm, 'Car', v, entrydt))
                    mycon.commit()
                    mycur.execute('Update vehicle_slots set Avl = %s where slot = %s and type = %s', ('B', v, 'Car'))
                    mycon.commit()
                    disable(v, 'Car')

                def book2(v, j):
                    from datetime import timedelta
                    global entrydt
                    entrydt = datetime.datetime.now()
                    Button(window2, text = ('Slot ', v), bg = 'red', padx = 20, pady = 20).place(x = 100 * j, y = 175)
                    mycur.execute('insert into details(vehicle, mobno, name, type, slot, entry_date_time) values(%s, %s, %s, %s, %s, %s)', (vno, mno, nm, 'Car', v, entrydt))
                    mycon.commit()
                    mycur.execute('Update vehicle_slots set Avl = %s where slot = %s and type = %s', ('B', v, 'Car'))
                    mycon.commit()
                    disable(v, 'Car')

                def book3(v, j):
                    from datetime import timedelta
                    global entrydt
                    entrydt = datetime.datetime.now()
                    Button(window2, text = ('Slot ', v), bg = 'red', padx = 20, pady = 20).place(x = 100 * j, y = 250)
                    mycur.execute('insert into details(vehicle, mobno, name, type, slot, entry_date_time) values(%s, %s, %s, %s, %s, %s)', (vno, mno, nm, 'Car', v, entrydt))
                    mycon.commit()
                    mycur.execute('Update vehicle_slots set Avl = %s where slot = %s and type = %s', ('B', v, 'Car'))
                    mycon.commit()
                    disable(v, 'Car')

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
                    from datetime import timedelta
                    global entrydt
                    entrydt = datetime.datetime.now()
                    Button(window2, text = ('Slot ', v), bg = 'red', padx = 20, pady = 20).place(x = 100 * j, y = 400)
                    mycur.execute('insert into details(vehicle, mobno, name, type, slot, entry_date_time) values(%s, %s, %s, %s, %s, %s)', (vno, mno, nm, 'Bike', v, entrydt))
                    mycon.commit()
                    mycur.execute('Update vehicle_slots set Avl = %s where slot = %s and type = %s', ('B', v, 'Bike'))
                    mycon.commit()
                    disable(v, 'Bike')

                def book5(v, j):
                    from datetime import timedelta
                    global entrydt
                    entrydt = datetime.datetime.now()
                    Button(window2, text = ('Slot ', v), bg = 'red', padx = 20, pady = 20).place(x = 100 * j, y = 475)
                    mycur.execute('insert into details(vehicle, mobno, name, type, slot, entry_date_time) values(%s, %s, %s, %s, %s, %s)', (vno, mno, nm, 'Bike', v, entrydt))
                    mycon.commit()
                    mycur.execute('Update vehicle_slots set Avl = %s where slot = %s and type = %s', ('B', v, 'Bike'))
                    mycon.commit()
                    disable(v, 'Bike')

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
                mycur.execute("select * from vehicle_slots where Avl = 'B'")
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
                Button(window2, text = 'Next', font = "times", bg = "light pink",command=nxt).place(x = 580, y = 580)

            vno = vehicleno.get()
            mno = mobileno.get()
            nm = name.get()
            l_vno = len(vno)
            mycur.execute('select vehicle from details')
            users = mycur.fetchall()
            len_users = len(users)
            count = 0
            for i in users:
                if vno == str(i[0]):
                    count = 1
                    break
            if count == 1 :
                messagebox.showerror("showerror", "Vehicle Number already registered, Use different Vehicle Number")
                vehicleno.delete(0, END)
                mobileno.delete(0, END)
                name.delete(0, END)
            elif len(mno) != 10 or not(mno).isdigit():
                messagebox.showerror("showerror", "Invalid Mobile Number, Enter valid 10 digit Mobile Number")
                vehicleno.delete(0, END)
                mobileno.delete(0, END)
                name.delete(0, END)
            elif l_vno != 10:
                messagebox.showerror("showerror", "Invalid Vehicle Number")
                vehicleno.delete(0, END)
            elif not(vno[2].isdigit() and vno[3].isdigit() and vno[6].isdigit() and vno[7].isdigit() and vno[8].isdigit() and vno[9].isdigit()):
                messagebox.showerror("showerror", "Invalid Vehicle Number")
                vehicleno.delete(0, END)
            elif vno[0:2] not in('AP', 'AR', 'AS', 'BR','CG', 'GA', 'GJ','HR', 'HP', 'JH', 'KA','KL', 'MP', 'MH', 'MN', 'ML', 'MZ', 'NL', 'OD', 'PB', 'RJ', 'SK', 'TN', 'TS', 'TR', 'UP', 'UK', 'WB'):
                messagebox.showerror("showerror", "Invalid Vehicle Number")
                vehicleno.delete(0, END)
            elif not(vno[4].isalpha() and vno[5].isalpha() and vno[4].isupper() and vno[5].isupper()):
                messagebox.showerror("showerror", "Invalid Vehicle Number")
                vehicleno.delete(0, END)
            else:
                messagebox.showinfo("Message", "You have logged in successfully")
                window1.destroy()
                slot()

    label = Label(window1, text = "Vehicle No", font = ("times", 16), bg = "light blue")
    label.place(x = 10, y = 20)
    label = Label(window1, text = "Mobile No", font = ("times", 16), bg = "light blue")
    label.place(x = 10, y = 75)
    label = Label(window1, text = "Name", font = ("times", 16), bg = "light blue")
    label.place(x = 10, y = 130)

    vehicleno = Entry(window1, width = 40)
    vehicleno.pack(pady = 20)

    mobileno = Entry(window1, width = 40)
    mobileno.pack(pady = 20)

    name = Entry(window1, width = 40)
    name.pack(pady = 20)

    button = Button(window1, text = 'Submit', command = submit)
    button.pack(pady = 10)

def exitt():
    window1 = Tk()
    window1.title('Logout')
    window1.configure(bg = "light blue")
    window1.geometry('500x200')
    def submit():
        def recipt():
            window3 = Tk()
            window3.title('Parking Recipt')
            window3.configure(bg = "light blue")
            window3.geometry('500x450')
            window1.destroy()
            mycur.execute('select vehicle, mobno, name, type, slot,entry_date_time, exit_date_time from details where vehicle = %s', (vno,))
            t = mycur.fetchall()
            e_split = (str)(t[0][5]).split()
            x_split = (str)(t[0][6]).split()
            label = Label(window3, text = "CACJ PARK XPERT", font = ("times", 14), bg = "light blue")
            label.place(x = 300, y = 0)
            label = Label(window3, text = "Hullahalli, Begur - Koppa Road", font = ("times", 10), bg = "light blue")
            label.place(x = 300, y = 20)
            label = Label(window3, text = "Bengaluru - 560083", font = ("times", 10), bg = "light blue")
            label.place(x = 300, y = 40)
            label = Label(window3, text = "------------------------------------------------------------", font = ("times", 16), bg = "light blue")
            label.place(x = 50, y = 60)
            label = Label(window3, text = "Parking Receipt", font = ("times", 18), bg = "light blue", fg = "maroon")
            label.place(x = 200, y = 80)
            label = Label(window3, text = "------------------------------------------------------------", font = ("times", 16), bg = "light blue")
            label.place(x = 50, y = 110)
            label = Label(window3, text = ("Name:", t[0][2]), font = ("times", 16), bg = "light blue")
            label.place(x = 100, y = 135)
            label = Label(window3, text = ("Vehicle", "No:", t[0][0]), font = ("times", 16), bg = "light blue")
            label.place(x = 100, y = 160)
            label = Label(window3, text = ("Mobile", "No:", t[0][1]), font = ("times", 16), bg = "light blue")
            label.place(x = 100, y = 185)
            label = Label(window3, text = ("Type:", t[0][3]), font = ("times", 16), bg = "light blue")
            label.place(x = 100, y = 210)
            label = Label(window3, text = ("Slot:", t[0][4]), font = ("times", 16), bg = "light blue")
            label.place(x = 100, y = 235)
            label = Label(window3, text = ("From:", e_split[0],"/", e_split[1]), font = ("times", 16), bg = "light blue")
            label.place(x = 100, y = 260)
            label = Label(window3, text = ("To:", x_split[0], "/", x_split[1]), font = ("times", 16), bg = "light blue")
            label.place(x = 100, y = 290)
            label = Label(window3, text =("Amount:Rs", amt), font = ("times", 16), bg = "light blue")
            label.place(x = 100, y = 320)
            label = Label(window3, text = "THANK YOU AND DRIVE SAFELY!", font = ("times", 20), bg = "light blue", fg = "maroon")
            label.place(x = 50, y = 360)
            #Refreshing the slot which will become free
            mycur.execute('update vehicle_slots set avl = %s where type = %s and slot =%s', ('U', t[0][3], t[0][4]))
            mycon.commit()
            mycur.execute('delete from details where vehicle = %s', (t[0][0],))
            mycon.commit()

        vno = vehicleno.get()
        mycur.execute('select vehicle from details where vehicle = %s', (vno,))
        vehicle_list = mycur.fetchall()
        if vehicle_list != []:
            exitdt = datetime.datetime.now()
            mycur.execute('update details set exit_date_time = %s where vehicle = %s', (exitdt, vno))
            mycon.commit()
            mycur.execute('select entry_date_time,type from details where vehicle = %s', (vno,))
            ty = mycur.fetchall()
            diff = exitdt - ty[0][0]
            #Separation of date and time by using split function
            s = (str)(diff).split()
            s_len = len(s)
            amt = 0
            #Amount with only time
            if s_len == 1:
                s = (str)(diff).split(':')
                if ty[0][1] == 'Car':
                    amt += (int)(s[0])*30 + (int)(s[1])//2
                else:
                    amt += (int)(s[0])*15 + (int)(s[1])//4
            #Amount with days and time
            else:
                if ty[0][1] == 'Car':
                    amt += (int)(s[0])*720
                else:
                    amt += (int)(s[0])*360
                s = (str)(s[2]).split(':')
                if ty[0][1] == 'Car':
                    amt += (int)(s[0])*30 + (int)(s[1])//2
                else:
                    amt += (int)(s[0])*15 + (int)(s[1])//4
            recipt()
        else:
            messagebox.showinfo("Message", "Enter Valid Vehicle no")
            vehicleno.delete(0, END)

    label = Label(window1, text = "Vehicle No", font = ("times", 16), bg = "light blue")
    label.place(x = 10, y = 20)

    vehicleno = Entry(window1, width = 40)
    vehicleno.pack(pady = 20)

    button = Button(window1, text = 'Submit', command = submit)
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
global entrydt
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
label = Label(window, text = "Car per hour Rs30", font = ("times", 18, 'italic'), bg = "light blue", fg = "black")
label.place(x = 520, y = 380)
label = Label(window, text = "Bike per hour Rs15", font = ("times", 18, 'italic'), bg = "light blue", fg = "black")
label.place(x = 520, y = 410)
Button(window, text = 'Entry', font = ("times", 15), bg = "light pink", width = 5, command = entry).place(x = 560, y = 210)
Button(window, text = 'Exit', font = ("times", 15), bg = "light pink",  width = 5, command = exitt).place(x = 650, y = 210)
window.mainloop()
