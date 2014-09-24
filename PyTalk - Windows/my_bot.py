import socket

class Bot(object):
    def __init__(self):
        self.quit_bot = False
        self.NETWORK = "chat.freenode.net"
        self.PORT = 6667
        self.nick = "pytalk-bot"
        self.channel = "##pytalk-test"
        self.owner = "No Owner"

    def AwaitInput(self,text,origin):
        print(text)
        thing = str(raw_input())
        if thing != "":
            return thing
        return origin
        
    def connect_to_server(self):
        self.NETWORK = self.AwaitInput("Enter the irc server you want to join (chat.freenode.net by default, just press enter to use that server): ",self.NETWORK)
        self.nick = self.AwaitInput("Enter your irc bot nickname: ",self.nick)
        self.channel = self.AwaitInput("Enter the irc channel you would like to join (##pytalk-test by default, just press enter to use that channel): ",self.channel)
        self.owner = self.AwaitInput("Enter the irc username (in channel) that owns this bot: ",self.owner)

        self.irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.irc.connect((self.NETWORK, self.PORT))
        self.irc.send('NICK ' + self.nick + '\r\n')
        self.irc.send('USER ' + self.nick + ' Ztbot Ztbot :Python IRC Bot\r\n')
        self.irc.send('JOIN ' + self.channel + '\r\n')

    def say_hello(self):
        self.irc.send('PRIVMSG '+ self.channel +" :Hello, this is the PY-Talk IRC Bot!\n")
        
    def say_message(self, message):
        self.irc.send('PRIVMSG '+ self.channel +" :"+message+"\n")
        
    def main(self):
        self.connect_to_server()
        self.say_hello()

if __name__ == '__main__':
    myBot = Bot()
    myBot.main()
