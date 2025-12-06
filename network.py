import socket
import pickle


class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.settimeout(10)  # 10 second timeout
        self.server = "rps-game-server.onrender.com"
        self.port = 5000
        self.addr = (self.server, self.port)
        self.p = self.connect()
        self.connected = self.p is not None

    def getP(self):
        return self.p if self.p else "0"

    def connect(self):
        try:
            print(f"Attempting to connect to {self.server}:{self.port}...")
            self.client.connect(self.addr)
            print("Connected! Waiting for player assignment...")
            return self.client.recv(2048).decode()
        except socket.timeout:
            print(f"Connection timeout: Server at {self.server}:{self.port} did not respond within 10 seconds")
            return None
        except Exception as e:
            print(f"Connection failed: {e}")
            return None

    def send(self, data):
        try:
            self.client.send(str.encode(data))
            return pickle.loads(self.client.recv(2048 * 2))
        except socket.error as e:
            print(f"Send error: {e}")
            return None
