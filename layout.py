from tkinter import *

root=Tk()

topF=Frame(root,height=300)
bottomF=Frame(root)
bottomF.pack(side=BOTTOM)
topF.pack()

E1=Entry(bottomF)
E1.grid(row=0)
B=Button(bottomF,text="Send",bg="green")
B.grid(row=0,column=1)
root.mainloop()
