import threading
import socket
import os
from docx import Document

def print_colorful_text(text):
    print(f"\033[31m{text}\033[0m")

def print_colorful_text_green(text):
    print(f"\033[32m{text}\033[0m")

print_colorful_text("""
 ██▀███  ▓█████ ▓█████▄      ██████  ██▓ ██▓    ▓█████  ███▄    █  ▄████▄  ▓█████  ██▀███    ██████ 
▓██ ▒ ██▒▓█   ▀ ▒██▀ ██▌   ▒██    ▒ ▓██▒▓██▒    ▓█   ▀  ██ ▀█   █ ▒██▀ ▀█  ▓█   ▀ ▓██ ▒ ██▒▒██    ▒ 
▓██ ░▄█ ▒▒███   ░██   █▌   ░ ▓██▄   ▒██▒▒██░    ▒███   ▓██  ▀█ ██▒▒▓█    ▄ ▒███   ▓██ ░▄█ ▒░ ▓██▄   
▒██▀▀█▄  ▒▓█  ▄ ░▓█▄   ▌     ▒   ██▒░██░▒██░    ▒▓█  ▄ ▓██▒  ▐▌██▒▒▓▓▄ ▄██▒▒▓█  ▄ ▒██▀▀█▄    ▒   ██▒
░██▓ ▒██▒░▒████▒░▒████▓    ▒██████▒▒░██░░██████▒░▒████▒▒██░   ▓██░▒ ▓███▀ ░░▒████▒░██▓ ▒██▒▒██████▒▒
░ ▒▓ ░▒▓░░░ ▒░ ░ ▒▒▓  ▒    ▒ ▒▓▒ ▒ ░░▓  ░ ▒░▓  ░░░ ▒░ ░░ ▒░   ▒ ▒ ░ ░▒ ▒  ░░░ ▒░ ░░ ▒▓ ░▒▓░▒ ▒▓▒ ▒ ░
  ░▒ ░ ▒░ ░ ░  ░ ░ ▒  ▒    ░ ░▒  ░ ░ ▒ ░░ ░ ▒  ░ ░ ░  ░░ ░░   ░ ▒░  ░  ▒    ░ ░  ░  ░▒ ░ ▒░░ ░▒  ░ ░
  ░░   ░    ░    ░ ░  ░    ░  ░  ░   ▒ ░  ░ ░      ░      ░   ░ ░ ░           ░     ░░   ░ ░  ░  ░  
   ░        ░  ░   ░             ░   ░      ░  ░   ░  ░         ░ ░ ░         ░  ░   ░           ░  
                 ░                                                ░                                 
""")
print("loading...")


##################
#### TeamChat ####
##################

host = '127.0.0.1'
port = 1337

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()
clients = []
nicknames = []


def broadcast(message):
    for client in clients:
        client.send(message)

def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast(f'{nickname} left the chat.'.encode('ascii'))
            nicknames.remove(nickname)
            break
        
        
def receive():
    print_colorful_text("""

╔╦╗┌─┐┌─┐┌┬┐  ╔═╗┬ ┬┌─┐┌┬┐
 ║ ├┤ ├─┤│││  ║  ├─┤├─┤ │ 
 ╩ └─┘┴ ┴┴ ┴  ╚═╝┴ ┴┴ ┴ ┴ 
                          
                          
""")
    while True:
        client, address = server.accept()
        
        client.send('NICK'.encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clients.append(client)
    
        broadcast(f"{nickname} joined the chat.".encode('ascii'))
        client.send(" Connected to the server.".encode('ascii'))   

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()
        
        
#############################
#### Rules of Engagement ####
#############################

def ROE():
    print_colorful_text("""
╦═╗╦ ╦╦  ╔═╗╔═╗  ╔═╗╔═╗  ╔═╗╔╗╔╔═╗╔═╗╔═╗╔═╗╔╦╗╔═╗╔╗╔╔╦╗
╠╦╝║ ║║  ║╣ ╚═╗  ║ ║╠╣   ║╣ ║║║║ ╦╠═╣║ ╦║╣ ║║║║╣ ║║║ ║ 
╩╚═╚═╝╩═╝╚═╝╚═╝  ╚═╝╚    ╚═╝╝╚╝╚═╝╩ ╩╚═╝╚═╝╩ ╩╚═╝╝╚╝ ╩ 
                                                                                                              
""")
    doc = Document('./ROE.docx')
    full_text = []
    for para in doc.paragraphs:
        full_text.append(para.text)
    return '\n'.join(full_text)

def attack():
    print_colorful_text("""
          
╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═
╠═╣ ║  ║ ╠═╣║  ╠╩╗
╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩

""")

def nma(ip):
    command = "/usr/bin/nmap -sV " + ip
    os.system(command)

def sop():
    print_colorful_text("""
                        
╔═╗╔╦╗╔═╗╔╗╔╔╦╗╔═╗╦═╗╔╦╗  ╔═╗╔═╗╔═╗╦═╗╔═╗╔╦╗╦╔╗╔╔═╗  ╔═╗╦═╗╔═╗╔═╗╔═╗╔╦╗╦ ╦╦═╗╔═╗
╚═╗ ║ ╠═╣║║║ ║║╠═╣╠╦╝ ║║  ║ ║╠═╝║╣ ╠╦╝╠═╣ ║ ║║║║║ ╦  ╠═╝╠╦╝║ ║║  ║╣  ║║║ ║╠╦╝║╣ 
╚═╝ ╩ ╩ ╩╝╚╝═╩╝╩ ╩╩╚══╩╝  ╚═╝╩  ╚═╝╩╚═╩ ╩ ╩ ╩╝╚╝╚═╝  ╩  ╩╚═╚═╝╚═╝╚═╝═╩╝╚═╝╩╚═╚═╝

""")
    print("""Reconnaissance - Getting information about the target network to identify vulnerabilities and security holes. Cybercriminals could use social engineering at this stage.

Weaponization - Creating or adapting malware to the vulnerabilities reached in the organization to be attacked.

Delivery - Sending the malware (weapon) to the target via USB, mail, or other means.

Exploitation - Exploiting a vulnerability that executes code in the system. 

Installation installing malware.

Command and control - Getting continued access to the target to control it and manipulate it remotely. 

Actions on objectives - Taking steps to achieve the goals such as data destruction, encryption, or exfiltration.
          """)

def mainPage():
    global opts
    print()
    print()
    print("""[ 1 ] Team Chat
[ 2 ] Attack
[ 3 ] Nmap
[ 4 ] Rules of Engagement
[ 5 ] Standard Operating Procedures""")
    opts = input("-> ")

print('OK')
print()
print()

try:
    
    while True:
        mainPage()
        
        ####TeamChat####
        if opts == "1":
            teamchatThread = threading.Thread(target=receive)
            teamchatThread.start()
            print("teamserver opened successfully!")
            opts = input("Press any key to out")
        
        elif opts == "2":
            attack()
            os.system('/usr/bin/nc -lvp 4444')

        elif opts == "3":
            print_colorful_text_green("""

╔╗╔╔╦╗╔═╗╔═╗
║║║║║║╠═╣╠═╝
╝╚╝╩ ╩╩ ╩╩  
            
                        
""")
            try:
                nm = input("Target IP : ")
                print()
                nma(nm)
                print()
                opts = input("Press any key to out")
            except:
                pass

        
        elif opts == "4":
            print(ROE())
            print()
            opts = input("Press any key to out")
        
        elif opts == "5":
            sop()
            opts = input("Press any key to out")
        
       
except:
    print("Unexpected Error.")
    quit




    

