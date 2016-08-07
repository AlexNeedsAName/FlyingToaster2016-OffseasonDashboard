#!/usr/bin/env python

from Tkinter import *
from ttk import Frame, Button, Style
import UDP

class GUI(Frame):
	def __init__(self, parent):
		Frame.__init__(self, parent)

		self.parent = parent

		self.parent.title("Dashboard: 2016 Offseason")
		self.style = Style()
		self.style.theme_use("default")

		frame = Frame(self, relief=RAISED, borderwidth=1)
		frame.pack(fill=BOTH, expand=True) 

		self.pack(fill=BOTH, expand=True)

		self.positionWindow()
		self.okButton = Button(self, text="OK")
		self.okButton.pack(side=RIGHT, padx=5, pady=5)
	
	def positionWindow(self):
		width  = self.parent.winfo_screenwidth()
		height = self.parent.winfo_screenheight()/2
		self.parent.geometry("%dx%d+-5+0"%(width,height))

root = Tk()
window = GUI(root)

while 1:
	root.update_idletasks()
	root.update()
	try:
		data = UDP.getData()
		if(data[:7] == ":PRINT:"):
			print data[7:]
	except UDP.socket.timeout:
		pass
