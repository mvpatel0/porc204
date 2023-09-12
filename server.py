import socket
from threading import Thread

IP_ADDRESS = '127.0.0.0'
SERVER = None
PORT = 6000

CLIENTS={}


    
def acceptConnections():
    global CLIENTS
    global SERVER

    while True:
        player_socket,addr=SERVER.accept()
        player_name=player_socket.recv(1024).decode().strip()
        print(player_name)
        if(len(CLIENTS.key())==0):
            CLIENTS[player_name]={'player_type':'player1'}
        else:
            CLIENTS[player_name]={'player_type':'player2'}

        CLIENTS[player_name]['player_socket']=player_socket
        CLIENTS[player_name]['address']=addr
        CLIENTS[player_name]['player_name']=player_name
        CLIENTS[player_name]['turn']=False

        print(f'Connection is established with {player_name}:{addr}')




def setup():
    print('\n\t\t\t\t\t***Welcome To Thamblao Game!***\n')

    global SERVER
    global PORT
    global IP_ADDRESS

    SERVER=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    SERVER.bind((IP_ADDRESS, PORT))
    SERVER.listen(10)

    print('\n\t\t\t\t***SERVER IS WAITING FOR INCOMING CONNECTION...\n')
    acceptConnections()

thread=Thread(target=setup)
thread.start()