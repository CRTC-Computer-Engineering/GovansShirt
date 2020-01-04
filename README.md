# GovansShirt
Calculates the costs of clothing orders

Follow the instructions on this cool website
https://wiki.wxpython.org/How%20to%20install%20wxPython

Also, use the Getting Started tab to learn how to use wx.


Install Python
The stable release of wxPython requires Python version 2.7. Get it from the official download page.

Windows
Installation under windows is especially simple: Run the installer you can get from wxPython and follow the instructions.

Mac OS X
An installer is available on the wxPython site, for both PPC and Intel Macs.

If you wish to build it yourself, you should follow the instruction described here.

A french howto can be found here

If you receive a message about the package being "damaged and can't be opened", then you need to change the security preference setting that is labeled Allow applications downloaded from: to Anywhere.

GNU/Linux - Redhat
You can find RPMs for Redhat (they are working just fine with Mandrake through), at the address wxPython

GNU/Linux - Debian
wxPython can be installed through apt-get by calling apt-get install python-wxgtk2.8 or apt-get install python-wxgtk2.6, depending on which version you want. You may have to call this with root permissions. The wxPython demo is in the wx-examples package. However, it is advised to install the demo separately, as described at Using wxPython Demo Code.

Try this:


apt-get install python-wxgtk2.8
Please note that sometimes older versions of wx are installed by using this method See InstallingOnUbuntuOrDebian for how to get the latest versions with apt-get.

GNU/Linux - Raspbian on Raspberry Pi
wxPython 4.0.1 can be installed and does run on Raspberry Pi's Debian variants 'Jessie' and 'Stretch'. It works on Python 3.4 and up. For install instructions Build wxPython on Raspberry Pi.

GNU/Linux - Gentoo
wxPython can be installed through portage by calling emerge wxPython (notice the capital P). The correct command is actually emerge wxpython (without a capital p) as of 11/28/04.

GNU/Linux - Building from the source
You might also want to build wxPython from the source. You have to do this in three steps:

Installing wxGTK from source
wxGTK is the GTK version of wxWidgets. GTK (Gimp ToolKit) is a graphic library used by Gnome, so it is probably already installed on your Linux box. All you have to do is download the wxGTK source from the wxGTK ftp server. Or the wxWidgets website

Untar wxGTK by type the command:
tar -xvzf wxGTK-2.2.5.tar.gz
Go into the directory:
cd wxGTK-2.2.5
Run the configure script:
./configure --with-gtk
You might get some errors here if GTK is not installed or if the include files for GTK are not installed (in a Mandrake distribution, gtk+-devel-1.2.8-6mdk.i586.rpm is the rpm that you want to install)

Run the make file:
make
You might get some errors here if yacc or lex are not installed. (in a Mandrake distribution, the right rpms are byacc-1.9-7mdk.i586.rpm and flex-2.5.4a-13mdk.i586.rpm)
You should now have a compiled version of wxGTK. We want to install it and link it into the system.

Become superuser:
su
Your root password is required here.

Install wxGTK:
make install
Link the library:
ldconfig
Exit from superuser mode:
exit
Normally, wxGTK is installed but there might be a problem with wxPython:
it is possible that the library is not installed where wxPython is looking for it. ( In a mandrake 7.2 distribution, you want wxGTK to be installed in /usr/lib whereas it is automatically installed in /usr/local/lib) The solution is to create a symbolic link of the library where you want it to be:

Go in to the directory where you want the library to be installed:
cd /usr/lib
Create a symbolic link to the library:
ln -s /usr/local/lib/libwx_gtk.so
Installing wxPython from source
Download the source code of the last wxPython release:
wxPython website

Untar the tarball:
tar -xvzf wxPython-2.2.5.tar.gz
go into the directory:
cd wxPython-2.2.5
Edit the setup.py to choose what you want to install. I suggest that you don't install OGL and GL_CANVAS. by selecting:
BUILD_GLCANVAS = 0 # If true, build the contrib/glcanvas extension module
BUILD_OGL = 0      # If true, build the contrib/ogl extension module
BUILD_STC = 1      # If true, build the contrib/stc extension module
CORE_ONLY = 0      # if true, don't build any of the above
GL_ONLY = 0        # Only used when making the -gl RPM.  See the "b" script
                   # for the ugly details
USE_SWIG = 0       # Should we actually execute SWIG, or just use the
                   # files already in the distribution?
IN_CVS_TREE = 0    # Set to true if building in a full wxWidgets CVS
                   # tree, otherwise will assume all needed files are
                   # available in the wxPython source distribution
Build the python module:
python setup.py build
Become root:
su
Your root password is required here.

Install the module:
python setup.py install
Exit root mode:
exit
Check if the module works:
 [lucas@b007 wxPython-2.2.5]$ python
Python 1.5.2 (#1, Sep 30 2000, 18:08:36)  [GCC 2.95.3 19991030 (prerelease)] on linux-i386
Copyright 1991-1995 Stichting Mathematisch Centrum, Amsterdam
>>> import wx
>>>
wxPython is fully installed!

Installing wxPython-Phoenix using pip
Please note that the most up to date information about installing the new wxPython4 wheels is usually located on the main wxPython website at: https://wxpython.org/pages/downloads/.

Make sure you have recent versions of pip and setuptools installed.

Installing wxPython4 (Phoenix) on Linux Since wxPython is not able to be built to the manylinux1 standard we're not able to put binaries on PyPI. Instead binary wheels are made available for a few popular linux distributions, and you can install them using pip once you locate the proper folder to tell pip to download from. Look around in https://extras.wxpython.org/wxPython4/extras/linux for a folder matching your distro and gtk preference. You can then install with a command like the following command. If you are not installing into a Python virtual environment then you will probably need to insert sudo at the beginning of the command:

   pip install -U \
      -f https://extras.wxpython.org/wxPython4/extras/linux/gtk3/ubuntu-16.04 \
      wxPython
Installing wxPython4 (Phoenix) on Windows and OSX Binary wheels for these platforms are available on PyPI so you can install with this simpler command if build are available for your target Python:

   pip install -U wxPython
Verify installation
   python2
   >>> import wx
   >>> wx.VERSION_STRING
   '4.0.1'
   >>> wx.version()
   '4.0.1 osx-cocoa (phoenix)'
