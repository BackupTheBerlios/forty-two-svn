#
# /etc/rc.d/Makefile - used for parallel booting: DO NOT EDIT!!
# 
# Editors: undeadpenguin
#

# Use like /etc/rc.d/Makefile ACTION=start/stop/restart
$ACTION=

include deps.mk

default : $(ALL)
	/etc/rc.d/$(ALL) $(ACTION) > /var/log/parallel
