import customtkinter

class Sidebar(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.grid_rowconfigure(4, weight=1)
        self.title_label = customtkinter.CTkLabel(self, text="Minecraft Server\nManager",
                                                  font=customtkinter.CTkFont(size=20, weight="bold"))
        self.title_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.sidebar_server_button = customtkinter.CTkButton(self,
                                                             command=self.sidebar_server_button_event,
                                                             text="Server List")
        self.sidebar_server_button.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_console_button = customtkinter.CTkButton(self,
                                                              command=self.sidebar_console_button_event, text="Console",
                                                              state="disabled")
        self.sidebar_console_button.grid(row=2, column=0, padx=20, pady=10)

    def sidebar_server_button_event(self):
        pass

    def sidebar_console_button_event(self):
        pass