# port-scanner
I have created a python script that scans the most popular ports on a target IP to determine whether or not they are open. 
Active reconnaissance like this is one of the most popular methods to perform network snooping before engaging in a cyber attack. 
Port Scanning is identified as Technique T0846 on the MITRE ATT&CK framework and is classified as a method of remote discovery
## What it does
- Scans a target IP for all common ports to see if there are any open ports 
- Checks if the connection attempt is successful indicating an open port
- Prints to the screen if a port is open and a summary of how many open ports there are at the end
## How it Works
- It first defines the target IP and creates a socket to be used for the connection
- Then we use connect_ex to connect to the specified ip and port combination
- This is then looped through the most popular ports and prints the open ports to the screen

## Sample Output
```
Scanning Common Ports
Port 22 SSH is open
Port 80 HTTP is open
Port 3389 RDP is open
Scan complete. 3 open ports found
```
## Note: Only use this tool on systems or networks you have permission to scan. 
