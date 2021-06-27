import tkinter as TK
top=TK.Tk()
top.title("标题")
screen_width,screen_height= top.maxsize()
width=240
height=480
align_Str= "%dx%d+%d+%d" %(width,height,(screen_width-width)//2,(screen_height-height)//2)
top.geometry(align_Str)
user_name_lable=TK.Label(top,text="登录")
user_name_lable.place(x=10,y=20)
top.mainloop()