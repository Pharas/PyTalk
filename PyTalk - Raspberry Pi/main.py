import time, sys, io
import sr
import my_bot

def MakeInitFileName(timeString):
    startTime = ""
    for c in timeString:
        if c == ':':
            startTime += "."
        else:
            startTime += str(c)
    return startTime
def EliminateWeekYear(timeString):
    count = 0
    for c in timeString:
        if c == " ":
            timeString = timeString[count+1:]
            break
        count += 1
    count = 0
    for c in reversed(timeString):
        if c == " ":
            timeString = timeString[:-count]
            break
        count += 1
    return timeString

class Program(object):
    def __init__(self):
        self.r = sr.Recognizer()
        self.sentences = []
        self.playing = True
        self.start_time = MakeInitFileName(time.asctime())

        self.IRC_BOT = my_bot.Bot()
        self.IRC_BOT.main()
        
    def ListenForSound(self):
        if self.playing == True:
            with sr.Microphone() as source:   # use the default microphone as the audio source
                audio = self.r.listen(source) # listen for the first phrase and extract it into audio data
            try:
                print(self.r.recognize(audio))
                self.IRC_BOT.say_message(self.r.recognize(audio))
                self.sentences.append(EliminateWeekYear(time.asctime()) + ": " + self.r.recognize(audio)+"\n\r")
                
                if self.r.recognize(audio) == "goodbye":
                    self.playing = False
                    self.WriteLogFile()
                    
                self.ListenForSound()
            except LookupError:#audio is unreadable
                print("Audio is unreadable")
                self.ListenForSound()

    def WriteLogFile(self):
        print("Ending recording. Writing log file: " + self.start_time + ".txt")
        self.IRC_BOT.say_message("Ending recording. Writing log file: " + self.start_time + ".txt")
        
        count = 0
        for c in reversed(self.start_time):
            if c == " ":
                self.start_time = self.start_time[:-count]
                break
            count += 1        
        file_object = open(self.start_time + ".txt", 'w')
        for i in self.sentences:
            file_object.write(i)
        file_object.close()
        
    def main(self):
        while True:
            if self.playing == True:
                self.ListenForSound()
            else:
                sys.exit(0)

program = Program()
program.main()
