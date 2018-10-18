import socket

bind_ip = "0.0.0.0" #change as needed
bind_port = 21 #change as needed

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((bind_ip,bind_port))
server.listen(10)
print("[*] Listening on " + bind_ip + ":" + str(bind_port)) 

def handle_client(client_socket):
    client_socket.send(b"220 (vsFTPd 3.0.3)\n")
    usernameRequest = client_socket.recv(1024)
    print("[+] Potential Username ---> " + str(usernameRequest))
    client_socket.send(b"331 Please specify the password.\n")
    passwordRequest = client_socket.recv(1024)
    print("[+] Potential Password ---> " + str(passwordRequest))
    client_socket.send(b"320 Login successful.\n")
    client_socket.close()

while True:
    client,addr = server.accept()
    print("[!] Received a connection from " + str(addr[0]) + ":" + str(addr[1]))
    handle_client(client)



