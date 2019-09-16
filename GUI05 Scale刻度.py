import tkinter as tk

window=tk.Tk()
window.title('scale 使用')
window.geometry('400x400')

var=tk.StringVar()
L=tk.Label(window,bg='green',width=20,height=2,textvariable=var).pack()

def print_L(v):
    var.set(v)
S=tk.Scale(window,label='try me',from_=0,to=20,orient=tk.HORIZONTAL,
           length=300,showvalue=1,tickinterval=2,resolution=0.01,command=print_L).pack()

window.mainloop()
