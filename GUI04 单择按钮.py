import tkinter as tk

window=tk.Tk()
window.title('radiobutton')
window.geometry('200x200')

var=tk.StringVar()
L=tk.Label(window,bg='yellow',width=20,text='empty')
L.pack()
def print_L():
    L.config(text='you have selected '+var.get())

R1=tk.Radiobutton(window,text='option A',variable=var,value='A',command=print_L).pack()
R2=tk.Radiobutton(window,text='option B',variable=var,value='B',command=print_L).pack()
R3=tk.Radiobutton(window,text='option C',variable=var,value='C',command=print_L).pack()

window.mainloop()