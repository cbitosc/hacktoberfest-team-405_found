from tkinter import *
import time;
root=Tk()
root.title("Message Commute")
root.geometry("400x600")
i=1
localtime = time.asctime( time.localtime(time.time()) )
topF=Frame(root,width=160,bg="black")
bottomF=Frame(root,width=160)
bottomF.pack(side=BOTTOM)
topF.pack()
def fun():
        global i
        sampleL2=Label(topF,text="ME:" + E1.get(),fg="blue")
        sampleL2.grid(row=i,column=1,sticky=E)
        i=i+1
        E1.delete(0,END)
E1=Entry(bottomF)
E1.grid(row=0)
B=Button(bottomF,text="Send",bg="green",command=fun)
B.grid(row=0,column=1,sticky=E)
sampleL1=Label(topF,text=localtime,fg="green")
sampleL1.grid(row=0,sticky=W)


root.mainloop()

