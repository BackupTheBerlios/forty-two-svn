#
# /etc/initconf.py: Forty-two (init) configuration file
# Linked to /etc/rc.conf
# Copyright 2004 Forty-two <http://forty-two.berlios.de>
# Released under a BSD license
#
############################################### 
# If you don't want to use a certain variable #
# (like font or keymap)                       # 
# DO NOT comment it out; set it to ""         #
# Example: FONT = ""                          #
# See man initconf.py for details             #
###############################################
#

# Set the timezone below
# Timezones can be found in /usr/share/zoneinfo
# Example: TIMEZONE = "US/Eastern"
TIMEZONE = "GMT"

# Set the hostname below
# Example: HOSTNAME = "myhost"
HOSTNAME = "myhost"

# Change the default console font here
# Example: FONT = "font name"
FONT = ""

# Change the default keymap here
# Example: KEYMAP = "keymap name"
KEYMAP = ""

# Configure the network here
# Set the loopback address
# Leaving it as 127.0.0.1 is recommended
LO = "lo 127.0.0.1"

# Now configure devices
# Each variable in the array will be considered one device
# For example: DEVICES = [ "dhcp" ]
# would make eth0 use DHCP
# If you have multiple NIC's, see the initconf.py man page
# To not use DHCP, set this to
# DEVICES = [ "eth0 10.0.0.1 netmask 255.255.255.0 broadcast 10.0.0.255" ]
# (of course, using your IP addresses)
DEVICES = [ "dhcp" ]

# Now say which interfaces to start on boot
# Put a number in here
# For example, to have eth0 and eth1 start, you would set it to
# INTERFACES = [ 0, 1 ]
INTERFACES = [ 0 ]

# Set modules to load on boot here
# Example: MODULES = [ "tulip", "i810_audio", "usb-storage" ]
MODULES = [ "ide-scsi" ]

# If you would like to have files backed up to /var/backup on boot, say yes here
# Example: BACKUP = "yes"
BACKUP = "yes"

# Now list files you would like backed up
# Use their full path. Wildcards (*) may be used
# Example: BACKUPS = [ "/etc/initconf", "/home/bob/important_file.txt" ]
BACKUPS = [ "/etc/initconf", "/etc/fstab" ]

# Now list services to start on boot
# Use the name that its /etc/rc.d/ script uses
# For example, Apache is httpd
# Example of usage: DAEMONS = [ "syslogd-ng", "crond", "net" ]
DAEMONS = [ "syslogd-ng", "crond", "net" ]

# End of file
# 
