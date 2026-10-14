from SimpleGraphics import *

#Set up Graph
line(100,100,100,500)
line(100,500,700,500)

#Get inputs
title = input("Enter title of chart: ")
barNum = int(input("Enter number of bars (2 to 6): "))
gridLine = int(input("Enter gridline interval (10 to 100): "))
labelY = input("Enter label for Y-Axis: ")

#Set up graph for bars
text(400,50,title,"c")
text(50,300,labelY,"c")
colours = ["red", "green", "blue", "yellow", "orange", "purple"]
barWidth = 500/barNum
barGap = 100/barNum
gridText = gridLine
gridY = 500 - gridLine
gridX = 100

#Make gridlines
for i in range (1, int(400/gridLine) + 1):
    text(750, gridY, str(gridText), "c")
    line(100, gridY, 700, gridY)
    gridY -= gridLine
    gridText += gridLine

#Make bars
for i in range (1, int(barNum)+1):
    label = input("Label Bar " + str(i) + ": ")
    value = int(input("Enter the value of bar " + label + ": "))
    setFill(colours[i-1])
    rect(gridX + barGap, 500 - value, barWidth, value)
    text(gridX + barGap + barWidth/2, 520, label, "c")
    text(gridX + barGap + barWidth/2, 500 - value + 20, str(value), "c")
    gridX += barWidth + barGap