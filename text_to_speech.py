from gtts import gTTS
import os

file = open("pop.txt").read()
speech = gTTS(text=file, lang='ru', slow=False)
speech.save("pop.mp3")
os.system("pop.mp3")