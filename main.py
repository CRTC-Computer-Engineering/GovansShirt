# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MacGuvon
###########################################################################

class MacGuvon ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"MacGuvons Order", pos = wx.DefaultPosition, size = wx.Size( 500,700 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		BoxSizer = wx.BoxSizer( wx.VERTICAL )

		self.name = wx.StaticText( self, wx.ID_ANY, u"Name: ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.name.Wrap( -1 )

		BoxSizer.Add( self.name, 0, wx.ALL, 5 )

		self.NameTextCtrl = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		BoxSizer.Add( self.NameTextCtrl, 0, wx.ALL, 5 )

		self.ID = wx.StaticText( self, wx.ID_ANY, u"ID: ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ID.Wrap( -1 )

		BoxSizer.Add( self.ID, 0, wx.ALL, 5 )

		self.IDTextCtrl = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		BoxSizer.Add( self.IDTextCtrl, 0, wx.ALL, 5 )

		self.ShirtSize = wx.StaticText( self, wx.ID_ANY, u"Shirt Size?", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ShirtSize.Wrap( -1 )

		BoxSizer.Add( self.ShirtSize, 0, wx.ALL, 5 )

		SizeComboBoxChoices = [ u"small", u"medium", u"large", u"extra large" ]
		self.SizeComboBox = wx.ComboBox( self, wx.ID_ANY, u"small", wx.DefaultPosition, wx.DefaultSize, SizeComboBoxChoices, 0 )
		BoxSizer.Add( self.SizeComboBox, 0, wx.ALL, 5 )

		self.type = wx.StaticText( self, wx.ID_ANY, u"Type of Clothing?", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.type.Wrap( -1 )

		BoxSizer.Add( self.type, 0, wx.ALL, 5 )

		TypeComboBoxChoices = [ u"t-shirt", u"longsleeve", u"sweatshirt", u"uniform", u"performance" ]
		self.TypeComboBox = wx.ComboBox( self, wx.ID_ANY, u"t-shirt", wx.DefaultPosition, wx.DefaultSize, TypeComboBoxChoices, 0 )
		BoxSizer.Add( self.TypeComboBox, 0, wx.ALL, 5 )

		ColorRadioBoxChoices = [ u"red", u"blue", u"green", u"yellow", u"orange", u"purple", u"gray", u"black", u"white", u"pink" ]
		self.ColorRadioBox = wx.RadioBox( self, wx.ID_ANY, u"Color for the item?", wx.DefaultPosition, wx.Size( 310,150 ), ColorRadioBoxChoices, 4, wx.RA_SPECIFY_COLS )
		self.ColorRadioBox.SetSelection( 0 )
		self.ColorRadioBox.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.ColorRadioBox.SetMaxSize( wx.Size( 310,150 ) )

		BoxSizer.Add( self.ColorRadioBox, 0, wx.ALL, 5 )

		self.Amount = wx.StaticText( self, wx.ID_ANY, u"How many of this item?", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Amount.Wrap( -1 )

		BoxSizer.Add( self.Amount, 0, wx.ALL, 5 )

		self.AmountTextCtrl = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		BoxSizer.Add( self.AmountTextCtrl, 0, wx.ALL, 5 )

		self.Done = wx.Button( self, wx.ID_ANY, u"Done", wx.DefaultPosition, wx.DefaultSize, 0 )
		BoxSizer.Add( self.Done, 0, wx.ALL, 5 )

		self.label = wx.StaticText( self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.label.Wrap( -1 )

		BoxSizer.Add( self.label, 0, wx.ALL, 5 )


		self.SetSizer( BoxSizer )
		self.Layout()
		self.m_menubar2 = wx.MenuBar( 0 )
		self.m_menu1 = wx.Menu()
		self.m_menuItem1 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Save", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.Append( self.m_menuItem1 )

		self.m_menuItem2 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Exit", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.Append( self.m_menuItem2 )

		self.m_menubar2.Append( self.m_menu1, u"File" )

		self.SetMenuBar( self.m_menubar2 )


		self.Centre( wx.BOTH )

		# Connect Events
		self.ColorRadioBox.Bind( wx.EVT_RADIOBOX, self.myFunc )
		self.Done.Bind( wx.EVT_BUTTON, self.buttonFunc )
		self.Bind( wx.EVT_MENU, self.SaveFunc, id = self.m_menuItem1.GetId() )
		self.Bind( wx.EVT_MENU, self.ExitFunc, id = self.m_menuItem2.GetId() )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def myFunc( self, event ):
		event.Skip()

	def buttonFunc( self, event ):
		getLabelText = self.SizeComboBox.GetSelection()
		self.label.SetLabel(getLabelText)
		self.Layout()

	def SaveFunc( self, event ):
		event.Skip()

	def ExitFunc( self, event ):
		event.Skip()


app = wx.App()
frame = MacGuvon(None)
frame.Show()
app.MainLoop()
