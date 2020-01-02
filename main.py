"""
Project: Mungovans Order Calculator
Members: Aidan Boucher, Travis Bettens
Date Created: January 1, 2020
Professor: Mrs. Marcou
Block: C

Project Description: 
Create a program for Mr. Mungovan to enter clothing orders and generate a bill for his customers.
The program should include user input for: Customer ID, Type of clothing, Sizes, Quantities,
Color, and Unit Price. The program must also include math expressions that will calculate
the quantity/type breakdown costs and the final cost.

Pseudocode:




"""


#!/usr/bin/env python
import wx

app = wx.App(False) #   Creates a new app
frame = wx.Frame(None, wx.ID_ANY, "Aidan is cool") #   top-level window 
frame.Show(True) #  Shows the frame
app.MainLoop() #    applies the user feedback loop
