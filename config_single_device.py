#Scipt for config single  palo-alto device

from netmiko import ConnectHandler
import time 


#Define the device details
device = {
	'device_type': 'paloalto_panos',

	'ip': '192.168.10.230', #Give the IP address of the device
	'username': 'admin', # Give the username inside the '' 
	'password': 'abc123' # Give the password ''
}





#This code part will put your firewalls commands into a list. 
with open('commands.txt') as f:
	commands_to_send = f.read().splitlines()

	print(commands_to_send)


#start the session with the device 
net_connect = ConnectHandler(**device)
time.sleep(4)
print("Connection Success")

#Send the commands to firewall
output = net_connect.send_config_set(commands_to_send)

#Commit the Changes
commit = net_connect.commit(read_timeout=300)

time.sleep(30)
#print the command output
print (output)
print(commit)

#Disconnet from devics
net_connect.disconnect()

