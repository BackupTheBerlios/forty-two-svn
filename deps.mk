#
# /etc/rc.d/deps.mk - Service dependencies
#

# Put all services to be started here
$ALL= service_name service2_name

# List service dependencies here
service_name : dependency_name
service2_name : dependency2_name
