import socket

host= "127.0.0.1"
ports= [22,80,443,631,3000]

for port in ports:
  s= socket.socket()
  s.settimeout(1)
  result= s.connect_ex((host,port))
  s.close()

  if result==0:
      print(f"Port{port} is open on {host}")
else:
      print(f"Port{port} is closed on {host}")