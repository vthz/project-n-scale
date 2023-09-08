import customtkinter
import CommandsFile as CF


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.button4 = None
        self.button3 = None
        self.button2 = None
        self.button1 = None

        self.geometry("720x360")
        self.title("Menu GUI")

        self.command_dd_choices = [i for i in CF.command_profiles]
        self.command_dd = customtkinter.CTkComboBox(self, values=self.command_dd_choices,
                                                    command=self.command_dd_callback, text_color="red")
        self.command_dd.pack(side="left", padx=20, pady=20, anchor="nw")

        self.logs_label = customtkinter.CTkLabel(self, height=50, width=100, text="", corner_radius=10)
        self.logs_label.pack(side="right", padx=20, pady=20, anchor="ne")
        self.required_widgets_list = [self.command_dd, self.logs_label]

    def remove_widgets_on_window(self):
        all_widgets = self.winfo_children()
        for widget in all_widgets:
            if widget not in self.required_widgets_list:
                widget.destroy()

    def update_logs(self, text):
        self.logs_label.configure(text=text)

    def command_dd_callback(self, choice):
        print("DropDown:", choice)
        self.command_dd.configure(text_color="green")
        if choice == "Command List 1":
            self.remove_widgets_on_window()
            self.update_logs("Choose " + choice)
            self.CL1Buttons()
        elif choice == "Command List 2":
            self.remove_widgets_on_window()
            self.update_logs("Choose " + choice)
            self.CL2Buttons()
        elif choice == "Command List 3":
            self.remove_widgets_on_window()
            self.update_logs("Choose " + choice)
            self.CL3Buttons()

    def CL1Buttons(self):
        self.button1 = customtkinter.CTkButton(self, text="Button 1", command=lambda: self.button_callback("F1"),
                                               fg_color="green")
        self.button2 = customtkinter.CTkButton(self, text="Button 2", command=lambda: self.button_callback("F2"),
                                               fg_color="green")
        self.button3 = customtkinter.CTkButton(self, text="Button 3", command=lambda: self.button_callback("F3"),
                                               fg_color="green")
        self.button4 = customtkinter.CTkButton(self, text="Button 4", command=lambda: self.button_callback("F4"),
                                               fg_color="green")

        self.button1.pack(padx=40, pady=5, anchor="nw")
        self.button2.pack(padx=40, pady=5, anchor="nw")
        self.button3.pack(padx=40, pady=5, anchor="nw")
        self.button4.pack(padx=40, pady=5, anchor="nw")

    def CL2Buttons(self):
        self.button1 = customtkinter.CTkButton(self, text="Button 1", command=self.button_callback, fg_color="blue")
        self.button2 = customtkinter.CTkButton(self, text="Button 2", command=self.button_callback, fg_color="blue")
        self.button3 = customtkinter.CTkButton(self, text="Button 3", command=self.button_callback, fg_color="blue")
        self.button4 = customtkinter.CTkButton(self, text="Button 4", command=self.button_callback, fg_color="blue")

        self.button1.pack(padx=40, pady=5, anchor="nw")
        self.button2.pack(padx=40, pady=5, anchor="nw")
        self.button3.pack(padx=40, pady=5, anchor="nw")
        self.button4.pack(padx=40, pady=5, anchor="nw")

    def CL3Buttons(self):
        pass

    def button_callback(self, variable):
        self.update_logs(variable)


app = App()
app.mainloop()
