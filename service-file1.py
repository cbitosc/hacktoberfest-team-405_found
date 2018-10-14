from Tkinter import *
import time;
import socket
port=int(raw_input())
addr=('192.168.100.177',port)
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(addr)
server.listen(3)
print "success"
client,addr=server.accept()
print "success"
i=2
root=Tk()
root.title("Message Commute")
root.geometry("400x600")
localtime = time.asctime( time.localtime(time.time()) )
topF=Frame(root,width=400)
bottomF=Frame(root,width=400)
topF.pack()
bottomF.pack(side=BOTTOM)
data=client.recv(1024)
sampleL3=Label(topF,text="Client:" + data,fg="orange")
sampleL3.grid(row=1,column=0,sticky=W)
def fun():
        global i
        client.send(E1.get())
        sampleL2=Label(topF,text="ME:" + E1.get(),fg="blue")
        sampleL2.grid(row=i,column=1,sticky=E)
        i=i+1
        data=client.recv(1024)
        sampleL4=Label(topF,text="Client:" + data,fg="orange")
        sampleL4.grid(row=i,column=0,sticky=W)
        i=i+1
        E1.delete(0,END)

E1=Entry(bottomF)
E1.grid(row=0)
B=Button(bottomF,text="Send",bg="green",command=fun)
B.grid(row=0,column=1,sticky=E)
sampleL1=Label(topF,text=localtime,fg="green")
sampleL1.grid(row=0,sticky=W)


root.mainloop()


