#!/usr/bin/env python
from Tkinter import *
import math

class Point():
	def __init__(self,x,y):
		self.x=x
		self.y=y
	def rotate(self, theta, center):
		theta = -theta;
		x= ((self.x-center.x) * math.cos(theta) - (self.y-center.y) * math.sin(theta))+center.x
		y= ((self.x-center.x) * math.sin(theta) + (self.y-center.y) * math.cos(theta))+center.y
		return Point(x,y)

class Arrow():
	def __init__(self, center, canvas, scale, color):
		self.center = center
		self.canvas = canvas

		n=15*scale
		self.n = n

		self.Tip = Point(center.x,	center.y-3*n)
		self.p1 = Point(self.Tip.x-n*1.5,self.Tip.y+2*n)
		self.p2 = Point(self.Tip.x-n/2,	self.Tip.y+2*n)
		self.p3 = Point(self.Tip.x-n/2,	self.Tip.y+6*n)
		self.p4 = Point(self.Tip.x+n/2,	self.Tip.y+6*n)
		self.p5 = Point(self.Tip.x+n/2,	self.Tip.y+2*n)
		self.p6 = Point(self.Tip.x+n*1.5,self.Tip.y+2*n)

		self.arrow = self.canvas.create_polygon(self.Tip.x, self.Tip.y, self.p1.x, self.p1.y, self.p2.x, self.p2.y, self.p3.x, self.p3.y, self.p4.x, self.p4.y, self.p5.x, self.p5.y, self.p6.x, self.p6.y, fill=color)

	def rotate(self,theta):
		self.rTip = self.Tip.rotate(theta,self.center)
		self.rp1 = self.p1.rotate(theta,self.center)
		self.rp2 = self.p2.rotate(theta,self.center)
		self.rp3 = self.p3.rotate(theta,self.center)
		self.rp4 = self.p4.rotate(theta,self.center)
		self.rp5 = self.p5.rotate(theta,self.center)
		self.rp6 = self.p6.rotate(theta,self.center)
		self.draw()

	def draw(self):
		self.canvas.coords(self.arrow,self.rTip.x, self.rTip.y, self.rp1.x, self.rp1.y, self.rp2.x, self.rp2.y, self.rp3.x, self.rp3.y, self.rp4.x, self.rp4.y, self.rp5.x, self.rp5.y, self.rp6.x, self.rp6.y)

class Swerve():
	def __init__(self, parrent, I, II, III, IV):
		self.I = I
		self.II = II
		self.III = III
		self.IV = IV
		self.center = Point(125,125)
		self.parrent = parrent
		self.swerve = Canvas(self.parrent, bg="white", height=250, width=250)
		self.swerve.grid(row=0,column=1)
		self.chassisG = self.swerve.create_polygon(I.x,I.y,II.x,II.y,III.x,III.y,IV.x,IV.y,fill="gray")
		self.arrow = Arrow(self.center, self.swerve, 1, "white")

	def rotate(self,theta):
		self.rI = self.I.rotate(theta,self.center)
		self.rII = self.II.rotate(theta,self.center)
		self.rIII = self.III.rotate(theta,self.center)
		self.rIV = self.IV.rotate(theta,self.center)
		self.draw()

		self.arrow.rotate(theta)

	def draw(self):
		self.swerve.coords(self.chassisG,self.rI.x,self.rI.y,self.rII.x,self.rII.y,self.rIII.x,self.rIII.y,self.rIV.x,self.rIV.y)
