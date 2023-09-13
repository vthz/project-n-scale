import customtkinter as ct
import os
import json
import SerialCommns as serial_communication


class App(ct.CTk):
    def __init__(self):
        super().__init__()
        self.config_switch = None
        self.config_button = None
        self.choose_json_config = None
        self.json_file_path = None
        self.welcome_label = None
        self.serial_obj = None
        self.geometry("400x420")
        self.window_title = "Python GUI v4"
        self.title(self.window_title)
        self.serial_obj = serial_communication.SerialComm()
        self.open_config_chooser_screen()
        self.required_widgets_list = [self.json_file_path, self.choose_json_config, self.welcome_label]

    def open_config_chooser_screen(self):
        self.welcome_label = ct.CTkLabel(self, text_color="black", text="Welcome!!!")
        self.welcome_label.pack(anchor="center", pady=5)

        #  C:/Users/snaiyer/Documents/GitHub/project-n-scale/Json/command_list_v1.json
        self.json_file_path = ct.CTkEntry(self, placeholder_text="Add JSON config file path!", width=200)
        self.json_file_path.pack(anchor="center", pady=5)

        self.choose_json_config = ct.CTkButton(self, text="Update", fg_color="red",
                                               command=lambda: self.update_with_json_config("OPEN_CONFIG"))
        self.choose_json_config.pack(pady=5, anchor="center")

    def remove_widgets_on_window(self):
        all_widgets = self.winfo_children()
        for widget in all_widgets:
            if widget not in self.required_widgets_list:
                widget.destroy()

    def update_with_json_config(self, variable):
        # file_path = self.json_file_path.get()
        file_path = "C:/Users/snaiyer/Documents/GitHub/project-n-scale/Json/command_list_v1.json"
        self.remove_widgets_on_window()
        if len(file_path) > 0 and os.path.exists(file_path):
            self.welcome_label.configure(text="File Path is valid")
            self.welcome_label.configure(text_color="green")
            with open(file_path, 'r') as file:
                data = json.load(file)
                self.title(self.window_title + " : " + data["title"] + " v" + data["version"])
                self.create_ui_with_config(data)
        else:
            self.welcome_label.configure(text="Invalid File Path")
            self.welcome_label.configure(text_color="red")

    def create_ui_with_config(self, data):
        button_list = data["button_list"]
        for button in button_list:
            button_id = button[1]
            self.config_button = ct.CTkButton(self, text=button[2],
                                              command=lambda id=button_id: self.button_callback(id))
            self.config_button.pack(pady=2, anchor="center")
            self.bind("<" + button[0] + ">", lambda event=None, id=button_id: self.button_callback(id))

        analog_list = data["analog_list"]
        for analog in analog_list:
            label = ct.CTkLabel(self, text=analog[2])
            label.pack(pady=1, anchor="center")

            analog_id = analog[1]
            config_analog = ct.CTkSlider(self, from_=analog[4], to=analog[5], number_of_steps=analog[6], width=200)
            config_analog.set(0)
            config_analog.pack(pady=1, anchor="center")

            def slider_callback(value, analog_id=analog_id):
                value_to_send = f"{analog_id}:{int(value)}"
                self.button_callback(value_to_send)

            config_analog.configure(
                command=lambda value=config_analog, analog_id=analog_id: slider_callback(value, analog_id))

        toggle_list = data["toggle_list"]
        for toggle in toggle_list:
            self.config_switch = ct.CTkSwitch(self, text=toggle[2], onvalue=True, offvalue=False)
            self.config_switch.pack(anchor="center")

    def update_welcome_label(self, updated_value):
        self.welcome_label.configure(text="--=> " + updated_value)

    def button_callback(self, variable):
        self.serial_send_value(variable)
        self.update_welcome_label(updated_value=variable)
        print(variable)

    def serial_send_value(self, value_to_send):
        # pass
        self.serial_obj.write_to_serial(value_to_send)


app = App()
app.mainloop()
