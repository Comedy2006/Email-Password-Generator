import names
import random
import string
import tkinter
from tkinter import *
from tkinter import messagebox

domain = ["gmail.com", "gmx.net", "web.de", "yahoo.com", "hotmail.com", "aol.com", 
    "hotmai.co.uk", "hotmail.fr", "msn.com", "yahoo.fr", "wanadoo.fr", "orange.fr", "comcast.net", 
    "yahoo.co.uk", "yahoo.com.br", "yahoo.co.in", "live.com", "rediffmail.com", "free.fr"]


top = tkinter.Tk()
top.title("Email-Password-Generator")

def mailadress():
    
    name = names.get_full_name().replace(" ", ".").lower()
    mail = name + "@" + random.choice(domain)

    return messagebox.showinfo("normal Email", "Email: " + mail)

def secondmail():

    rngmail = ''.join(random.choice(string.ascii_letters+string.digits) for i in range(random.randint(15,20))) + "@" + random.choice(domain)

    return messagebox.showinfo("RNG Email", "Email: " + rngmail)

def rngPasswd():

    passwd = ''.join(random.choice(string.ascii_letters+string.digits) for i in range(random.randint(10,16)))

    return messagebox.showinfo("RNG Password", "Password: " + passwd)

def rngPasswdSpecial():

    passwdsp = ''.join(random.choice(string.ascii_letters+string.digits+string.punctuation) for i in range(random.randint(10,16)))

    return messagebox.showinfo("RNG Password", "Password: " + passwdsp)

def genEmail():
    var0b = var0.get()
    if var0b == 0:
        mailadress()
    elif var0b == 1:
        secondmail()
    else:
        print("email")

def genPasswd():
    var1b = var1.get()
    if var1b == 0:
        rngPasswd()
    elif var1b == 1:
        rngPasswdSpecial()
    else:
        print("passwd")

var0, var1 = IntVar(), IntVar()
R1 = tkinter.Radiobutton(top, text="Real name", variable=var0, value=0).grid(row = 1, column = 1, sticky="w")
R2 = tkinter.Radiobutton(top, text="Random characters", variable=var0, value=1).grid(row = 2, column = 1, sticky="w")
R3 = tkinter.Radiobutton(top, text="Without special characters", variable=var1, value=0).grid(row = 1, column = 2, sticky="w")
R4 = tkinter.Radiobutton(top, text="With special characters", variable=var1, value=1).grid(row = 2, column = 2, sticky="w")
B1 = tkinter.Button(top, text = "Generate Email", width = 20, command = genEmail).grid(row = 3, column = 1)
B2 = tkinter.Button(top, text = "Generate Password", width = 20, command = genPasswd).grid(row = 3, column = 2)


top.mainloop()
