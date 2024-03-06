import customtkinter


class ServerListRow(customtkinter.CTkFrame):
    def __init__(self, master, /, name):
        super().__init__(master, fg_color="transparent")

        self.server_name = customtkinter.CTkLabel(self, text=name,
                                                  font=customtkinter.CTkFont(size=20, weight="bold"))
        self.server_name.grid(row=0, column=0, pady=20)

        self.server_button_edit = customtkinter.CTkButton(self, text="Edit", width=50, height=10, font=customtkinter.CTkFont(size=15))
        self.server_button_edit.grid(row=0, column=1, padx=10)


class ServerList(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color="transparent")

        self.title_label = customtkinter.CTkLabel(self, text="Server List", font=customtkinter.CTkFont(size=30, weight="bold"))
        self.title_label.grid(row=0, column=0, padx=20, pady=(10, 20), sticky="nw")

        self.server_list = self.get_server_list()
        for row, server_list_row in enumerate(self.server_list, 1):
            server_list_row.grid(row=row, column=0, padx=(70, 0))

    def get_server_list(self):
        #TODO ottenere i dati dai nomi dei server
        return [
            ServerListRow(self, "Server Prova 1"),
            ServerListRow(self, "Server Prova 2"),
            ServerListRow(self, "Server Prova 3")
        ]