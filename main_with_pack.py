from datetime import datetime
import os
import time

from tkinter import Tk, Label, Button, DISABLED, NORMAL, Frame, Scrollbar, VERTICAL, Canvas, BOTH, LEFT, Entry

temp = 0
temp_id = ''
worked_time_id = 0
os.environ['TZ'] = 'UTC'
time.tzset()
some_data = [
    'first time\n\n\n\n\nfd', 'second time',
    'second time', 'second time',
    'second time', 'second time', 'second time', 'second time' ,'second time', 'second time',
'second time', 'second time', 'second time' ,'second time' ,'second time' ,'second time', 'second time',
    'second time', 'second time', 'second time', 'second time', 'second time', 'second time', 'second time', 'TEST'
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
    stop_timer_button.config(state=NORMAL)
    timer_label.config(state=DISABLED)
    root.focus_set()


def pause_timer_command():
    root.after_cancel(temp_id)
    pause_timer_button.grid_forget()
    continue_timer_button.grid(row=1, columnspan=2, sticky='ew')
    timer_label.config(state=NORMAL)


def continue_timer_command():
    timer()
    continue_timer_button.grid_forget()
    pause_timer_button.grid(row=1, columnspan=2, sticky='ew')
    timer_label.config(state=DISABLED)


def stop_timer_command():
    global temp, worked_time_id
    root.after_cancel(temp_id)
    worked_time = datetime.fromtimestamp(temp).strftime('%H:%M:%S')
    pause_timer_button.grid_forget()
    continue_timer_button.grid_forget()
    worked_time_record_label = Label(current_day_data_frame, width=10, text=f'{timer_label.get()}', font=('Mac', 10))
    worked_time_record_time = Label(current_day_data_frame, width=10, text=f'{worked_time}', font=('Mac', 10))
    worked_time_record_label.grid(row=worked_time_id + 1, column=0)
    worked_time_record_time.grid(row=worked_time_id + 1, column=1)
    start_timer_button.grid(row=1, columnspan=2, sticky='ew')
    print(f'Worked time {worked_time}')
    temp = 0
    worked_time_id += 1
    start_timer_time.configure(text='00:00:00')
    stop_timer_button.config(state=DISABLED)
    timer_label.config(state=NORMAL)


root = Tk()
root.title('Timer')
root.geometry('500x500')

main_frame = Frame(root, bg='gray')
main_frame.pack(fill=BOTH, expand=1)

canvas = Canvas(main_frame, bd=0, highlightthickness=0, relief='ridge')
canvas.pack(fill=BOTH, expand=1, side=LEFT)

scrollbar = Scrollbar(main_frame, orient=VERTICAL, command=canvas.yview)
scrollbar.pack(side='right', fill='y')
canvas.configure(yscrollcommand=scrollbar.set)
canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox('all')))

canvas_frame = Frame(canvas)
canvas.create_window((0, 0), window=canvas_frame, anchor='nw')

start_timer_time = Label(canvas_frame, width=10, font=('Mac', 50), text='00:00:00')
start_timer_time.grid(columnspan=2, row=0)

start_timer_button = Button(canvas_frame, text='Start', font=('Mac', 15), command=start_timer_command)
pause_timer_button = Button(canvas_frame, text='Pause', font=('Mac', 15), command=pause_timer_command)
continue_timer_button = Button(
    canvas_frame,
    text='Continue',
    font=('Mac', 15),
    command=continue_timer_command
)
stop_timer_button = Button(
    canvas_frame, text='Stop', font=('Mac', 15), command=stop_timer_command, state=DISABLED
)
start_timer_button.grid(row=1, columnspan=2, sticky='ew')
stop_timer_button.grid(row=2, columnspan=2, sticky='ew')

timer_label = Entry(canvas_frame)
timer_label.grid(row=3, columnspan=2, sticky='ew')

current_day_data_frame = Frame(canvas_frame)
current_day_data_header = Label(current_day_data_frame, text='Today')
current_day_data_header.grid(row=0, columnspan=2, sticky='ew')
current_day_data_frame.grid(row=5, columnspan=2, sticky='ew')

history_data_frame = Frame(canvas_frame)
history_data_frame.grid(row=6, columnspan=2, sticky='ew')

for index, data in enumerate(some_data):
    history_row = Label(history_data_frame, width=10, text=f'{data}', font=('Mac', 10))
    history_row.grid(row=index, columnspan=2, sticky='ew')

root.mainloop()
