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
lo = "lo 127.0.0.1"

# Now configure devices
# If you do not have DHCP, put in here whatever
# you would normally put in when you do a
# /sbin/ifconfig (to start the network)
# If you do have DHCP, just say eth0 = "dhcp"
#
# If you have eth1, eth2, etc. state them here, as well
eth0 = "dhcp"

# List interface to start on boot here
# For example, it could be something like:
# INTERFACES = [ lo, eth0, eth1 ]
INTERFACES = [ lo, eth0 ]

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
