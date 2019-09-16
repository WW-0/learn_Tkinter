import tkinter as tk

window=tk.Tk()
window.title('多选按钮+画布')
window.geometry('500x800')

L=tk.Label(window,bg='yellow',text='Empty',width=20,height=2)
L.pack()
def print_L():
    if (var1.get()==1)and(var2.get()==0):
        L.config(text='I love python')
    elif(var1.get()==0)and(var2.get()==1):
        L.config(text='I love c++')
    elif (var1.get() == 1)and(var2.get() == 1):
        L.config(text='I love both')
    else:
        L.config(text='I do not love either')
var1=tk.IntVar()
var2=tk.IntVar()
CB1=tk.Checkbutton(window,text='python',height=2,variable=var1,onvalue=1,offvalue=0,command=print_L).pack()
CB2=tk.Checkbutton(window,text='c++',height=2,variable=var2,onvalue=1,offvalue=0,command=print_L).pack()

canvas=tk.Canvas(window,bg='blue',width=500,height=500)
# image_file=tk.PhotoImage(file='001.gif')
# image=canvas.create_image(0,0,anchor='nw',image=image_file)
canvas.pack()
# x0,y0,x1,y1=100,100,150,150
# line=canvas.create_line(x0,y0,x1,y1)
# arc = canvas.create_arc(x0, y0, x1, y1, start=0, extent=90)  #创建一个扇形
rect = canvas.create_rectangle(10, 130, 10+50, 130+50)   #创建一个矩形
canvas.create_arc(10,10,100,80,extent=45)
canvas.create_arc(10,80,200,160,extent=90)
canvas.create_arc(10,160,200,240,extent=135)
canvas.create_arc(10,240,200,320,extent=180)
canvas.create_arc(10,320,200,400,extent=359)
def moveit():
    canvas.move(rect, 0, 2)

B=tk.Button(window,height=2,text='move',command=moveit).pack()
window.mainloop()
