from server_builder import ServerBuilder

server_builder = ServerBuilder()

version = input('Inserisci la versione: ')
server_name = input('Inserisci il nome del server: ')

server_builder.create_server(version, server_name)