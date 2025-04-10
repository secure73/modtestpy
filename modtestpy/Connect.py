class Connect:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def connect(self):
        # Simulate a connection to the server
        print(f"Connecting to {self.host}:{self.port}...")
        # Here you would add the actual connection logic
        print("Connected!")