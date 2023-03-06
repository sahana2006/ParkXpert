from tkinter import *
from tkinter import messagebox

def Slot_Car():
    window1 = Tk()
    window1.title('CAR SLOTS')
    window1.geometry('1200x500')
    window1.configure(bg = "light pink")
    label = Label(window1, text = "Availability Slots For Car", font = "times 28 bold", bg = 'light pink')
    label.place(x = 100, y = 25)

    def Close():
        window1.destroy()

    def disable(v):
        a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]
        a.remove(v)
        for i in a:
            if 1 <= i <= 10:
                Button(window1, text = ('Slot ', i), bg = 'grey', padx = 20, pady = 20, state = DISABLED).place(x = 100 * i, y = 100)
            elif 11 <= i <= 20:
                Button(window1, text = ('Slot ', i), bg = 'grey', padx = 20, pady = 20, state = DISABLED).place(x = 100 * (i - 10), y = 175)
            elif 21 <= i <= 30:
                Button(window1, text = ('Slot ', i), bg = 'grey', padx = 20, pady = 20, state = DISABLED).place(x = 100 * (i - 20), y = 250)
            elif 31 <= i <= 40:
                Button(window1, text = ('Slot ', i), bg = 'grey', padx = 20, pady = 20, state = DISABLED).place(x = 100 * (i - 30), y = 325)
            else:
                Button(window1, text = ('Slot ', i), bg = 'grey', padx = 20, pady = 20, state = DISABLED).place(x = 100 * (i - 40), y = 400)
        Button(window1, text = "Your Slot Is Booked, Click Me to Confirm", padx = 50, pady = 20, bg = 'light yellow', font = "calibri 10 bold", command = Close).place(x = 800, y = 25)

    def book1(v, j):
        Button(window1, text = ('Slot ', v), bg = 'red', padx = 20, pady = 20).place(x = 100 * j, y = 100)
        disable(v)

    def book2(v, j):
        Button(window1, text = ('Slot ', v), bg = 'red', padx = 20, pady = 20).place(x = 100 * j, y = 175)
        disable(v)

    def book3(v, j):
        Button(window1, text = ('Slot ', v), bg = 'red', padx = 20, pady = 20).place(x = 100 * j, y = 250)
        disable(v)

    def book4(v, j):
        Button(window1, text = ('Slot ', v), bg = 'red', padx = 20, pady = 20).place(x = 100 * j, y = 325)
        disable(v)

    def book5(v, j):
        Button(window1, text = ('Slot ', v), bg = 'red', padx = 20, pady = 20).place(x = 100 * j, y = 400)
        disable(v)

    i = 1; xlen = 20; ylen = 20; xloc = 100; yloc = 100
    Button(window1, text = ('Slot ', i), bg = 'light green', padx = xlen, pady = ylen, command = lambda:book1( 1,  1)).place(x = xloc, y = yloc); i += 1; xloc += 100
    Button(window1, text = ('Slot ', i), bg = 'light green', padx = xlen, pady = ylen, command = lambda:book1( 2,  2)).place(x = xloc, y = yloc); i += 1; xloc += 100
    Button(window1, text = ('Slot ', i), bg = 'light green', padx = xlen, pady = ylen, command = lambda:book1( 3,  3)).place(x = xloc, y = yloc); i += 1; xloc += 100
    Button(window1, text = ('Slot ', i), bg = 'light green', padx = xlen, pady = ylen, command = lambda:book1( 4,  4)).place(x = xloc, y = yloc); i += 1; xloc += 100
    Button(window1, text = ('Slot ', i), bg = 'light green', padx = xlen, pady = ylen, command = lambda:book1( 5,  5)).place(x = xloc, y = yloc); i += 1; xloc += 100
    Button(window1, text = ('Slot ', i), bg = 'light green', padx = xlen, pady = ylen, command = lambda:book1( 6,  6)).place(x = xloc, y = yloc); i += 1; xloc += 100
    Button(window1, text = ('Slot ', i), bg = 'light green', padx = xlen, pady = ylen, command = lambda:book1( 7,  7)).place(x = xloc, y = yloc); i += 1; xloc += 100
    Button(window1, text = ('Slot ', i), bg = 'light green', padx = xlen, pady = ylen, command = lambda:book1( 8,  8)).place(x = xloc, y = yloc); i += 1; xloc += 100
    Button(window1, text = ('Slot ', i), bg = 'light green', padx = xlen, pady = ylen, command = lambda:book1( 9,  9)).place(x = xloc, y = yloc); i += 1; xloc += 100
    Button(window1, text = ('Slot ', i), bg = 'light green', padx = xlen, pady = ylen, command = lambda:book1(10, 10)).place(x = xloc, y = yloc); i += 1;

    xloc = 100; yloc = 175
    Button(window1, text = ('Slot ', i), bg = 'light green', padx = xlen, pady = ylen, command = lambda:book2(11,  1)).place(x = xloc, y = yloc); i += 1; xloc += 100
    Button(window1, text = ('Slot ', i), bg = 'light green', padx = xlen, pady = ylen, command = lambda:book2(12,  2)).place(x = xloc, y = yloc); i += 1; xloc += 100
    Button(window1, text = ('Slot ', i), bg = 'light green', padx = xlen, pady = ylen, command = lambda:book2(13,  3)).place(x = xloc, y = yloc); i += 1; xloc += 100
    Button(window1, text = ('Slot ', i), bg = 'light green', padx = xlen, pady = ylen, command = lambda:book2(14,  4)).place(x = xloc, y = yloc); i += 1; xloc += 100
    Button(window1, text = ('Slot ', i), bg = 'light green', padx = xlen, pady = ylen, command = lambda:book2(15,  5)).place(x = xloc, y = yloc); i += 1; xloc += 100
    Button(window1, text = ('Slot ', i), bg = 'light green', padx = xlen, pady = ylen, command = lambda:book2(16,  6)).place(x = xloc, y = yloc); i += 1; xloc += 100
    Button(window1, text = ('Slot ', i), bg = 'light green', padx = xlen, pady = ylen, command = lambda:book2(17,  7)).place(x = xloc, y = yloc); i += 1; xloc += 100
    Button(window1, text = ('Slot ', i), bg = 'light green', padx = xlen, pady = ylen, command = lambda:book2(18,  8)).place(x = xloc, y = yloc); i += 1; xloc += 100
    Button(window1, text = ('Slot ', i), bg = 'light green', padx = xlen, pady = ylen, command = lambda:book2(19,  9)).place(x = xloc, y = yloc); i += 1; xloc += 100
    Button(window1, text = ('Slot ', i), bg = 'light green', padx = xlen, pady = ylen, command = lambda:book2(20, 10)).place(x = xloc, y = yloc); i += 1;

    xloc = 100; yloc = 250
    Button(window1, text = ('Slot ', i), bg = 'light green', padx = xlen, pady = ylen, command = lambda:book3(21,  1)).place(x = xloc, y = yloc); i += 1; xloc += 100
    Button(window1, text = ('Slot ', i), bg = 'light green', padx = xlen, pady = ylen, command = lambda:book3(22,  2)).place(x = xloc, y = yloc); i += 1; xloc += 100
    Button(window1, text = ('Slot ', i), bg = 'light green', padx = xlen, pady = ylen, command = lambda:book3(23,  3)).place(x = xloc, y = yloc); i += 1; xloc += 100
    Button(window1, text = ('Slot ', i), bg = 'light green', padx = xlen, pady = ylen, command = lambda:book3(24,  4)).place(x = xloc, y = yloc); i += 1; xloc += 100
    Button(window1, text = ('Slot ', i), bg = 'light green', padx = xlen, pady = ylen, command = lambda:book3(25,  5)).place(x = xloc, y = yloc); i += 1; xloc += 100
    Button(window1, text = ('Slot ', i), bg = 'light green', padx = xlen, pady = ylen, command = lambda:book3(26,  6)).place(x = xloc, y = yloc); i += 1; xloc += 100
    Button(window1, text = ('Slot ', i), bg = 'light green', padx = xlen, pady = ylen, command = lambda:book3(27,  7)).place(x = xloc, y = yloc); i += 1; xloc += 100
    Button(window1, text = ('Slot ', i), bg = 'light green', padx = xlen, pady = ylen, command = lambda:book3(28,  8)).place(x = xloc, y = yloc); i += 1; xloc += 100
    Button(window1, text = ('Slot ', i), bg = 'light green', padx = xlen, pady = ylen, command = lambda:book3(29,  9)).place(x = xloc, y = yloc); i += 1; xloc += 100
    Button(window1, text = ('Slot ', i), bg = 'light green', padx = xlen, pady = ylen, command = lambda:book3(30, 10)).place(x = xloc, y = yloc); i += 1;

    xloc = 100; yloc = 325
    Button(window1, text = ('Slot ', i), bg = 'light green', padx = xlen, pady = ylen, command = lambda:book4(31,  1)).place(x = xloc, y = yloc); i += 1; xloc += 100
    Button(window1, text = ('Slot ', i), bg = 'light green', padx = xlen, pady = ylen, command = lambda:book4(32,  2)).place(x = xloc, y = yloc); i += 1; xloc += 100
    Button(window1, text = ('Slot ', i), bg = 'light green', padx = xlen, pady = ylen, command = lambda:book4(33,  3)).place(x = xloc, y = yloc); i += 1; xloc += 100
    Button(window1, text = ('Slot ', i), bg = 'light green', padx = xlen, pady = ylen, command = lambda:book4(34,  4)).place(x = xloc, y = yloc); i += 1; xloc += 100
    Button(window1, text = ('Slot ', i), bg = 'light green', padx = xlen, pady = ylen, command = lambda:book4(35,  5)).place(x = xloc, y = yloc); i += 1; xloc += 100
    Button(window1, text = ('Slot ', i), bg = 'light green', padx = xlen, pady = ylen, command = lambda:book4(36,  6)).place(x = xloc, y = yloc); i += 1; xloc += 100
    Button(window1, text = ('Slot ', i), bg = 'light green', padx = xlen, pady = ylen, command = lambda:book4(37,  7)).place(x = xloc, y = yloc); i += 1; xloc += 100
    Button(window1, text = ('Slot ', i), bg = 'light green', padx = xlen, pady = ylen, command = lambda:book4(38,  8)).place(x = xloc, y = yloc); i += 1; xloc += 100
    Button(window1, text = ('Slot ', i), bg = 'light green', padx = xlen, pady = ylen, command = lambda:book4(39,  9)).place(x = xloc, y = yloc); i += 1; xloc += 100
    Button(window1, text = ('Slot ', i), bg = 'light green', padx = xlen, pady = ylen, command = lambda:book4(40, 10)).place(x = xloc, y = yloc); i += 1;

    xloc = 100; yloc = 400
    Button(window1, text = ('Slot ', i), bg = 'light green', padx = xlen, pady = ylen, command = lambda:book5(41,  1)).place(x = xloc, y = yloc); i += 1; xloc += 100
    Button(window1, text = ('Slot ', i), bg = 'light green', padx = xlen, pady = ylen, command = lambda:book5(42,  2)).place(x = xloc, y = yloc); i += 1; xloc += 100
    Button(window1, text = ('Slot ', i), bg = 'light green', padx = xlen, pady = ylen, command = lambda:book5(43,  3)).place(x = xloc, y = yloc); i += 1; xloc += 100
    Button(window1, text = ('Slot ', i), bg = 'light green', padx = xlen, pady = ylen, command = lambda:book5(44,  4)).place(x = xloc, y = yloc); i += 1; xloc += 100
    Button(window1, text = ('Slot ', i), bg = 'light green', padx = xlen, pady = ylen, command = lambda:book5(45,  5)).place(x = xloc, y = yloc); i += 1; xloc += 100
    Button(window1, text = ('Slot ', i), bg = 'light green', padx = xlen, pady = ylen, command = lambda:book5(46,  6)).place(x = xloc, y = yloc); i += 1; xloc += 100
    Button(window1, text = ('Slot ', i), bg = 'light green', padx = xlen, pady = ylen, command = lambda:book5(47,  7)).place(x = xloc, y = yloc); i += 1; xloc += 100
    Button(window1, text = ('Slot ', i), bg = 'light green', padx = xlen, pady = ylen, command = lambda:book5(48,  8)).place(x = xloc, y = yloc); i += 1; xloc += 100
    Button(window1, text = ('Slot ', i), bg = 'light green', padx = xlen, pady = ylen, command = lambda:book5(49,  9)).place(x = xloc, y = yloc); i += 1; xloc += 100
    Button(window1, text = ('Slot ', i), bg = 'light green', padx = xlen, pady = ylen, command = lambda:book5(50, 10)).place(x = xloc, y = yloc);

