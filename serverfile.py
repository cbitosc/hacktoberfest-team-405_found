import socket
port=int(raw_input())
addr=('192.168.100.177',port)
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(addr)
server.listen(3)
client,addr=server.accept()
print addr
while True:
	data=client.recv(1024)
	print"CLIENT>",data
	udata=raw_input()
	print"SERVER>",udata
	client.send(udata)
	if udata=='NO':
		break
server.close()

