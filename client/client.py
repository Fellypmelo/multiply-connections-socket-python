# -*- coding: utf-8 -*-
#!/usr/bin/env python3

import threading
import socket

PORT = 5500
HOST = socket.gethostbyname(socket.gethostname())
CONNECT_SERVER = (HOST,PORT)
MAX_B = 2048
FORMAT = 'utf-8'
MSG_OFF = '!disc'

def Main():
    #criando socket do client
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    #tentado conectar ao servidor
    try:
        client.connect(CONNECT_SERVER)
        print("Conectado...")
    except:
        return print("\nNão foi possivel conectar ao servidor :'(\n")
    
    print("Digite o seu username")
    username = input("User-> ")
    print(f"[Conectado] --> {username}")

    thread1 = threading.Thread(target=receiveMsg,args=[client])
    thread2 = threading.Thread(target=sendMsg,args=(client,username))

    thread1.start()
    thread2.start()

def receiveMsg(client):
    
    while True:
        try:
            msg = client.recv(MAX_B).decode(FORMAT)
            print(msg+'\n=>')
        except:
            client.close()
            break
def sendMsg(client,username):
    sendmenssagem = True
    while sendmenssagem:
        try:
            msg = input('\n=>')
            client.send(f'<{username}> :: {msg}'.encode(FORMAT))
        except:
            return
        #caso o usuario queria se disconectar é so digitar '!disc'
        if msg == MSG_OFF:
            print("\nDeseja sair ?\n")
            msg = str(input('[Y \ N]: '))
            if msg == 'y':
                
                print("Disconectado...")
                print(f"Até a proxima, {username}\n") 
                client.close()
                break
            elif msg == 'n':
                    print("...")

if __name__=='__main__':

    print("Tentando conectar...")
    Main()
    