def Slot_Bike():
    window1 = Tk()
    window1.title('BIKE SLOTS')
    window1.geometry('1200x500')
    window1.configure(bg = "light pink")
    label = Label(window1, text = "Availability Slots For Bike", font = "times 28 bold", bg = 'light pink')
    label.place(x = 100, y = 25)

    def Close():
        window1.destroy()

    def disable(v):
        a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
        a.remove(v)
        for i in a:
            if 1 <= i <= 10:
                Button(window1, text = ('Slot ', i), bg = 'grey', padx = 20, pady = 20, state = DISABLED).place(x = 100 * i, y = 100)
            elif 11 <= i <= 20:
                Button(window1, text = ('Slot ', i), bg = 'grey', padx = 20, pady = 20, state = DISABLED).place(x = 100 * (i - 10), y = 175)
            else:
                Button(window1, text = ('Slot ', i), bg = 'grey', padx = 20, pady = 20, state = DISABLED).place(x = 100 * (i - 20), y = 250)
        Button(window1, text = "Your Slot Is Booked, Click Me to Confirm", padx = 50, pady = 20, bg = 'light yellow', font = "calibri 10 bold", command = Close).place(x = 800, y = 25)

    def book1(v, j):
        Button(window1, text = ('Slot ', v), bg = 'red', padx = 20, pady = 20).place(x = 100 * j, y = 100)
        disable(v)

    def book2(v, j):
        Button(window1, text = ('Slot ', v), bg = 'red', padx = 20, pady = 20).place(x = 100 * j, y = 175)
        disable(v)

    def book3(v, j):
        Button(window1, text = ('Slot ', v), bg = 'red', padx = 20, pady = 20).place(x = 100 * j, y = 250)
        disable(v)

    i = 1; xlen = 20; ylen = 20; xloc = 100; yloc = 100
    Button(window1, text = ('Slot ', i), bg = 'light green', padx = xlen, pady = ylen, command = lambda:book1( 1,  1)).place(x = xloc, y = yloc); i += 1; xloc += 100
    Button(window1, text = ('Slot ', i), bg = 'light green', padx = xlen, pady = ylen, command = lambda:book1( 2,  2)).place(x = xloc, y = yloc); i += 1; xloc += 100
    Button(window1, text = ('Slot ', i), bg = 'light green', padx = xlen, pady = ylen, command = lambda:book1( 3,  3)).place(x = xloc, y = yloc); i += 1; xloc += 100
    Button(window1, text = ('Slot ', i), bg = 'light green', padx = xlen, pady = ylen, command = lambda:book1( 4,  4)).place(x = xloc, y = yloc); i += 1; xloc += 100
    Button(window1, text = ('Slot ', i), bg = 'light green', padx = xlen, pady = ylen, command = lambda:book1( 5,  5)).place(x = xloc, y = yloc); i += 1; xloc += 100
    Button(window1, text = ('Slot ', i), bg = 'light green', padx = xlen, pady = ylen, command = lambda:book1( 6,  6)).place(x = xloc, y = yloc); i += 1; xloc += 100
    Button(window1, text = ('Slot ', i), bg = 'light green', padx = xlen, pady = ylen, command = lambda:book1( 7,  7)).place(x = xloc, y = yloc); i += 1; xloc += 100
    Button(window1, text = ('Slot ', i), bg = 'light green', padx = xlen, pady = ylen, command = lambda:book1( 8,  8)).place(x = xloc, y = yloc); i += 1; xloc += 100
    Button(window1, text = ('Slot ', i), bg = 'light green', padx = xlen, pady = ylen, command = lambda:book1( 9,  9)).place(x = xloc, y = yloc); i += 1; xloc += 100
    Button(window1, text = ('Slot ', i), bg = 'light green', padx = xlen, pady = ylen, command = lambda:book1(10, 10)).place(x = xloc, y = yloc); i += 1;

    xloc = 100; yloc = 175
    Button(window1, text = ('Slot ', i), bg = 'light green', padx = xlen, pady = ylen, command = lambda:book2(11,  1)).place(x = xloc, y = yloc); i += 1; xloc += 100
    Button(window1, text = ('Slot ', i), bg = 'light green', padx = xlen, pady = ylen, command = lambda:book2(12,  2)).place(x = xloc, y = yloc); i += 1; xloc += 100
    Button(window1, text = ('Slot ', i), bg = 'light green', padx = xlen, pady = ylen, command = lambda:book2(13,  3)).place(x = xloc, y = yloc); i += 1; xloc += 100
    Button(window1, text = ('Slot ', i), bg = 'light green', padx = xlen, pady = ylen, command = lambda:book2(14,  4)).place(x = xloc, y = yloc); i += 1; xloc += 100
    Button(window1, text = ('Slot ', i), bg = 'light green', padx = xlen, pady = ylen, command = lambda:book2(15,  5)).place(x = xloc, y = yloc); i += 1; xloc += 100
    Button(window1, text = ('Slot ', i), bg = 'light green', padx = xlen, pady = ylen, command = lambda:book2(16,  6)).place(x = xloc, y = yloc); i += 1; xloc += 100
    Button(window1, text = ('Slot ', i), bg = 'light green', padx = xlen, pady = ylen, command = lambda:book2(17,  7)).place(x = xloc, y = yloc); i += 1; xloc += 100
    Button(window1, text = ('Slot ', i), bg = 'light green', padx = xlen, pady = ylen, command = lambda:book2(18,  8)).place(x = xloc, y = yloc); i += 1; xloc += 100
    Button(window1, text = ('Slot ', i), bg = 'light green', padx = xlen, pady = ylen, command = lambda:book2(19,  9)).place(x = xloc, y = yloc); i += 1; xloc += 100
    Button(window1, text = ('Slot ', i), bg = 'light green', padx = xlen, pady = ylen, command = lambda:book2(20, 10)).place(x = xloc, y = yloc); i += 1;

    xloc = 100; yloc = 250
    Button(window1, text = ('Slot ', i), bg = 'light green', padx = xlen, pady = ylen, command = lambda:book3(21,  1)).place(x = xloc, y = yloc); i += 1; xloc += 100
    Button(window1, text = ('Slot ', i), bg = 'light green', padx = xlen, pady = ylen, command = lambda:book3(22,  2)).place(x = xloc, y = yloc); i += 1; xloc += 100
    Button(window1, text = ('Slot ', i), bg = 'light green', padx = xlen, pady = ylen, command = lambda:book3(23,  3)).place(x = xloc, y = yloc); i += 1; xloc += 100
    Button(window1, text = ('Slot ', i), bg = 'light green', padx = xlen, pady = ylen, command = lambda:book3(24,  4)).place(x = xloc, y = yloc); i += 1; xloc += 100
    Button(window1, text = ('Slot ', i), bg = 'light green', padx = xlen, pady = ylen, command = lambda:book3(25,  5)).place(x = xloc, y = yloc); i += 1; xloc += 100
    Button(window1, text = ('Slot ', i), bg = 'light green', padx = xlen, pady = ylen, command = lambda:book3(26,  6)).place(x = xloc, y = yloc); i += 1; xloc += 100
    Button(window1, text = ('Slot ', i), bg = 'light green', padx = xlen, pady = ylen, command = lambda:book3(27,  7)).place(x = xloc, y = yloc); i += 1; xloc += 100
    Button(window1, text = ('Slot ', i), bg = 'light green', padx = xlen, pady = ylen, command = lambda:book3(28,  8)).place(x = xloc, y = yloc); i += 1; xloc += 100
    Button(window1, text = ('Slot ', i), bg = 'light green', padx = xlen, pady = ylen, command = lambda:book3(29,  9)).place(x = xloc, y = yloc); i += 1; xloc += 100
    Button(window1, text = ('Slot ', i), bg = 'light green', padx = xlen, pady = ylen, command = lambda:book3(30, 10)).place(x = xloc, y = yloc); i += 1;

