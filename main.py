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

		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Name: ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )

		bSizer3.Add( self.m_staticText2, 0, wx.ALL, 5 )

		self.NameTextCtrl = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.NameTextCtrl, 0, wx.ALL, 5 )

		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"ID: ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )

		bSizer3.Add( self.m_staticText3, 0, wx.ALL, 5 )

		self.IDTextCtrl = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.IDTextCtrl, 0, wx.ALL, 5 )

		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"Shirt Size?", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )

		bSizer3.Add( self.m_staticText4, 0, wx.ALL, 5 )

		m_comboBox1Choices = [ u"small", u"medium", u"large", u"extra large" ]
		self.m_comboBox1 = wx.ComboBox( self, wx.ID_ANY, u"small", wx.DefaultPosition, wx.DefaultSize, m_comboBox1Choices, 0 )
		bSizer3.Add( self.m_comboBox1, 0, wx.ALL, 5 )

		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"Type of Clothing?", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )

		bSizer3.Add( self.m_staticText5, 0, wx.ALL, 5 )

		m_comboBox3Choices = [ u"t-shirt", u"longsleeve", u"sweatshirt", u"uniform", u"performance" ]
		self.m_comboBox3 = wx.ComboBox( self, wx.ID_ANY, u"t-shirt", wx.DefaultPosition, wx.DefaultSize, m_comboBox3Choices, 0 )
		bSizer3.Add( self.m_comboBox3, 0, wx.ALL, 5 )

		ColorRadioBoxChoices = [ u"red", u"blue", u"green", u"yellow", u"orange", u"purple", u"gray", u"black", u"white", u"pink" ]
		self.ColorRadioBox = wx.RadioBox( self, wx.ID_ANY, u"Color for the item?", wx.DefaultPosition, wx.Size( 310,150 ), ColorRadioBoxChoices, 4, wx.RA_SPECIFY_COLS )
		self.ColorRadioBox.SetSelection( 0 )
		self.ColorRadioBox.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.ColorRadioBox.SetMaxSize( wx.Size( 310,150 ) )

		bSizer3.Add( self.ColorRadioBox, 0, wx.ALL, 5 )

		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"How many of this item?", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )

		bSizer3.Add( self.m_staticText7, 0, wx.ALL, 5 )

		self.AmountTextCtrl = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.AmountTextCtrl, 0, wx.ALL, 5 )


		self.SetSizer( bSizer3 )
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
		self.Bind( wx.EVT_MENU, self.SaveFunc, id = self.m_menuItem1.GetId() )
		self.Bind( wx.EVT_MENU, self.ExitFunc, id = self.m_menuItem2.GetId() )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def SaveFunc( self, event ):
        GetLineText(self,-1)
		#

	def ExitFunc( self, event ):
		#


app = wx.App()
frame = MacGuvon(None)
frame.Show()
app.MainLoop()
