import time, sys
import io
import sr
import string
import my_bot

# NOTE: this requires PyAudio because it uses the Microphone class

r = sr.Recognizer()
sentences = []
playing = True

start_time = ""

IRC_BOT = my_bot.Bot()
IRC_BOT.connect_to_server()
IRC_BOT.say_hello()

for c in time.asctime():
    if c == ':':
        start_time += "."
    else:
        start_time += str(c)
    
def Go():
    global playing
    if playing == True:
        with sr.Microphone() as source:                # use the default microphone as the audio source
            audio = r.listen(source)                   # listen for the first phrase and extract it into audio data
        try:
            #just some basic timestamp recording. eliminating day of week and year to make it look neater
            string_time = time.asctime()
            count = 0
            for c in string_time:
                if c == " ":
                    string_time = string_time[count+1:]
                    break
                count += 1
            count = 0
            for c in reversed(string_time):
                if c == " ":
                    string_time = string_time[:-count]
                    break
                count += 1
            ################################################################################################
                
            print(r.recognize(audio))
            IRC_BOT.say_message(r.recognize(audio))
            sentences.append(string_time + ": " + r.recognize(audio)+"\n\r")
            
            if r.recognize(audio) == "goodbye":
                playing = False

                ##write speech said to text file
                global start_time
                string_time = start_time
                count1 = 0
                for c in reversed(string_time):
                    if c == " ":
                        string_time = string_time[:-count1]
                        break
                    count1 += 1

                
                file_object = open(string_time + ".txt", 'w')
                for i in sentences:
                    file_object.write(i)
                file_object.close()
                ################################
                
                print("Ending recording")
            Go()
        except LookupError:#audio is unreadable
            print("Audio is unreadable")
            Go()


while True:
    if playing == True:
        Go()
    else:
        sys.exit()