def time():
    import datetime
    now = datetime.datetime.now()
    h_entry = now.strftime('%H')
    m_entry = now.strftime('%M')
    return h_entry, m_entry

def amt_hrs(hrs, mi):
    amt = 60
    if hrs < 2:
        mi = 0
    if hrs <= 2:
        amt = 60
    else:
        hrs = hrs - 2
        d = hrs * 2
        amt += d * 20
    if mi == 0:
       amt += 0
    elif 0 < mi <= 30:
       amt += 20
    else:
       amt += 40
    return amt

def clk(hh, mm):
  window1 = Tk()
  window1.title('BILLING')
  window1.geometry('1000x200')
  window1.configure(bg = "light pink")

  h_exi = (int)(hh)
  m_exi = (int)(mm)
  h_entry, m_entry = time()

  if h_exi == (int)(h_entry):
    if m_exi <= (int)(m_entry):
      h_exi += 24
  
  if (int)(h_entry) > h_exi:
     h_exi += 24
  h = h_exi - (int)(h_entry)
  m = m_exi - (int)(m_entry)
  if m < 0:
    m = -m
    h -= 1
    m = 60 - m
  amt = amt_hrs(h, m)

  label=Label(window1, text = ("Estimated", "Time", "Spent", ":", h, "Hours", m, "Minutes"), font = "times 28 bold", bg = "light pink")
  label.place(x = 200, y = 65)
  label=Label(window1, text = ("Amount", ":", "Rs", amt), font = "times 28 bold", bg = "light pink")
  label.place(x = 200, y = 105)

