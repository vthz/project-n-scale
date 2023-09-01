import customtkinter
import CommandsFile as CF


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("720x360")
        self.title("Menu GUI")
        self.command_dd_choices = [i for i in CF.command_profiles]

        self.command_dd = customtkinter.CTkComboBox(self, values=self.command_dd_choices,
                                                    command=self.command_dd_callback, text_color="red")

        self.button = customtkinter.CTkButton(self, text="my button", command=self.button_callback)

        self.command_dd.pack(side="left", padx=20, pady=20, anchor="nw")
        self.button.pack(padx=40, pady=40, anchor="nw")
        self.required_widgets_list = [self.command_dd]

    @staticmethod
    def button_callback():
        print("button clicked")

    def remove_widgets_on_window(self):
        all_widgets = self.winfo_children()
        # print(all_widgets)
        for widget in all_widgets:
            if widget not in self.required_widgets_list:
                widget.destroy()

    def command_dd_callback(self, choice):
        print("DropDown:", choice)
        self.command_dd.configure(text_color="green")
        if choice == "Command List 1":
            self.remove_widgets_on_window()
            self.label1 = customtkinter.CTkLabel(self, text="Feature 1")
            self.label1.pack(padx=50, pady=50, anchor="nw")
        elif choice == "Command List 2":
            self.remove_widgets_on_window()
            self.label2 = customtkinter.CTkLabel(self, text="Feature 2")
            self.label2.pack(padx=50, pady=50, anchor="nw")


app = App()
app.mainloop()
