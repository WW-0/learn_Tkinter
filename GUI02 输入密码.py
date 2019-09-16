import tkinter as tk

window=tk.Tk()
window.title('输入密码')
window.geometry('200x200')

E=tk.Entry(window,show=None)
E.pack()
def insert_point():
    var=E.get()
    T.insert('insert',var)
def insert_end():
    var=E.get()
    T.insert('end',var)
B1=tk.Button(window,text='insert point',width=15,height=2,command=insert_point)
B1.pack()
B2=tk.Button(window,text='insert end',command=insert_end)
B2.pack()

T=tk.Text(window,height=2)
T.pack()

window.mainloop()