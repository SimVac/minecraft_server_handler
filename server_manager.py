import os
import json

class ServerManager:
    def __init__(self):
        self._servers_path = 'servers/'
        self._server_info_name_file = 'server_info.json'

    def get_servers_data(self):
        servers_info = []
        for subdir, dirs, files in os.walk(self._servers_path):
            for file in files:
                if file == self._server_info_name_file:
                    with open(os.path.join(subdir, file), 'r') as f:
                        servers_info.append(json.load(f))
        return servers_info

    def get_servers_name(self):
        servers_data = self.get_servers_data()
        return list(map(lambda server: server['server_name'], servers_data))
