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
	def __init__(self, center, canvas, length, tipLength, color, width):
		self.canvas = canvas
		self.width = width
		self.color = color
		self.drawn = False
		self.tipLength = tipLength
		self.set(center, math.pi/2, length)

	def set(self, center, radians, length):
		self.center = center
		self.radians = -radians -  math.pi/2
		self.p1 = Point((self.center.x + math.sin(self.radians) * length/2), (self.center.y + math.cos(self.radians)*length/2))
		self.p2 = Point((self.center.x - math.sin(self.radians) * length/2), (self.center.y - math.cos(self.radians)*length/2))
		self.p3 = Point((self.p2.x + math.sin(self.radians+math.pi/4) * self.tipLength), (self.p2.y + math.cos(self.radians+math.pi/4)*self.tipLength))
		self.p4 = Point((self.p2.x + math.sin(self.radians-math.pi/4) * self.tipLength), (self.p2.y + math.cos(self.radians-math.pi/4)*self.tipLength))

		if(self.drawn):
			self.undraw()
		else:
			self.drawn = True
		self.draw()

	def draw(self):
		self.line1 = self.canvas.create_line(self.p1.x, self.p1.y, self.p2.x, self.p2.y, width=self.width, fill=self.color)
		self.line2 = self.canvas.create_line(self.p2.x, self.p2.y, self.p3.x, self.p3.y, width=self.width, fill=self.color)
		self.line3 = self.canvas.create_line(self.p2.x, self.p2.y, self.p4.x, self.p4.y, width=self.width, fill=self.color)

	def undraw(self):
		self.canvas.delete(self.line1)
		self.canvas.delete(self.line2)
		self.canvas.delete(self.line3)



class Wheel():
	def __init__(self, center, canvas):
		self.canvas = canvas
		self.arrow = Arrow(center, self.canvas, 1, 7.5, "black", 2)
	def rotate(self, theta, center, power):
		self.arrow.set(center, theta, 50*power)

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
		self.arrow = Arrow(self.center, self.swerve, 50, 15, "white", 2)

		self.wI = Wheel(I,self.swerve)
		self.wII = Wheel(II,self.swerve)
		self.wIII = Wheel(III,self.swerve)
		self.wIV = Wheel(IV,self.swerve)

	def updateWheels(self, wIR, wIP, wIIR, wIIP, wIIIR, wIIIP, wIVR, wIVP):
		self.wI.rotate(self.radians-wIR,self.rI, wIP)
		self.wII.rotate(self.radians-wIIR,self.rII, wIIP)
		self.wIII.rotate(self.radians-wIIIR,self.rIII, wIIIP)
		self.wIV.rotate(self.radians-wIVR,self.rIV, wIVP)

	def rotate(self,theta):
		self.radians = theta
		self.rI = self.I.rotate(theta,self.center)
		self.rII = self.II.rotate(theta,self.center)
		self.rIII = self.III.rotate(theta,self.center)
		self.rIV = self.IV.rotate(theta,self.center)
		self.draw()

		self.arrow.set(self.center, theta-math.pi/2, 50)

	def draw(self):
		self.swerve.coords(self.chassisG,self.rI.x,self.rI.y,self.rII.x,self.rII.y,self.rIII.x,self.rIII.y,self.rIV.x,self.rIV.y)
