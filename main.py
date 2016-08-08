#!/usr/bin/env python

from Tkinter import *
from ttk import Frame, Button, Style
import os
import UDP
import swerveVisual
from swerveVisual import Point

root = Tk()

width  = 1920#root.winfo_screenwidth()
height = root.winfo_screenheight()*2/3
root.geometry('{}x{}+-6+0'.format(width,height))
root.resizable(width=False, height=False)

#Adding a Console for Debuging
console = Text(root, width=80, height=19, font="CourierNew 12",  bg="black", fg="#55FF55", relief=RAISED)
console.grid(row=0,column=0)
console.insert(END, "Welcome to DIY Dashboard\n")
console.config(state=DISABLED)

#Swerve Visual:
swerveGraphic= swerveVisual.Swerve(root,Point(200,50),Point(50,50),Point(50,200),Point(200,200))

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
		elif(data[:8] == ":SWERVE:"):
			d = dict(s.split("=") for s in data[8:].split(";"))
			swerveGraphic.rotate(float(d["R"]))
			swerveGraphic.updateWheels(float(d["wIR"]), float(d["wIP"]), float(d["wIIR"]), float(d["wIIP"]), float(d["wIIIR"]), float(d["wIIIP"]), float(d["wIVR"]), float(d["wIVP"]))
	except UDP.socket.timeout:
		pass
