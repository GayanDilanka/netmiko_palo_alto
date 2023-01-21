#Configure Mutiple palo alto devices

from netmiko import ConnectHandler
import time 


#This code part will put your firewalls commands into a list. 
with open('commands.txt') as f:
	commands_to_send = f.read().splitlines()

	#print(commands_to_send)



#This code block make a list of IPs 
with open('ips.txt') as f:
	ip_addresses = f.read().splitlines()


#This loop will log in to each of the device and do the configurations
for ip in ip_addresses:
    device = {
        'device_type': 'paloalto_panos',
        'ip': ip,
        'username': 'admin',
        'password': 'abc123'
    }
    #print(device)

    #start the session with the device 
	net_connect = ConnectHandler(**device)
	time.sleep(4)
	print("Connection Success")

	output = net_connect.send_config_set(commands_to_send)
	commit = net_connect.commit(read_timeout=300)
	
	time.sleep(30)
	#print the command output
	print (output)
	print(commit)
	net_connect.disconnect()






