#!/usr/bin/python
#
# Installer for Forty-two
#

# Import the system module
from os import system

# Import the path module
from os import path

# Import the path module
from sys import exit 

# Prompt 'em
print "\x1b[1;31mYOU ARE GOING TO BE MOVING SYSTEM FILES\x1b[0m"
print "\x1b[1;31mTHIS COULD DESTROY YOUR SYSTEM\x1b[0m"
Print " are you sure you want to install forty-two , type yes or no"
logq = str(raw_input(' yes or no : '))

if logq == "yes":
	print " install starting..."
	
elif logq == "no":
	print " 42 has NOT been installed "
        exit()
	
else:
	print "you did not type yes or no , if you would like to install fort-two try again"
        exit()

	
system( "/usr/bin/clear" )

# Array of files
files = [ "rc", "rc.multi", "rc.shutdown", "rc.single", "initconf.py", "inittab", "rc.local", "rc.d/skeleton" ]

# If the files already exist, move them to /etc/[file].old
for file in files:
	tmp = "/etc/"+file
	if path.exists( tmp ):
		print "\x1b[1;31mMOVING\x1b[0m /etc/"+file+" to /etc/"+file+".old"
		tmp = "mv /etc/"+file+" /etc/"+file+".old"
		system( tmp )

# Now move the files to /etc
for file in files:
	print "\x1b[1;32mMOVING\x1b[0m ",file,"to /etc/"+file
	tmp = "/bin/mv "+file+" /etc/"+file
	system( tmp )
	tmp = "/bin/chmod +x /etc/"+file

print "\x1b[1;32mMOVING\x1b[0m initconf.py man page to /usr/man/man5/initconf.py.5.gz"
system( "mv man/initconf.py.5.gz /usr/man/man5/initconf.py.5.gz" )

if path.exists( "/etc/rc.conf" ):
	print "\x1b[1;31mMOVING\x1b[0m /etc/rc.conf to /etc/rc.conf.old"
	system( "mv /etc/rc.conf /etc/rc.conf.old" )

print "\x1b[1;32mLINKING\x1b[0m /etc/initconf.py to /etc/rc.conf"
system( "ln -sf /etc/initconf.py /etc/rc.conf" )

# Move rc.d/skeleton to /etc/rc.d/
print "\x1b[1;32mMOVING\x1b[0m rc.d/skeleton to /etc/rc.d/skeleton"
system( "/bin/mv rc.d/skeleton /etc/rc.d/skeleton" )

print "\x1b[1;32mINSTALLATION COMPLETE\x1b[0m"
print "\x1b[1;31mPLEASE EDIT\x1b[0m /etc/initconf.py to configure Forty-two."

# End of file
#
