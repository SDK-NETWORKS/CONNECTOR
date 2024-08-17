
<h1 align="center">
  <img src="Static/connector.png" alt="Connector">
  <br>
</h1>

🚀 Just wrapped up a Telnet automation script! 💻 This Python tool allows seamless interaction with Devices, making it easy to connect, authenticate, and execute commands directly from the terminal. 🔄


# Features

1.Telnet Connection Handling: 
- The script allows users to establish a Telnet connection to a network switch using its IP address.
- Includes IP address validation to ensure that users input a valid IP address before attempting to connect.
 
2.User Authentication: 
- Prompts for username and password credentials, with support for hidden password input using the getpass module.
- Handles authentication and confirms successful login by detecting the switch's prompt.

3.Interactive Command Execution: 
- Once logged in, users can execute multiple commands interactively on the switch.
- Outputs the results of each command execution, providing real-time feedback.

4.Error Handling and User-Friendly Interface: 
- The script includes robust error handling for failed connections, invalid credentials, and unexpected errors.
- Provides clear prompts and error messages, improving user experience.

5.Graceful Exit: 
- Supports user interruptions with **Ctrl+C**, allowing users to exit loops and close the Telnet session cleanly.
- Automatically closes the Telnet connection when the user is done.

6.Timeout Mechanism: 
- Includes a timeout mechanism during command execution to prevent the script from hanging indefinitely.

7.Customization: 
- The script can be easily adapted to work with different network devices or extended with additional features, such as logging or batch command execution.

**CONNECTOR** is a powerful tool that can be used to connect to your remote devices . It is easy to use and can be run on any platform.

# Available On :

- 𝙇𝙄𝙉𝙐𝙓

- 𝙏𝙀𝙍𝙈𝙐𝙓

- 𝙒𝙄𝙉𝘿𝙊𝙒𝙎
# CONNECTOR Installation

```
git clone https://github.com/SDK-NETWORKS/CONNECTOR
cd CONNECTOR
chmod +x Telnet.py
```

# Running CONNECTOR

This will Run **CONNECTOR** Tool.

```
python3 Telnet.py 
```
<h1 align="left">
  <img width="500" alt="Connector" src="Static/example.png">
  <br>
</h1>

**CONNECTOR IS MADE WITH 🖤 BY SDK-NETWORKS.**
