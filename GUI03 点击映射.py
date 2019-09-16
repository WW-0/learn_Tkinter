import tkinter as tk

window=tk.Tk()
window.title('点击')
window.geometry('200x200')
var1=tk.StringVar()
L=tk.Label(window,bg='yellow',width=20,textvariable=var1).pack()

def print_L():
    var=LB.get(LB.curselection())
    var1.set(var)

B=tk.Button(window,text='print_L',width=15,height=2,command=print_L).pack()

var2=tk.StringVar()
var2.set((1,2,3))
LB=tk.Listbox(window,listvariable=var2)

list_items=[5,6,7,8]
for item in list_items:
    LB.insert('end',item)  #插入字符
LB.insert(1,'first')
LB.insert(2,'second')
#LB.delete(2)                #删除第二个位置的字符
LB.pack()


window.mainloop()
