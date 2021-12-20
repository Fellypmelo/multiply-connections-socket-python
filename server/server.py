# -*- coding: utf-8 -*-
#!/usr/bin/env python3

import threading
import socket

PORT = 5500
HOST = socket.gethostbyname(socket.gethostname())
SERVER = (HOST,PORT)
MAX_B = 2048

#criando lista para clientes
clients = []

def startServer():
    #criando socket
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    #tentando iniciar o servidor
    try:
        print("Conectando ao servidor")
        server.bind(SERVER)
        print("Aguardando clientes...")
        server.listen()
    except:
        print("Não foi possivel conectar o servidor!!!")


    while True:
        client, ender = server.accept()
        #adicionando clientes na lista
        clients.append(client)

        threadView = threading.Thread(target=view_Server,args=(client,ender))
        thread = threading.Thread(target=msgtratamento,args=[client])
        
        threadView.start()
        thread.start()
    
def view_Server(client,ender):
    try:
        print(f"[CONEXÕES ATIVAS] --> [{threading.activeCount()-1}]")
        print(f"[NOVA CONEXÃO]--> ENDEREÇO:[{ender}]")
    except:
        return print("Nenhuma conexão ativa.")
    return client

def msgtratamento(client):
    #tratando o dados do recebidos
    while True:
        try:
            msg = client.recv(MAX_B)
            broadcast(msg,client)
        except:
            deleteClient(client)
            break

def broadcast(msg,client):
    for clientIndex in clients:
        if clientIndex != client:
            try:
                clientIndex.send(msg)
            except:
                deleteClient(clientIndex)

def deleteClient(client):
    #removendo client do lista
    clients.remove(client)

if __name__ == '__main__':
    print("SERVER RODANDO...")
    startServer()
