from datetime import datetime
import os
import time

from tkinter import Tk, Label, Button, DISABLED, NORMAL, Frame, Scrollbar, VERTICAL, Canvas

temp = 0
temp_id = ''
worked_time_id = 0
os.environ['TZ'] = 'UTC'
time.tzset()
some_data = [
    'first time', 'second time',
    'second time', 'second time',
    'second time', 'second time', 'second time', 'second time' ,'second time', 'second time',
'second time', 'second time', 'second time' ,'second time' ,'second time' ,'second time'
]


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
    global temp, worked_time_id
    root.after_cancel(temp_id)
    worked_time = datetime.fromtimestamp(temp).strftime('%H:%M:%S')
    pause_timer_button.grid_forget()
    continue_timer_button.grid_forget()
    worked_time_record = Label(current_day_data_frame, width=10, text=f'{worked_time}', font=('Mac', 10))
    worked_time_record.grid(row=worked_time_id, columnspan=2, sticky='ew')
    start_timer_button.grid(row=1, columnspan=2, sticky='ew')
    print(f'Worked time {worked_time}')
    temp = 0
    worked_time_id += 1
    start_timer_time.configure(text='00:00:00')
    stop_timer_button['state'] = DISABLED


root = Tk()
root.title('Timer')
root.geometry('500x500')
start_timer_time = Label(root, width=10, font=('Mac', 50), text='00:00:00')
start_timer_time.grid(row=0, columnspan=2)

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
current_day_data_frame = Frame(root)
current_day_data_frame.grid(row=3, columnspan=2, sticky='ew')
history_data_frame = Frame(root)
history_data_frame.grid(row=4, columnspan=2, sticky='ew')
# history_data_frame_canvas = Canvas(history_data_frame)
# history_data_frame_canvas.grid(row=0, sticky="news")
# history_data_frame_scrollbar = Scrollbar(history_data_frame_canvas, orient=VERTICAL, command=history_data_frame_canvas.yview)
# history_data_frame_scrollbar.pack(side='right', fill='y')

for index, data in enumerate(some_data):
    history_row = Label(history_data_frame, width=10, text=f'{data}', font=('Mac', 10))
    history_row.grid(row=index, columnspan=2, sticky='ew')
# history_text_area = Text(history_data_frame)
# history_text_area.grid(row=0, columnspan=2, sticky='ew')
# history_data_scroll = Scrollbar(history_data_frame, orient=VERTICAL)
# history_data_frame.config(yscrollcommand=history_data_scroll.set)

root.mainloop()
