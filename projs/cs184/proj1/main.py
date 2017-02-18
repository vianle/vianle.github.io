from sys import argv
import random as rand
import os
import sys
import datetime
from time import gmtime, strftime
import re
import math



"""Tests all files in testing directory"""
def testmain():
	width = 800
	height = 800
	newName = Filename + ".svg"
	f = open(newName, "a")
	s = "<?xml version=\"1.0\" encoding=\"utf-8\"?>\n <!DOCTYPE svg PUBLIC \"-//W3C//DTD SVG 1.1//EN\" \"http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd\">\n	<svg version=\"1.1\" id=\"Layer_1\" xmlns=\"http://www.w3.org/2000/svg\" xmlns:xlink=\"http://www.w3.org/1999/xlink\" x=\"0px\" y=\"0px\" width=\""+	str(width)+"px\" height=\""+str(height)+"px\" viewBox=\"0 0 "+str(width)+" "+str(height)+"\" enable-background=\
		\"new 0 0 "+str(width)+" "+str(height)+"\" xml:space=\"preserve\">\n"
	deg = 270;
	for x in range(4):
		s += "<g transform=\"translate(400 400)\">\n<g transform=\"rotate("+str(deg)+")\">\n<g transform=\"translate(-400 -400)\">\n"
		r = 0
		g = 0
		b = 0
		a = 255
		count = 0
		# x1, y1, x2, y2 = width/2 - 30.0, height/2 + 30.0, width/2 + 30.0, height/2 + 30.0 #remember to keep values floats
		x1, y1, x2, y2 =  10.0, height, 10.0, height #remember to keep values floats
		angle = 2*math.atan2(x2/y2, -1)
		# angle = math.atan(y2/x2)
		r1, g1, b1 = 5, 7, 10
		while count < 25:
			count += 1
			r += r1
			g += g1
			b += b1
			# if r > 255 or r < 0:
			# 	r1 = -r1
			
			# if g > 255 or g < 0:
			# 	g1 = -g1
			
			# if b > 255 or b < 0:
			# 	b1 = -b1
			
			x1, y1, x2, y2 = int(x2), int(y2), x2 + width, y2 + height
			# x1, y1 = x1*math.cos(angle) - y1*math.sin(angle), y1*math.cos(angle) + x1*math.sin(angle)
			x2, y2 = x2*math.cos(angle) - y2*math.sin(angle), y2*math.cos(angle) + x2*math.sin(angle)
			x2, y2 = int(x2 - width), int(y2 - height)
			line1 = str((r/255.0)) + " " + str(g/255.0) + " " + str(b/255.0) + " " + str(a/255.0)
			line2 = str((b/255.0)) + " " + str((g)/255.0) + " " + str(r/255.0) + " " + str(a/255.0)
			line3 = str((r/255.0)) + " " + str((g/255.0)) + " " + str(1-(b/255.0)) + " " + str(a/255.0)
			# s += "<polygon fill=\"rgba(" + str(r) + "," + str(g) + "," + str(b) + "," + str(a) + ")\" points=\""+ str(width) +"," + str(height) + " " + str(x1) + "," + str(y1) + " " + str(x2) + "," + str(y2) + "\"/>\n"
			# s += "<polygon fill=\"#1865ED)\" points=\"0,0 " + str(x1) + "," + str(y1) + " " + str(x2) + "," + str(y2) + "\"/>\n"
			s += "<colortri points=\""+ str(width) +" " + str(height) + " " + str(x1) + " " + str(y1) + " " + str(x2) + " " + str(y2) + "\" colors=\" "+line2+" "+line3+" "+line1+" \"/>\n"
		deg -=90 
		s += "</g>\n</g>\n</g>\n"
	s += "</svg>"
	f.write(s)
	f.close()



if len(argv) == 2: 
	runningfile, Filename = argv
	testmain()
elif len(argv) == 3 and argv[1] == "rm":
	os.remove(argv[2]+".svg")

