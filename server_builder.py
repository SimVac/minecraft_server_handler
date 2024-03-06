from server_data import ServerData
import json
import os
import uuid
import requests
import datetime
import shutil

class ServerBuilder:
    def __init__(self):
        self.server_data = ServerData()
        self._servers_path = 'servers'

        if not os.path.exists(self._servers_path):
            os.mkdir(self._servers_path)

    # scarica una versione in un file specifico
    def _download_version(self, version, file_path):
        url_download = self.server_data.get_version_url_download(version)

        data = requests.get(url_download).content

        with open(file_path, 'wb') as f:
            f.write(data)

    # crea le informazioni base in un file json del server
    def _create_server_info(self, file_path, info):
        with open(file_path, 'w') as f:
            json.dump(info, f)

    # crea il server
    def create_server(self, version, server_name, file_name='server.jar'):
        id = str(uuid.uuid4())
        path_to_directory = os.path.join(self._servers_path, id)
        try:
            self.server_data.version_exists(version)
            if not server_name:
                server_name = version

            os.mkdir(path_to_directory)

            path_to_server = os.path.join(path_to_directory, file_name)
            path_to_info = os.path.join(path_to_directory, 'server_info.json')

            server_info = {'version': version,
                           'server_name': server_name,
                           'server_file_name': file_name,
                           'id': id,
                           'date_creation': str(datetime.datetime.now())}

            self._download_version(version, path_to_server)
            self._create_server_info(path_to_info, server_info)
        except Exception:
            shutil.rmtree(path_to_directory)
            print('Errore durante la creazione del server')

