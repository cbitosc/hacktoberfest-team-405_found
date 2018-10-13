from tkinter import *

root=Tk()
i=1	
topF=Frame(root,width=40)
bottomF=Frame(root,width=40)
bottomF.pack(side=BOTTOM)
topF.pack()
def fun():
	global i
	sampleL2=Label(topF,text=E1.get(),fg="blue")
	sampleL2.grid(row=i,column=1,sticky=E)
	i=i+1
	E1.delete(0,END)
E1=Entry(bottomF)
E1.grid(row=0)
B=Button(bottomF,text="Send",bg="green",command=fun)
B.grid(row=0,column=1)
sampleL1=Label(topF,text="sampleL1",fg="green")
sampleL1.grid(row=0,sticky=W)


root.mainloop()
