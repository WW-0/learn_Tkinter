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
    def sign_to_Mofan_Python():
        np = new_pwd.get()
        npf = new_pwd_confirm.get()
        nn = new_name.get()
        with open('user_info.pickle', 'rb') as usr_file:
            exist_usr_info = pickle.load(usr_file)
        if np != npf:
            tk.messagebox.showerror('Error', 'Password and confirm password must be the same!')
        elif nn in exist_usr_info:
            tk.messagebox.showerror('Error', 'The user has already signed up!')
        else:
            exist_usr_info[nn] = np
            with open('user_info.pickle', 'wb') as usr_file:
                pickle.dump(exist_usr_info, usr_file)
            tk.messagebox.showinfo('Welcome', 'You have successfully signed up!')
            window_sign_up.destroy()
    window_sign_up = tk.Toplevel(window)
    window_sign_up.geometry('350x200')
    window_sign_up.title('Sign up window')

    new_name = tk.StringVar()
    new_name.set('example@python.com')
    tk.Label(window_sign_up, text='User name: ').place(x=10, y= 10)
    entry_new_name = tk.Entry(window_sign_up, textvariable=new_name)
    entry_new_name.place(x=150, y=10)

    new_pwd = tk.StringVar()
    tk.Label(window_sign_up, text='Password: ').place(x=10, y=50)
    entry_usr_pwd = tk.Entry(window_sign_up, textvariable=new_pwd, show='*')
    entry_usr_pwd.place(x=150, y=50)

    new_pwd_confirm = tk.StringVar()
    tk.Label(window_sign_up, text='Confirm password: ').place(x=10, y= 90)
    entry_usr_pwd_confirm = tk.Entry(window_sign_up, textvariable=new_pwd_confirm, show='*')
    entry_usr_pwd_confirm.place(x=150, y=90)

    btn_comfirm_sign_up = tk.Button(window_sign_up, text='Sign up', command=sign_to_Mofan_Python)
    btn_comfirm_sign_up.place(x=150, y=130)

B1=tk.Button(window,text='登录',command=sign_in).place(x=230,y=310)
B2=tk.Button(window,text='注册',command=sign_up).place(x=320,y=310)
window.mainloop()
