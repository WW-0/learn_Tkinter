import tkinter as tk

window=tk.Tk()
window.title('my code')
window.geometry('200x100')

var=tk.StringVar()
L=tk.Label(window,textvariable=var,bg='yellow',
           font=('Arial',12),width=15,height=2)
L.pack()



flag=False
def hit_me():
    global flag
    if flag==False:
        flag=True
        var.set('你点我')
    else:
        flag=False
        var.set('')
B=tk.Button(window,text='点我',width=15,height=2,
            command=hit_me)
B.pack()

window.mainloop()