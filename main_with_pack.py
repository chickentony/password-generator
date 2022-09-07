from datetime import datetime
import os
import time

from tkinter import Tk, Label, Button, DISABLED, NORMAL, Frame, Scrollbar, VERTICAL, Canvas, BOTH, LEFT

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
    pause_timer_button.pack_forget()
    continue_timer_button.pack_forget()
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

main_frame = Frame(root, bg='gray')
main_frame.pack(fill=BOTH, expand=1)

canvas = Canvas(main_frame)
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

current_day_data_frame = Frame(canvas_frame)
current_day_data_frame.grid(row=3, columnspan=2, sticky='ew')
# frame_canvas = Frame(main_frame)
# frame_canvas.grid(row=2, column=0, pady=(5, 0), sticky='nw')
# frame_canvas.grid_rowconfigure(0, weight=1)
# frame_canvas.grid_columnconfigure(0, weight=1)
# frame_canvas.grid_propagate(False)
# canvas = Canvas(frame_canvas, bg="yellow")
# canvas.grid(row=0, column=0, sticky="news")
#

# scrollbar.grid(row=0, column=1, sticky='ns')

#
# history_data_frame = Frame(canvas)
# canvas.create_window((0, 0), anchor='nw', window=history_data_frame)
# start_timer_time.pack()
# button_frame = Frame(root)
# button_frame.pack()
#
# continue_timer_button = Button(
#     button_frame,
#     text='Continue',
#     font=('Mac', 15),
#     command=continue_timer_command
# )
# stop_timer_button = Button(
#     button_frame, text='Stop', font=('Mac', 15), command=stop_timer_command, state=DISABLED
# )
#
# start_timer_button.pack()
# stop_timer_button.pack()
# # start_timer_button.grid(row=1, columnspan=2, sticky='ew')
# # stop_timer_button.grid(row=2, columnspan=2, sticky='ew')
# current_day_data_frame = Frame(root)
# current_day_data_frame.pack()
# # current_day_data_frame.grid(row=3, columnspan=2, sticky='ew')
# history_data_frame = Frame(root)
# # history_data_frame.grid(row=4, columnspan=2, sticky='ew')
# history_data_frame.pack()
# history_data_frame_canvas = Canvas(history_data_frame)
# history_data_frame_canvas.grid(row=0, column=0, sticky="news")
# history_data_frame_scrollbar = Scrollbar(history_data_frame_canvas, orient=VERTICAL, command=history_data_frame_canvas.yview)
# history_data_frame_scrollbar.grid(row=0, column=1, sticky='ns')
# history_data_frame_canvas.configure(yscrollcommand=history_data_frame_scrollbar.set)
#
for index, data in enumerate(some_data):
    history_row = Label(canvas_frame, width=10, text=f'{data}', font=('Mac', 10))
    history_row.grid(row=index + 4, column=0, sticky='ew')

root.mainloop()
