#
# /etc/initconf.py: Init configuration file
# Linked to /etc/rc.conf
# Copyright 2004 Forty-two <http://forty-two.berlios.de>
# Released under a BSD license
#
# If you don't want to use a certain variable
# (like font or keymap)
# DO NOT comment it out; set it to ""
# Example: font = ""
#
# Todo:
# Add an option for booting parallely
#

# Set the timezone below
# Timezones can be found in /usr/share/zoneinfo
# Example: timezone = "US/Eastern"
timezone = "GMT"

# Set the hostname below
# Example: hostname = "myhost"
hostname = "myhost"

# Change the default console font here
# Example: font = "font name"
font = ""

# Change the default keymap here
# Example: keymap = "keymap name"
keymap = ""

# Set modules to load on boot here
# Example: modules = [ "tulip", "i810_audio", "usb-storage" ]
modules = [ "ide-scsi" ]

# If you would like to have files backed up to /var/backup on boot, say yes here
# Example: backup = "yes"
backup = "yes"

# Now list files you would like backed up
# Use their full path. Wildcards (*) may be used
# Example: backups = [ "/etc/initconf", "/home/bob/important_file.txt" ]
backups = [ "/etc/initconf", "/etc/fstab" ]

# Now list services to start on boot
# Use the name that its /etc/rc.d/ script uses
# For example, Apache is httpd
# Example of usage: daemons = [ "syslogd-ng", "crond", "net" ]
daemons = [ "syslogd-ng", "crond", "net" ]

# End of file
# 
