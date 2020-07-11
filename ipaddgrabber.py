import socket

websitename = input("Enter the website name: ")

ip = socket.gethostbyname(websitename)

print("The IP address of " + websitename + " is: " + ip)