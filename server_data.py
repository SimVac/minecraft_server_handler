import requests

class ServerData:
    def __init__(self, url="https://launchermeta.mojang.com/mc/game/version_manifest.json"):
        self._data = requests.get(url).json()

    #ritorna i dati di tutte le versioni
    def get_versions_data(self):
        return self._data['versions']

    #ritorna una lista con i nomi di tutte le versioni
    def get_versions_name(self):
        return list(map(lambda x: x['id'], self._data['versions']))

    #controlla se una versione esiste, se non esiste lancia un'eccezione
    def version_exists(self, version):
        self.get_version_data(version)

    #ritorna i dati di una versione, se non esiste lancia un'eccezione
    def get_version_data(self, name):
        version = list(filter(lambda version: version['id'] == name, self._data['versions']))
        if len(version) > 0: return version[0]
        raise Exception('Version not found')

    #ritorna l'url con i dati specifici di una versione
    def get_version_url_info(self, name):
        version_data = self.get_version_data(name)
        return version_data['url']

    #ritorna l'url da cui fare il download di un server
    def get_version_url_download(self, name):
        url = self.get_version_url_info(name)
        version_info = requests.get(url).json()
        return version_info['downloads']['server']['url']
