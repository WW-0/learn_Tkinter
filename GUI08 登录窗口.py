import tkinter as tk
from tkinter import messagebox
import pickle

window=tk.Tk()
window.title('登录界面')
window.geometry('600x400')

C=tk.Canvas(window,width=600,height=200)
image_file=tk.PhotoImage(file='002.gif')
image=C.create_image(0,0,anchor='nw',image=image_file)
C.pack(side='top')

L1=tk.Label(window,text='用户名',relief='groove').place(x=200,y=240)
L2=tk.Label(window,text='密　码',relief='groove').place(x=200,y=270)

var_username=tk.StringVar()
var_username.set('example@python.com')
E1=tk.Entry(window,textvariable=var_username).place(x=250,y=240)
var_password=tk.StringVar()
E2=tk.Entry(window,textvariable=var_password,show='*').place(x=250,y=270)

def sign_in():
    user_name=var_username.get()
    user_pwd=var_password.get()
    try:
        with open('user_info.pickle','rb') as user_file:
            user_info=pickle.load(user_file)
    except FileNotFoundError:
        with open('user_info.pickle','wb') as user_file:
            user_info={'admin':'admin'}
            pickle.dump(user_info,user_file)

    if user_name in user_info:
        if user_pwd==user_info[user_name]:
            tk.messagebox.showinfo(title='Welcome',message='Hi,'+user_name)

        else:
            tk.messagebox.showerror(message='Erroe,password is wrong,try again')
    else:
        is_sign_up=tk.messagebox.askyesno('Welcome','You have not sign up yet. Sign up today?')
        if is_sign_up:
            sign_up()

def sign_up():
    pass

B1=tk.Button(window,text='登录',command=sign_in).place(x=230,y=310)
B2=tk.Button(window,text='注册',command=sign_up).place(x=320,y=310)
window.mainloop()
