import customtkinter as ct
import os
import json
import SerialCommns as serialCommunication


class App(ct.CTk):
    def __init__(self):
        super().__init__()
        self.frame0 = None
        self.frame4 = None
        self.frame3 = None
        self.frame2 = None
        self.frame1 = None
        self.config_switch = None
        self.config_button = None
        self.choose_json_config = None
        self.json_file_path = None
        self.welcome_label = None
        self.serial_obj = None
        self.geometry("800x200")
        self.resizable(width=False, height=True)
        self.window_title = "Python GUI v4"
        self.title(self.window_title)
        self.serial_obj = serialCommunication.SerialComm()
        self.create_layout_frames()
        self.open_config_chooser_screen()
        self.required_widgets_list = [self.json_file_path, self.choose_json_config, self.welcome_label, self.frame0,
                                      self.frame1, self.frame2, self.frame3, self.frame4]

    def create_layout_frames(self):
        self.frame0 = ct.CTkFrame(self, fg_color="grey")
        self.frame1 = ct.CTkFrame(self.frame0, width=200, corner_radius=0, border_color="red")
        self.frame2 = ct.CTkFrame(self.frame0, width=200, corner_radius=0)
        self.frame3 = ct.CTkFrame(self.frame0, width=200, corner_radius=0)
        self.frame4 = ct.CTkFrame(self.frame0, width=200, corner_radius=0)

        self.frame0.pack(side="top", fill="both", expand="true", padx=5, pady=5)
        self.frame1.pack(side="left", fill="both", expand="true", padx=2, pady=2)
        self.frame2.pack(side="left", fill="both", expand="true")
        self.frame3.pack(side="left", fill="both", expand="true")
        self.frame4.pack(side="left", fill="both", expand="true")

    def open_config_chooser_screen(self):
        self.welcome_label = ct.CTkLabel(self.frame1, text_color="black", text="Welcome!!!", width=180)
        self.welcome_label.pack(anchor="center", pady=2, padx=2)

        #  C:/Users/snaiyer/Documents/GitHub/project-n-scale/Json/command_list_v1.json
        self.json_file_path = ct.CTkEntry(self.frame1, placeholder_text="Add JSON config file path!", width=200)
        self.json_file_path.pack(anchor="center", pady=2, padx=2)

        self.choose_json_config = ct.CTkButton(self.frame1, text="Update", fg_color="red",
                                               command=lambda: self.update_with_json_config("OPEN_CONFIG"))
        self.choose_json_config.pack(anchor="center", pady=2, padx=2)

    def remove_widgets_on_window(self):
        widgets_to_destroy = self.frame2.winfo_children()
        for widget in widgets_to_destroy:
            widget.destroy()
        widgets_to_destroy = self.frame3.winfo_children()
        for widget in widgets_to_destroy:
            widget.destroy()
        widgets_to_destroy = self.frame4.winfo_children()
        for widget in widgets_to_destroy:
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
            self.config_button = ct.CTkButton(self.frame2, text=button[2],
                                              command=lambda id=button_id: self.button_callback(id))
            self.config_button.pack(pady=2, anchor="center")
            self.bind("<" + button[0] + ">", lambda event=None, id=button_id: self.button_callback(id))

        analog_list = data["analog_list"]
        for analog in analog_list:
            label = ct.CTkLabel(self.frame3, text=analog[2])
            label.pack(pady=1, anchor="center")

            analog_id = analog[1]
            config_analog = ct.CTkSlider(self.frame3, from_=analog[4], to=analog[5], number_of_steps=analog[6],
                                         width=200)
            config_analog.set(0)
            config_analog.pack(pady=1, anchor="center")

            def slider_callback(value, analog_id=analog_id):
                value_to_send = f"{analog_id}:{int(value)}"
                self.button_callback(value_to_send)

            config_analog.configure(
                command=lambda value=config_analog, analog_id=analog_id: slider_callback(value, analog_id))

        toggle_list = data["toggle_list"]
        for toggle in toggle_list:
            switch = ct.CTkSwitch(self.frame4, text=toggle[2], onvalue=True, offvalue=False)
            switch.pack(anchor="center")
            callback = lambda switch=switch, toggle=toggle: self.switch_callback(switch, toggle)
            switch.configure(command=callback)

    def switch_callback(self, switch, toggle):
        # print(f"Switch '{toggle[2]}' toggled. Current state: {switch.get()}")
        value_to_send = f"{toggle[2]}:{int(switch.get())}"
        self.button_callback(value_to_send)

    def update_welcome_label(self, updated_value):
        self.welcome_label.configure(text="--=> " + updated_value)

    def button_callback(self, variable):
        self.serial_send_value(variable)
        self.update_welcome_label(updated_value=variable)

    def serial_send_value(self, value_to_send):
        if self.serial_obj.write_to_serial(value_to_send):
            self.welcome_label.configure(text_color="green")
        else:
            self.welcome_label.configure(text_color="red")

        print(value_to_send)


app = App()
app.mainloop()
