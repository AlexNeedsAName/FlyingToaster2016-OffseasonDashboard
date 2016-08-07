#!/usr/bin/env python

from Tkinter import *
from ttk import Frame, Button, Style
import os
import UDP

root = Tk()

width  = root.winfo_screenwidth()
height = root.winfo_screenheight()/2
root.geometry('{}x{}+-6+0'.format(width,height))
root.resizable(width=False, height=False)

console = Text(root, width=80, font="CourierNew 12",  bg="black", fg="#55FF55", relief=RAISED)
console.grid(row=0,column=0)

console.insert(END, "Welcome to DIY Dashboard\n")
console.config(state=DISABLED)

while 1:
	root.update_idletasks()
	root.update()
	try:
		data, addr = UDP.getData()
		if(data[:7] == ":PRINT:"):
			console.config(state=NORMAL)
			console.insert(END, str(addr[0]) + ": " + data[7:] + "\n")
			console.see(END)
			console.config(state=DISABLED)
	except UDP.socket.timeout:
		pass
