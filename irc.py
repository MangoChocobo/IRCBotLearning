import socket
import sys

class IRC:
    irc = socket.socket()

    def __init__(self):
        self.irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM);

    def send(self, chan, msg):
        self.irc.send("PRIVMSG " + chan + " " + msg + "n");

    def connect(self, server, channel, botnick):
        #defines the socket
        print ("connecting to: " + server);
        self.irc.connect((server, 6667));       #Connects to server
        self.irc.send("USER " + botnick + " " + botnick + " " + botnick + " :This is a bot for fun!n");     #User Authentication
        self.irc.send("NICK " + botnick + "n");
        self.irc.send("JOIN " + channel + "n");     #join the channel

    def get_text(self):
        text = self.irc.recv(2040);     #recieve the texts

        if(text.find('Ping') != -1):
            self.irc.send('Pong ' + text.split() [1] + 'rn');

        return text;