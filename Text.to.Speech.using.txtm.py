# Text to speech : using text message to speech
# Import the required module for text , Google text to speech 
from gtts import gTTS 
  
# imported os for play the converted audio 
import os 
  
# write the text message for converting to speech
mytext = 'There are several APIs available to convert text to speech in python. One of such APIs is the Google Text to Speech API commonly known as the gTTS API. gTTS is a very easy to use tool which converts the text entered, into audio which can be saved as a mp3 file.'
  
# write the Language in which you want to convert 
language = 'en'
  
# myobj is object of gtts engine and passing the parameter , slow = false is covernting the audio high speed 
myobj = gTTS(text=mytext, lang=language, slow=False) 
  
# Saving the converted audio into mp3 file named 
myobj.save("txtm.mp3") 
  
# Playing the converted file # you can use also mpg321
os.system("txtm.mp3") 