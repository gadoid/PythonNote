import tkinter as tk
import time
main=tk.Tk()
current_time=0
clock_status=False
main.geometry("800x500")
def start_clock():
    global clock_status
    global show_content
    clock_status=True
    a = 0
    while clock_status and a<4 :
        show_content=clock(0,show_content)
        a+=1


def shutdown_clock():
    global clock_status
    clock_status=False
# def clock(time,ob=show_content):
#     ob.destroy()
#     time+=1
#     show_content=tk.Label(text=time)
#     show_content.pack()
#     return show_content
def clock(time=0):
    global current_time
    current_time+=1
show_content=tk.Label(text=current_time)
show_content.bind(clock()) 
show_content.pack() 
main.title("番茄时间")
label=tk.Label(text="番茄")
start_button=tk.Button(text="开始",command=start_clock)
start_button.pack()
shutdown_button=tk.Button(text="停止",command=shutdown_clock())
shutdown_button.pack()
label.pack()
while True:
    time.sleep(1)
    clock()
    main.mainloop()

# 文件处理
# 处理模式 w 写入，原有内容清空 r 只读模式 a 追加模式

# 异常处理 try...except...else...finally
