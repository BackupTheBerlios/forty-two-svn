#!/usr/bin/python
#
# System boot script
# Copyright 2004 Forty-two <http://forty-two.berlios.de>
# Released under a BSD license
#

# Variables needed from /etc/rc.conf:
# timezone
# hostname

# Load the system module
from os import system
from os import path

print "Forty-two is booting the system...\n"

# Here we would normally load rc.conf
# Since we don't have an rc.conf I'm skipping it

# Start devfsd below
# I would have started pts, but I don't know what daemon to start...
# We will use PTS eventually.

system( "/sbin/devfsd /dev" )

# Activate swap partition

system( "/sbin/swapon -a" )

# Mount root (/) read-only
system( "/bin/mount -n -o remount,ro /" )

# Check filesystems for errors
# This can be commented out to improve boot time
system( "/sbin/fsck -A -T -C -a" )
tmp = system( "/bin/echo $?" ) # The shell variable $?
if tmp > 1: # If the filesystem is bad
	print "************ ERROR: FILESYSTEM CHECK FAILED *************\n"
	print "**                                                     **\n"
	print "** You will now enter a shell to repair this manually. **\n"
	print "** You will then be rebooted.                          **\n"
	print "*********************************************************\n"
	#Give them a shell then reboot the system
	system( "/sbin/sulogin -p" )
	print "Forty-two is rebooting the system...\n"
	system( "/bin/umount -a" )
	system( "/bin/mount -n -o remount,ro /" )
	system( "/sbin/reboot -f" )
	exit # Kill the script

# Mount filesystems
system( "/bin/mount -n -o remount,rw /" )
system( "/bin/rm -f /etc/mtab*" )
system( "/bin/mount -a -O no_netdev" )

# Clean up miscellaneous files

# I don't know what this does so I'm not including it yet
# When the time comes I'll uncomment it
# system( "/var/run/utmp" )

system( "/bin/rm -rf /forcefsck /fastboot /etc/nologin /etc/shutdownpid /var/run/*.pid /var/lock/* /tmp/* &> /dev/null" )

# Set kernel variables
system( "/sbin/sysctl -p > /dev/null" )

# Update shared library links
system( "/sbin/ldconfig" )

# Configure hostname
if hostname:
	print "Setting hostname to",hostname,"\n"
	#Set the hostname
	tmp = "/bin/hostname",hostname
	system( tmp )

# Load random seed
# Returns true if /var/tmp/random-seed exists
tmp = path.exists( "/var/tmp/random-seed" )
if tmp:
	system( "/bin/cat /var/tmp/random-seed > /dev/urandom" )

# Set the clock
tmp = path.exists( "/etc/adjtime" )
if tmp:
	break
else:
	system( "/bin/echo \"0.0 0 0.0\" > /etc/adjtime" )

if timezone:
	tmp = "/bin/ln -sf /usr/share/zoneinfo/",timezone,"
