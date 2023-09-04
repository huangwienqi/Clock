import time
import tkinter as tk

def start_timer():
    countdown(25 * 60)  # 设置25分钟倒计时

def countdown(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        timer_label.config(text=timeformat)
        time.sleep(1)
        seconds -= 1
    timer_label.config(text="Time's up!")

root = tk.Tk()
root.title("专注时钟")

timer_label = tk.Label(root, font=("Helvetica", 48), fg="red")
timer_label.pack(pady=20)

start_button = tk.Button(root, text="开始", command=start_timer)
start_button.pack(pady=10)

root.mainloop()
