import socket
import sys
# define IP
ip = "10.10.10.10"

 
#used to test connections 
print("Scanning Common Ports")
Open_Ports=0
# Define range of ports to scan 
CommonPorts = [21, 22, 23, 25, 53, 69, 80, 88, 135, 139, 443, 445, 1433, 3306, 3389, 5985, 8080, 8443]
PortNames = {
    21: "FTP" , 22: "SSH", 23: "Telnet" , 25: "SMTP", 53: "DNS", 69: "TFTP", 80: "HTTP", 88: "Kerberos",
    135: "RPC", 139: "NetBIOS", 443: "HTTPS", 445: "SMB", 1433: "MSSQL", 3306: "MySQL", 3389: "RDP", 5985:"WinRM",
    8080: "HTTP-Alt", 8443: "HTTPS-ALT"
}

for p in CommonPorts:
    s = socket.socket(family = socket.AF_INET, type = socket.SOCK_STREAM, proto = 0, fileno = None)
    s.settimeout(0.3)
    result = s.connect_ex((ip, p))
    # if connection succeeds print , else move to next port
    if result == 0:
        print(f"Port {p} {PortNames.get(p, 'Unknown')} is open")
        Open_Ports = Open_Ports + 1

# print summary of open ports within port range
print (f"Scan complete. {Open_Ports} open ports found")




