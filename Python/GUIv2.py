import customtkinter as ct


class App(ct.CTk):
    def __init__(self):
        super().__init__()
        self.create_config_label = None
        self.create_config_button = None
        self.open_config_button = None
        self.welcome_label = None
        self.geometry("720x360")
        self.title("Python-A GUI v2")
        self.open_welcome_screen()

        self.main_menu_button = ct.CTkButton(self, text="Main Menu", command=lambda: self.button_callback("MAIN_MENU"))
        self.main_menu_button.pack(side="left", padx=10, pady=10)
        self.required_widgets_list = [self.main_menu_button]

    def open_welcome_screen(self):
        self.remove_widgets_on_window()
        self.welcome_label = ct.CTkLabel(self, text="Welcome!")
        self.open_config_button = ct.CTkButton(self, text="Open Config File",
                                               command=lambda: self.button_callback("OPEN_CONFIG"))
        self.create_config_button = ct.CTkButton(self, text="Create Config File",
                                                 command=lambda: self.button_callback("CREATE_CONFIG"))

        self.welcome_label.pack(anchor="center", pady=50)
        self.open_config_button.pack(anchor="center", pady=10)
        self.create_config_button.pack(anchor="center", pady=10)

    def button_callback(self, variable):
        if variable == "CREATE_CONFIG":
            self.open_create_config_screen()
        elif variable == "OPEN_CONFIG":
            pass
        elif variable == "MAIN_MENU":
            self.open_welcome_screen()
        print(variable)

    def remove_widgets_on_window(self):
        all_widgets = self.winfo_children()
        for widget in all_widgets:
            if widget not in self.required_widgets_list:
                widget.destroy()

    def open_create_config_screen(self):
        self.remove_widgets_on_window()
        self.create_config_label = ct.CTkLabel(self, text="Create Config")
        self.create_config_label.pack(anchor="center")


app = App()
app.mainloop()
