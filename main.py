from datetime import datetime
import os
import time

from tkinter import Tk, Label, BOTH, RAISED, Frame, Entry, Button, DISABLED

temp = 0
temp_id = ''
os.environ['TZ'] = 'UTC'
time.tzset()


def timer():
    global temp, temp_id
    temp_id = timer_frame.after(1000, start_timer_command)
    time_format = datetime.fromtimestamp(temp).strftime('%H:%M:%S')
    start_timer_time.configure(text=time_format)
    temp += 1


def start_timer_command():
    timer()
    start_timer_button.grid_forget()
    pause_timer_button.grid(row=0, column=1)
    stop_timer_button.grid(row=0, column=2)


def pause_timer_command():
    timer_frame.after_cancel(temp_id)
    pause_timer_button.grid_forget()
    continue_timer_button.grid(row=0, column=1)


def continue_timer_command():
    timer()
    continue_timer_button.grid_forget()
    pause_timer_button.grid(row=0, column=1)


def stop_timer_command():
    global temp
    timer_frame.after_cancel(temp_id)
    time_format = datetime.fromtimestamp(temp).strftime('%H:%M:%S')
    pause_timer_button.grid_forget()
    continue_timer_button.grid_forget()
    start_timer_button.grid(row=0, column=1)
    print(f'Worked time {time_format}')
    temp = 0
    start_timer_time.configure(text='00:00:00')


root = Tk()
history_frame = Frame(root, height=100, width=100, borderwidth=1, background='red')
history_frame.grid(row=0, column=0)

timer_frame = Frame(root, height=100, width=100, borderwidth=1, background='blue')
timer_frame.grid(row=0, column=1)
time_entry_description_input = Entry(timer_frame, width=30, borderwidth=2)
time_entry_description_input.grid(row=0, column=0)
start_timer_button = Button(timer_frame, text='Start', padx=5, pady=5, command=start_timer_command)
pause_timer_button = Button(timer_frame, text='Pause', padx=5, pady=5, command=pause_timer_command)
continue_timer_button = Button(timer_frame, text='Continue', padx=5, pady=5, command=continue_timer_command)
stop_timer_button = Button(timer_frame, text='Stop', padx=5, pady=5, command=stop_timer_command)
start_timer_button.grid(row=0, column=1)
start_timer_time = Label(timer_frame, width=10, text='00:00:00')
start_timer_time.grid(row=1, column=1)

root.mainloop()
