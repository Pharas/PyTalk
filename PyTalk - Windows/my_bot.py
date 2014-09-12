#!/usr/bin/env python

import socket
import re

class Bot():
    # Change into values that suit you.

    #TODO - ASSIGN THESE VALUES BASED ON USER INPUT
    NETWORK = 'chat.freenode.net'
    PORT = 6667
    nick = 'pytalk-bot'
    channel = '##pytalk-test'
    owner = 'mtubinis'

    def __init__(self):
        self.quit_bot = False
        self.command_list = []  # initialy we have not received any command.
        self.data_buffer = ''  # no data received yet.
        self.rexp_general = re.compile(r'^(:[^ ]+)?[ ]*([^ ]+)[ ]+([^ ].*)?$')

    def connect_to_server(self):
        self.irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.irc.connect((self.NETWORK, self.PORT))
        self.irc.send('NICK ' + self.nick + '\r\n')
        self.irc.send('USER ' + self.nick + ' Ztbot Ztbot :Python IRC Bot\r\n')
        self.irc.send('JOIN ' + self.channel + '\r\n')

    def say_hello(self):
        # Say hello!
        self.irc.send('PRIVMSG '+ self.channel +" :Hello, this is the PY-Talk IRC Bot!\n")
    def say_message(self,message):
        self.irc.send('PRIVMSG '+ self.channel +" :"+message+"\n")

    def parse_command(self, data):
        p = self.rexp_general
        r = p.search(data)
        if r is None:
            # command does not match.
            print "command does not match."
            return

        g = r.groups()
        print g
        sender = g[0]
        cmd = g[1]
        params = g[2]

        if cmd == 'PING':
            self.irc.send('PONG ' + params + '\r\n')
            return
        elif cmd == 'KICK':
            self.irc.send('JOIN ' + self.channel + '\r\n')
            return
        elif cmd == 'PRIVMSG':
            quit_rex = r'%s:[ ]+(quit|QUIT)' % self.nick
            if re.search(quit_rex, params) is not None:
                s_expr = 'PRIVMSG %s :OK, I am quitting now!\r\n' % self.owner
                self.irc.send(s_expr)
                self.irc.send('QUIT\r\n')
                self.quit_bot = True
                return
            hi_rex = r'(hi|hello|hola)[ ]+%s' % self.nick
            if re.search(hi_rex, params) is not None:
                msg = 'Hi, I am a pythonic irc bot!\r\n'
                self.irc.send('PRIVMSG %s :%s\r\n' % (self.channel, msg))
                return

    def get_command(self):

        if len(self.command_list) > 0:
            result = self.command_list.pop(0)
            return result

        # There is no command available, we read more bytes.
        chunk = self.irc.recv(4096)
        self.data_buffer = ''.join([self.data_buffer, chunk])

        self.command_list = self.data_buffer.split('\r\n')
        self.data_buffer = self.command_list.pop()
        if len(self.command_list) == 0:
            return None

        result = self.command_list.pop(0)
        return result

    def main(self):

        self.connect_to_server()
        self.say_hello()

        while True:

            com = self.get_command()
            while com is None:
                com = self.get_command()
            print "com: ", com

            self.parse_command(com)
            if self.quit_bot == True:
                break

if __name__ == '__main__':
    myBot = Bot()
    myBot.main()
