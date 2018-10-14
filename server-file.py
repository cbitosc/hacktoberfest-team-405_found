from Tkinter import *
import time;
import socket
port=int(raw_input())
addr=('192.168.100.177',port)
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(addr)
print "success"
server.listen(3)
client,addr=server.accept()
print "success"
root=Tk()
root.title("Message Commute")
root.geometry("400x600")
i=0
localtime = time.asctime( time.localtime(time.time()) )
topF=Frame(root,width=160)
bottomF=Frame(root,width=160)
topF.pack()
bottomF.pack(side=BOTTOM)
def fun():
        global i   
        sampleL2=Label(topF,text="ME:" + E1.get(),fg="blue")
        sampleL2.grid(row=i,column=1,sticky=E)
        i=i+1
        E1.delete(0,END)
data=client.recv(1024)
sampleL3=Label(topF,text="Client :" + data,fg="orange")
sampleL3.grid(row=i,column=0,sticky=W)
E1=Entry(bottomF)
E1.grid(row=0)
B=Button(bottomF,text="Send",bg="green",command=fun)
B.grid(row=0,column=1,sticky=E)
sampleL1=Label(topF,text=localtime,fg="green")
sampleL1.grid(row=0,sticky=W)
root.mainloop()

