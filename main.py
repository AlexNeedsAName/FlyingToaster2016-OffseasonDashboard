#!/usr/bin/env python

from Tkinter import Tk, BOTH
from ttk import Frame, Button, Style

class GUI(Frame):
	def __init__(self, parent):
		Frame.__init__(self, parent)

		self.parent = parent
		self.parent.title("Dashboard: 2016 Offseason")
		#self.style = Style()
		#self.style.theme_use("default")

		self.pack(fill=BOTH, expand=1)

		self.positionWindow()
	
	def positionWindow(self):
		width  = self.parent.winfo_screenwidth()
		height = self.parent.winfo_screenheight()/2
		self.parent.geometry("%dx%d+0+0"%(width,height))

root = Tk()
window = GUI(root)
root.mainloop()
