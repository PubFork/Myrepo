import socket
import logging
import datetime
import threading

logging.basicConfig(level=logging.INFO,format=("%(asctime)s %(threadName)s %(message)s"))

class ChatServer:
    def __init__(self,ip="127.0.0.1",port=9999):
        self.addr = (ip,port)
        self.socket = socket.socket()
        self.client = {}
        self.event = threading.Event()
        self.error = []

    def start(self):
        self.socket.bind(self.addr)
        self.socket.listen()
        threading.Thread(target=self.accept,name="accept").start()

    def accept(self):
        try:
            while not self.event.is_set():
                sock,client = self.socket.accept()
                self.client[client] = sock
                threading.Thread(target=self.recv,args=(sock,client),name='recv').start()
        except Exception as e:
            pass


    def recv(self,sock,client):
        try:
            while not self.event.is_set():
                data = sock.recv(1024)
                msg  = data.decode().strip()
                # msg = "{:%Y/%m/%d %H:%M:%S} {}:{}\n {}\n".format(datetime.datetime.now(),*client,data.decode())
                if msg == "quit":
                    self.client.pop(client)
                    sock.close()
                    logging.info(msg)

                logging.info(msg)
                for sock in self.client.values():
                    sock.send(msg.encode())
        except Exception as e:
            pass

    def stop(self):
        for sock in self.client.values():
            sock.close()
        self.socket.close()
        self.event.set()


s = ChatServer()
s.start()

e = threading.Event()
while not e.wait(1):
    cmd = input(">>>").strip()
    if cmd == "quit":
        s.stop()
        e.wait(3)
        break