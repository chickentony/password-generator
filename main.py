from datetime import datetime
import os
import time

from tkinter import Tk, Label, Frame, Entry, Button, DISABLED, NORMAL

temp = 0
temp_id = ''
os.environ['TZ'] = 'UTC'
time.tzset()


def timer():
    global temp, temp_id
    temp_id = root.after(1000, start_timer_command)
    time_format = datetime.fromtimestamp(temp).strftime('%H:%M:%S')
    start_timer_time.configure(text=time_format)
    temp += 1


def start_timer_command():
    timer()
    start_timer_button.grid_forget()
    pause_timer_button.grid(row=1, columnspan=2, sticky='ew')
    stop_timer_button['state'] = NORMAL


def pause_timer_command():
    root.after_cancel(temp_id)
    pause_timer_button.grid_forget()
    continue_timer_button.grid(row=1, columnspan=2, sticky='ew')


def continue_timer_command():
    timer()
    continue_timer_button.grid_forget()
    pause_timer_button.grid(row=1, columnspan=2, sticky='ew')


def stop_timer_command():
    global temp
    root.after_cancel(temp_id)
    worked_time = datetime.fromtimestamp(temp).strftime('%H:%M:%S')
    pause_timer_button.grid_forget()
    continue_timer_button.grid_forget()
    worked_time_record = Label(root, width=10, text=f'{worked_time}', font=('Mac', 10))
    worked_time_record.grid(row=3, columnspan=2, sticky='ew')
    start_timer_button.grid(row=1, columnspan=2, sticky='ew')
    print(f'Worked time {worked_time}')
    temp = 0
    start_timer_time.configure(text='00:00:00')
    stop_timer_button['state'] = DISABLED


root = Tk()
root.title('Timer')
root.geometry('500x500')
# history_frame = Frame(root, height=300, width=300, borderwidth=1, background='red')
# history_frame.grid(row=0, column=0)
# history_frame.grid_propagate(False)

# timer_frame = Frame(root, height=300, width=300, borderwidth=1, background='blue')
# timer_frame.grid(row=0, column=1)
# timer_frame.grid_propagate(False)
start_timer_time = Label(root, width=10, font=('Mac', 50), text='00:00:00')
start_timer_time.grid(row=0, columnspan=2)

# time_entry_description_input = Entry(root, width=20, borderwidth=1)
# time_entry_description_input.grid(row=0, column=3, columnspan=3)

start_timer_button = Button(root, text='Start', font=('Mac', 15), command=start_timer_command)
pause_timer_button = Button(root, text='Pause', font=('Mac', 15), command=pause_timer_command)
continue_timer_button = Button(
    root,
    text='Continue',
    font=('Mac', 15),
    command=continue_timer_command
)
stop_timer_button = Button(
    root, text='Stop', font=('Mac', 15), command=stop_timer_command, state=DISABLED
)

start_timer_button.grid(row=1, columnspan=2, sticky='ew')
stop_timer_button.grid(row=2, columnspan=2, sticky='ew')

root.mainloop()
