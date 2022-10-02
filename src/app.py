from tkinter import Tk, Frame, Button, Label


class App(Tk):
    def __init__(self):
        super().__init__()
        self.title('Password generator')
        self.geometry('700x200')
        self.create_widgets()

    def create_widgets(self):
        password_generate = PasswordGenerateWidget(self)
        password_generate.grid(column=0, row=0)


class PasswordGenerateWidget(Frame):
    def __init__(self, container):
        super().__init__(container)
        self.create_widgets()
        self.widgets = self.winfo_children()
        self.container = container
        # print(container)

    def create_widgets(self):
        password_label = Label(
            self,
            text="Password",
            borderwidth=2,
            relief="groove",
            height=2,
            width=40
        )
        password_label.grid(column=0, row=0)
        generate_button = Button(self, text="Generate password", command=self.generate_button_command)
        generate_button.grid(column=1, row=0)
        copy_button = Button(self, text="Copy password", command=self.copy_password_button_command)
        copy_button.grid(column=2, row=0)

        for widget in self.winfo_children():
            widget.grid(padx=0, pady=5)

    def generate_button_command(self):
        self.widgets[0].config(text="New password")

    def copy_password_button_command(self):
        password = self.widgets[0]["text"]
        self.clipboard_append(password)