def amount():
    global hrs, mins, hvar, mvar
    hrs = StringVar(window)
    hrs.set("Select the exit hour")
    mins = StringVar(window)
    mins.set("Select the exit minutes")

    hvar = StringVar(window)
    mvar = StringVar(window)
    h_entry, m_entry = time()
    hvar = h_entry
    mvar = m_entry

    def hours(h_exi):
       global hvar
       hvar = h_exi

    def minutes(m_exi):
        mvar = m_exi
        clk(hvar, mvar)

    w = OptionMenu(window, hrs, "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "00", command = hours)
    w.configure(bg = "cyan", font = "times")
    w.pack()

    w = OptionMenu(window, mins, "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", 
                   "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59", "00", command = minutes)
    w.configure(bg = "aqua", font = "times")
    w.pack()

window = Tk()
window.title('Parking Management')
window.geometry('900x400')
window.configure(bg = "light green")
frame = LabelFrame(window, text = 'Type of the Vehicle', font = "times 28 bold", borderwidth = 20, relief = GROOVE, bg = 'light green')
frame.pack()
Button(frame, text = 'Available Slots For Car', font = "times", command = Slot_Car, bg = "light pink").grid(row = 5, column = 10)
Button(frame, text = 'Available Slots For Bike', font = "times", command = Slot_Bike, bg = "salmon").grid(row = 5, column = 11)
Button(window, text = 'Billing Amount', font = "times 24 bold", bg = "gold", command = amount).place(x = 60, y = 110)
window.mainloop()
