import socket
import threading

class Socks5ProxyServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.host, self.port))
        
    def handle_client(self, client_socket):
        # Receive initial handshake from client
        client_hello = client_socket.recv(4096)
        
        # Respond with server handshake
        server_hello = b"\x05\x00"
        client_socket.send(server_hello)
        
        # Receive request from client
        request = client_socket.recv(4096)
        
        # Parse request
        version = request[0]
        command = request[1]
        address_type = request[3]
        
        if command == 1:  # CONNECT
            if address_type == 1:  # IPv4
                address = socket.inet_ntoa(request[4:8])
                port = int.from_bytes(request[8:10], byteorder='big')
            elif address_type == 3:  # Domain name
                address_length = request[4]
                address = request[5:5+address_length].decode('utf-8')
                port = int.from_bytes(request[5+address_length:7+address_length], byteorder='big')
                
            # Connect to target server
            target_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            target_socket.connect((address, port))
            
            # Respond to client
            response = b"\x05\x00\x00\x01"  # SOCKS5, succeeded, IPv4 address type
            response += socket.inet_aton("0.0.0.0") + (0).to_bytes(2, byteorder='big')  # Dummy IP and port
            client_socket.send(response)
            
            # Relay data between client and target server
            self.relay_data(client_socket, target_socket)
        else:
            # Unsupported command
            response = b"\x05\x07\x00\x01"  # SOCKS5, command not supported
            response += socket.inet_aton("0.0.0.0") + (0).to_bytes(2, byteorder='big')  # Dummy IP and port
            client_socket.send(response)
            
        client_socket.close()
    
    def relay_data(self, source_socket, destination_socket):
        while True:
            data = source_socket.recv(4096)
            if not data:
                break
            destination_socket.sendall(data)
    
    def start(self):
        self.server.listen(5)
        print(f"[*] Listening on {self.host}:{self.port}")
        while True:
            client_socket, client_addr = self.server.accept()
            print(f"[*] Accepted connection from {client_addr[0]}:{client_addr[1]}")
            client_handler = threading.Thread(target=self.handle_client, args=(client_socket,))
            client_handler.start()

if __name__ == "__main__":
    proxy_server = Socks5ProxyServer("127.0.0.1", 1080)
    proxy_server.start()
