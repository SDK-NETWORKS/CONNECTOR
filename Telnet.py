print('''

 ██████╗ ██████╗ ███╗   ██╗███╗   ██╗███████╗ ██████╗████████╗ ██████╗ ██████╗ 
██╔════╝██╔═══██╗████╗  ██║████╗  ██║██╔════╝██╔════╝╚══██╔══╝██╔═══██╗██╔══██╗
██║     ██║   ██║██╔██╗ ██║██╔██╗ ██║█████╗  ██║        ██║   ██║   ██║██████╔╝
██║     ██║   ██║██║╚██╗██║██║╚██╗██║██╔══╝  ██║        ██║   ██║   ██║██╔══██╗
╚██████╗╚██████╔╝██║ ╚████║██║ ╚████║███████╗╚██████╗   ██║   ╚██████╔╝██║  ██║
 ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═══╝╚══════╝ ╚═════╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝
                                                                                                                                                                                                                                                                          
    ''')

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
import telnetlib
import time
import re

# Establish a Telnet connection
while True:
    try:
        # Define your switch details and credentials
        SWITCH_IP = input("Enter The IP Address Of The Devices: ")

        # Validate IP address
        if not re.match(r"^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$", SWITCH_IP):
            print("Invalid IP Address. Please Enter a Valid IP Address.")
            time.sleep(1)
            continue

        tn = telnetlib.Telnet(SWITCH_IP)
        print(f"Connected To {SWITCH_IP}")
        break
    except Exception as e:
        print(f"Failed To Connect To {SWITCH_IP}: {e}")
        time.sleep(1)
        continue
    except KeyboardInterrupt:
        print("\nExiting From Script")
        exit(0)

# Login to the switch
while True:
    try:
        USERNAME = input("Enter Your Username: ")
        PASSWORD = input("Enter Your Password: ")

        tn.read_until(b"Username: ")
        tn.write(USERNAME.encode('ascii') + b"\n")
        tn.read_until(b"Password: ")
        tn.write(PASSWORD.encode('ascii') + b"\n")

        # Check if login was successful
        output = tn.read_until(b">", 1).decode('ascii')
        if ">" in output:
            print("Login Successful!")
            break
        elif "#" in output:
            print("Login Successful!")
            break
        elif "<" in output:
            print("Login Successful!")
            break
        else:
            print("Invalid Username Or Password. Try Again!")
    except KeyboardInterrupt:
        print("\nExiting From Script")
        exit(0)

print("Wait Few Seconds To Show Output")
tn.write(b"terminal length 0\n")

# Send a newline character to get the initial output
tn.write(b"\n")

# Wait for the output to be displayed
output = ''
start_time = time.time()
while True:
    line = tn.read_until(b'\n', 1).decode('ascii')
    if line.strip() == '':
        if time.time() - start_time > 10:  # Wait for 10 seconds for the output to be displayed
            break
        continue
    output += line
print(output)

while True:
    try:
        # Ask the user for the command to execute
        COMMAND = input("Enter The Command To Execute On The Devices: ")

        # Execute command
        tn.write(COMMAND.encode('ascii') + b"\n")

        # Wait for the command to execute and output to be displayed
        output = ''
        start_time = time.time()
        while True:
            line = tn.read_until(b'\n', 1).decode('ascii')
            if line.strip() == '':
                if time.time() - start_time > 10:  # Wait for 10 seconds for the output to be displayed
                    break
                continue
            output += line
        print(output)
    except EOFError:
        break
    except KeyboardInterrupt:
        break

# Close the Telnet connection
tn.write(b"exit\n")
tn.close()
print("\nConnection Closed.")