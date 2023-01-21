#Script to check the confurations

from netmiko import ConnectHandler

#Define the device details
device = {
    'device_type': 'paloalto_panos',

    'ip': '192.168.10.230', #Give the IP address of the device
    'username': 'admin', # Give the username inside the '' 
    'password': 'abc123' # Give the password ''
}


#start the session with the device 
net_connect = ConnectHandler(**device)

#Pass a sample command to check the code
output = net_connect.send_command('show admins',expect_string=">")

#print the command output
print (output)