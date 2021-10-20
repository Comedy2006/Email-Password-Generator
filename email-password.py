import names
import random
import string
import tkinter
from tkinter import messagebox

domain = ["gmail.com", "gmx.net", "web.de", "yahoo.com", "hotmail.com", "aol.com", 
    "hotmai.co.uk", "hotmail.fr", "msn.com", "yahoo.fr", "wanadoo.fr", "orange.fr", "comcast.net", 
    "yahoo.co.uk", "yahoo.com.br", "yahoo.co.in", "live.com", "rediffmail.com", "free.fr"]

top = tkinter.Tk()
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

B1 = tkinter.Button(top, text = "Email with a real name", command = mailadress)
B2 = tkinter.Button(top, text = "random character Email", command = secondmail)
B3 = tkinter.Button(top, text = "random generated Password", command = rngPasswd)
B1.pack()
B2.pack()
B3.pack()

top.mainloop()