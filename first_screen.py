from Tkinter import *
root8=Tk()
def fun():
    root8.destroy()
    r=Tk()
    def fun2():
        r.destroy()
        import bank
    a1=PhotoImage(file='cc.gif')
    l1=Label(r,image=a1)
    l1.after(5000,fun2)
    l1.pack()
    r.mainloop()
a=PhotoImage(file='debit.gif')
l=Label(root8,image=a)
l.after(5000,fun)
l.pack()
root8.mainloop()
