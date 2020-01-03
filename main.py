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

bing bong bing bing bong bong



"""


#!/usr/bin/env python
import wx # the library used to make the app
import calc # imported from C:\...\GovansShirt
import tables # imported from C:\...\GovansShirt

class Menu(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent,size=(400,500))

        # the edit control - one line version.
        self.id = wx.StaticText(self, label="Your ID :", pos=(20, 30))
        self.editid = wx.TextCtrl(self, value="Enter your ID here", pos=(150, 30), size=(140,-1))

        # shows logs in app.

        # A multiline TextCtrl - This is here to show how the events work in this program, don't pay too much attention to it
        # self.logger = wx.TextCtrl(self, pos=(300,20), size=(200,300), style=wx.TE_MULTILINE | wx.TE_READONLY)

        # A button
        self.button =wx.Button(self, label="Done", pos=(150, 325))
        self.Bind(wx.EVT_BUTTON, self.OnClick,self.button)

        # the edit control - one line version.
        self.lblname = wx.StaticText(self, label="Your name :", pos=(20,60))
        self.editname = wx.TextCtrl(self, value="Enter here your name", pos=(150, 60), size=(140,-1))
        self.Bind(wx.EVT_TEXT, self.EvtText, self.editname)
        self.Bind(wx.EVT_CHAR, self.EvtChar, self.editname)

        # the combobox Control
        # dropdown with options
        self.sampleList = ['small', 'medium', 'large', 'Extra Large']
        self.lblhear = wx.StaticText(self, label="Shirt size?", pos=(20, 90))
        self.edithear = wx.ComboBox(self, pos=(150, 90), size=(95, -1), choices=self.sampleList, style=wx.CB_DROPDOWN)
        self.Bind(wx.EVT_COMBOBOX, self.EvtComboBox, self.edithear)
        self.Bind(wx.EVT_TEXT, self.EvtText,self.edithear)

        # Checkbox
        self.insure = wx.CheckBox(self, label="Do you want Insured Shipment ?", pos=(20,140))
        self.Bind(wx.EVT_CHECKBOX, self.EvtCheckBox, self.insure)

        # Radio Boxes
        radioList = ['blue', 'red', 'yellow', 'orange', 'green', 'purple', 'navy blue', 'black', 'gray']
        rb = wx.RadioBox(self, label="What color would you like ?", pos=(20, 170), choices=radioList,  majorDimension=3,
                         style=wx.RA_SPECIFY_COLS)
        self.Bind(wx.EVT_RADIOBOX, self.EvtRadioBox, rb)

    def EvtRadioBox(self, event):
        self.logger.AppendText('EvtRadioBox: %d\n' % event.GetInt())
    def EvtComboBox(self, event):
        self.logger.AppendText('EvtComboBox: %s\n' % event.GetString())
    def OnClick(self,event):
        self.logger.AppendText(" Click on object with Id %d\n" %event.GetId())
    def EvtText(self, event):
        self.logger.AppendText('EvtText: %s\n' % event.GetString())
    def EvtChar(self, event):
        self.logger.AppendText('EvtChar: %d\n' % event.GetKeyCode())
        event.Skip()
    def EvtCheckBox(self, event):
        self.logger.AppendText('EvtCheckBox: %d\n' % event.Checked())


app = wx.App(False) #   Creates a new app
frame = wx.Frame(None, wx.ID_ANY, "Mucgovans Shirt", size=(400,500)) #   top-level window
panel = Menu(frame)
frame.Show()#  Shows the frame
app.MainLoop()#    applies the user feedback loop
