from tkinter import *

root=Tk()

topF=Frame(root,height=300)
bottomF=Frame(root)
bottomF.pack(side=BOTTOM)
topF.pack()
Ec=Entry(topF)
E=Entry(topF)
E.grid(row=10)
Ec.grid(row=10,column=1)

E1=Entry(bottomF)
E1.grid(row=0)
B=Button(bottomF,text="Send",bg="green")
B.grid(row=0,column=1)
root.mainloop()

