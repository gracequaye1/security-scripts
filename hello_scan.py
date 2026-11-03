import socket

host = input("Enter the host to scan (press Enter for your own laptop): ")

if host == "":
    host = "127.0.0.1"
port_text = input("Enter ports separated by commas (press Enter for the default list): ")

if port_text == "":
    ports = [22, 80, 443, 631, 3000]
else:
    ports = [int(p) for p in port_text.split(",")]

for port in ports:
  s= socket.socket()
  s.settimeout(1)
  result= s.connect_ex((host,port))
  s.close()

  if result==0:
      print(f"Port{port} is open on {host}")
else:
      print(f"Port{port} is closed on {host}")