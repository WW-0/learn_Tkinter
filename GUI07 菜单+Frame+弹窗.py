import tkinter as tk
import tkinter.messagebox
window=tk.Tk()
window.title('Menubar')
window.geometry('200x200')


L1=tk.Label(window,width=20,height=2,bg='yellow')
L1.pack()
counter=0
def do_job():
    global counter
    L1.config(text='do'+str(counter))
    counter+=1

menubar=tk.Menu(window)#创建一个菜单栏相当于一个容器在窗口上方

filemenu=tk.Menu(menubar,tearoff=0) #定义一个空菜单单元   tearoff 能否被分开
menubar.add_cascade(label='File',menu=filemenu)#将上面定义的空菜单命名为`File`，放在菜单栏中，就是装入那个容器中
filemenu.add_command(label='New',command=do_job)
filemenu.add_command(label='Open',command=do_job)
filemenu.add_command(label='Save',command=do_job)
filemenu.add_separator()#分割线
filemenu.add_command(label='Exit',command=window.quit)

submenu=tk.Menu(filemenu,tearoff=0)#和上面定义菜单一样，不过此处是在`File`上创建一个空的菜单
filemenu.add_cascade(label='import',menu=submenu,underline=0)#给放入的菜单`submenu`命名为`Import`
submenu.add_command(label='submenu1',command=do_job)


editmenu=tk.Menu(menubar,tearoff=0) #定义一个空菜单单元   tearoff 能否被分开
menubar.add_cascade(label='Edit',menu=editmenu)#将上面定义的空菜单命名为`File`，放在菜单栏中，就是装入那个容器中
editmenu.add_command(label='Copy',command=do_job)
editmenu.add_command(label='Cut',command=do_job)
editmenu.add_command(label='Psate',command=do_job)

L2=tk.Label(window,text='on the window').pack()
frame=tk.Frame(window).pack()

###在刚刚创建的`frame`上创建两个`frame`，我们可以把它理解成一个大容器里套了一个小容器，即`frm`上有两个`frame` ，`frm_l`和`frm_r`
###这里是控制小的`frm`部件在大的`frm`的相对位置，此处`frm_l`就是在`frm`的左边，`frm_r`在`frm`的右边
frame_L=tk.Frame(frame)
frame_L.pack(side='left')   ###"""此处尤为重要，不能直接按快速写法写，否则pack内参数失效"""
frame_R=tk.Frame(frame)
frame_R.pack(side='right')
###这里的三个label就是在我们创建的frame上定义的label部件，还是以容器理解，就是容器上贴了标签，来指明这个是什么，解释这个容器。
tk.Label(frame_L, text='on the frame_L1').pack()##这个`label`长在`frm_l`上，显示为`on the frm_l1`
tk.Label(frame_L, text='on the frame_L2').pack()##这个`label`长在`frm_l`上，显示为`on the frm_l2`
tk.Label(frame_R, text='on the frame_R1').pack()##这个`label`长在`frm_r`上，显示为`on the frm_r1`

def win_message():
    tk.messagebox.showinfo(title='hi boy',message='hahhhahahah')# 提示信息对话窗
    tk.messagebox.showwarning(title='hi boy',message='hahhhahahah')  # 提出警告对话窗
    tk.messagebox.showerror(title='hi boy',message='hahhhahahah')  # 提出错误对话窗
    tk.messagebox.askquestion(title='hi boy',message='hahhhahahah')  # 询问选择对话窗
    print(tk.messagebox.askquestion())  # 返回yes和no
    print(tk.messagebox.askokcancel())  # 返回true和false
    print(tk.messagebox.askyesno())  # 返回true和false
    print(tk.messagebox.askretrycancel())  # 返回true和false

B=tk.Button(frame_R,height=2,text='hite me',command=win_message).pack()

window.config(menu=menubar)
window.mainloop()


