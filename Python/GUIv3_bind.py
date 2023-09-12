import customtkinter as ct


class App(ct.CTk):
    def __init__(self):
        super().__init__()
        self.switch1_flag = False
        self.switch2_flag = False
        self.switch3_flag = False

        self.geometry("220x360")
        self.counter_var = 0
        self.title("Python - Arduino GUI with Key Binding v3")
        self.bind("<w>", lambda event=None: self.button_callback("Pressed_W"))
        self.bind("<a>", lambda event=None: self.button_callback("Pressed_A"))
        self.bind("<s>", lambda event=None: self.button_callback("Pressed_S"))
        self.bind("<d>", lambda event=None: self.button_callback("Pressed_D"))
        self.bind("<m>", lambda event=None: self.button_callback("Pressed_M"))

        self.bind("1", lambda event=None: self.button_callback("Pressed_1"))
        self.bind("2", lambda event=None: self.button_callback("Pressed_2"))
        self.bind("3", lambda event=None: self.button_callback("Pressed_3"))

        self.logs_label = ct.CTkLabel(self, text_color="black", text="Welcome!!!")
        self.logs_label.pack(anchor="center")

        self.switch_1 = ct.CTkSwitch(self, text="LED 1", onvalue=True, offvalue=False)
        self.switch_1.pack(anchor="center")
        self.switch_2 = ct.CTkSwitch(self, text="LED 2", onvalue=True, offvalue=False)
        self.switch_2.pack(anchor="center")
        self.switch_3 = ct.CTkSwitch(self, text="LED 3", onvalue=True, offvalue=False)
        self.switch_3.pack(anchor="center")

        self.speed_slider = ct.CTkSlider(self, from_=0, to=100, number_of_steps=100, width=200)
        self.speed_slider.set(0)
        self.speed_slider.pack(padx=10, pady=10, anchor="center")

    def button_callback(self, variable):
        self.counter_var += 1
        final_var_to_serial = None
        if variable == "Pressed_W":
            final_var_to_serial = "W"
        elif variable == "Pressed_A":
            final_var_to_serial = "A"
        elif variable == "Pressed_S":
            final_var_to_serial = "S"
        elif variable == "Pressed_D":
            final_var_to_serial = "D"
        elif variable == "Pressed_M":
            final_var_to_serial = "M" + ":" + str("{:.2f}".format(self.speed_slider.get()))
        elif variable == "Pressed_1":
            self.switch1_flag = not self.switch1_flag
            if self.switch1_flag:
                self.switch_1.select()
            else:
                self.switch_1.deselect()
            final_var_to_serial = "LED:1"
        elif variable == "Pressed_2":
            self.switch2_flag = not self.switch2_flag
            if self.switch2_flag:
                self.switch_2.select()
            else:
                self.switch_2.deselect()
            final_var_to_serial = "LED:2"
        elif variable == "Pressed_3":
            self.switch3_flag = not self.switch3_flag
            if self.switch3_flag:
                self.switch_3.select()
            else:
                self.switch_3.deselect()
            final_var_to_serial = "LED:3"
        self.logs_label.configure(text="-=> " + final_var_to_serial)
        print(final_var_to_serial)


app = App()
app.mainloop()
