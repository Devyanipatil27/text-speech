from gtts import gTTS # we import this module for text to speech conversion
import os

#if you want from file that you can change this
abc=open("sample.text")
text=abc.read()

language = "en" # en for english language

obj = gTTS(text =text, lang=language,slow=False)
# we have use slow=False because our converted video will have high speed

obj.save("sample.mp3")

#to open the video file automatically we have to import os 
os.system("sample.mp3")