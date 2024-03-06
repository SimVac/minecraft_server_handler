import customtkinter

from server_list import ServerList
from sidebar import Sidebar

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("Minecraft Server Manager")
        self.geometry(f"{1100}x{580}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create sidebar
        self.sidebar = Sidebar(self)
        self.sidebar.grid(row=0, column=0, rowspan=4, sticky="nsew")

        # server list
        self.server_list = ServerList(self)
        self.server_list.grid(row=0, column=1, rowspan=4, sticky="nsew")