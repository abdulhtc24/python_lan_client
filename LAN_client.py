#LAN_client.py
import socket, atexit, time
def cleanup():
	sock.send("quit\n")
	sock.close()
atexit.register(cleanup)
sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.connect(("IP",<port>))
sock.send("T?\n")
time.sleep(0.1)
reply=sock.recv(1000);
ptint(reply.strip())
