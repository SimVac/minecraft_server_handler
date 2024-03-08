import customtkinter
from PIL import Image


class ServerListRow(customtkinter.CTkFrame):
    def __init__(self, master, /, name, version):
        super().__init__(master, fg_color="transparent")
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # images load
        self.green_circle_image = customtkinter.CTkImage(light_image=Image.open("./assets/green_circle.png"),
                                                   dark_image=Image.open("./assets/green_circle.png"),
                                                   size=(25, 25))
        self.red_circle_image = customtkinter.CTkImage(light_image=Image.open("./assets/red_circle.png"),
                                                 dark_image=Image.open("./assets/red_circle.png"),
                                                 size=(25, 25))
        self.play_image = customtkinter.CTkImage(light_image=Image.open("./assets/play.png"),
                                                 dark_image=Image.open("./assets/play.png"),
                                                 size=(25, 25))
        self.menu_icon_image = customtkinter.CTkImage(light_image=Image.open("./assets/menu.png"),
                                                      dark_image=Image.open("./assets/menu.png"),
                                                      size=(25, 25))

        self.temp = customtkinter.CTkFrame(self, fg_color="transparent")
        self.temp.grid_columnconfigure((0, 1, 2), weight=1, uniform="fred")
        self.temp.grid(row=0, column=0, sticky="w")
        # server status icon
        # TODO cambiare icona dello status del server
        self.server_status = customtkinter.CTkLabel(self.temp, image=self.red_circle_image, text="")
        self.server_status.grid(row=0, column=0)

        # server name
        self.server_name = customtkinter.CTkLabel(self.temp, text=name,
                                                  font=customtkinter.CTkFont(size=25, weight="bold"))
        self.server_name.grid(row=0, column=1)

        # server version
        self.server_name = customtkinter.CTkLabel(self.temp, text=version,
                                                  font=customtkinter.CTkFont(size=25, weight="bold"))
        self.server_name.grid(row=0, column=2)

        #last buttons frame
        self.last_buttons_frame = customtkinter.CTkFrame(self, fg_color="transparent")
        self.last_buttons_frame.grid(row=0, column=1, sticky="e", padx=(0, 10))

        # server play button
        self.play_button = customtkinter.CTkButton(self.last_buttons_frame, image=self.play_image, fg_color="transparent", text="", width=25, height=25, hover_color="#404040")
        self.play_button.grid(row=0, column=0)

        # server menu button
        self.server_button_edit = customtkinter.CTkButton(self.last_buttons_frame, text="", width=25, height=25, image=self.menu_icon_image, fg_color="transparent", hover_color="#404040")
        self.server_button_edit.grid(row=0, column=1)


class ServerList(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color="transparent")
        self.grid_columnconfigure(0, weight=1)

        self.server_list = map(lambda server: ServerListRow(self, name=server['name'], version=server['version']), self.get_server_list())
        for row, server_list_row in enumerate(self.server_list, 1):
            server_list_row.grid(row=row, column=0, sticky="ew", pady=20)
    def get_server_list(self):
        #TODO ottenere i dati dai nomi dei server
        return [
            {"name": "Server Prova 1", "version": "1.20"},
            {"name": "Server Prova 1", "version": "1.7.4"},
            {"name": "Server Prova 1", "version": "1.12.1"}
        ]