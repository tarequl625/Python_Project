import pyttsx3

#simple text to speech
pyttsx3.speak("This is simple text to speech python module")

#Voice & Volumn change
#Male Voice
engine = pyttsx3.init() # object creation

# RATE
rate = engine.getProperty('rate')   # getting details of current speaking rate
print (rate)                        # printing current voice rate
engine.setProperty('rate', 120)     # setting up new voice rate

# VOLUME
volume = engine.getProperty('volume')   # getting to know current volume level (min=0 and max=1)
print (volume)                          # printing current volume level
engine.setProperty('volume',0.5)        # setting up volume level  between 0 and 1

# VOICE
voices = engine.getProperty('voices')       # getting details of current voice
engine.setProperty('voice', voices[0].id)  # changing index, changes voices. o for male
#engine.setProperty('voice', voices[1].id)   # changing index, changes voices. 1 for female

engine.say("This is simple text to speech python module")
engine.say('My current speaking rate is ' + str(rate))
engine.runAndWait()
engine.stop()

# Saving Voice to a file
# On Linux, make sure that 'espeak-ng' is installed
engine.save_to_file('This is simple text to speech python module', 'test.mp3')
engine.runAndWait()

#FeMale Voice
engine = pyttsx3.init() # object creation

# RATE
rate = engine.getProperty('rate')   # getting details of current speaking rate
print (rate)                        # printing current voice rate
engine.setProperty('rate', 120)     # setting up new voice rate

# VOLUME
volume = engine.getProperty('volume')   # getting to know current volume level (min=0 and max=1)
print (volume)                          # printing current volume level
engine.setProperty('volume',0.5)        # setting up volume level  between 0 and 1

# VOICE
voices = engine.getProperty('voices')       # getting details of current voice
#engine.setProperty('voice', voices[0].id)  # changing index, changes voices. o for male
engine.setProperty('voice', voices[1].id)   # changing index, changes voices. 1 for female

engine.say("This is simple text to speech python module")
engine.say('My current speaking rate is ' + str(rate))
engine.runAndWait()
engine.stop()

# Saving Voice to a file
# On Linux, make sure that 'espeak-ng' is installed
engine.save_to_file('This is simple text to speech python module', 'test.mp3')
engine.runAndWait()

#Male & Female Voice
engine = pyttsx3.init() # object creation

# RATE
rate = engine.getProperty('rate')   # getting details of current speaking rate
print (rate)                        # printing current voice rate
engine.setProperty('rate', 120)     # setting up new voice rate

# VOLUME
volume = engine.getProperty('volume')   # getting to know current volume level (min=0 and max=1)
print (volume)                          # printing current volume level
engine.setProperty('volume',0.5)        # setting up volume level  between 0 and 1

# VOICE
voices = engine.getProperty('voices')       # getting details of current voice
#engine.setProperty('voice', voices[0].id)  # changing index, changes voices. o for male
engine.setProperty('voice', voices[0].id)   # changing index, changes voices. 1 for female

engine.say("This is simple text to speech python module")
engine.say('My current speaking rate is ' + str(rate))
engine.runAndWait()

#FeMale Voice
engine = pyttsx3.init() # object creation

# RATE
rate = engine.getProperty('rate')   # getting details of current speaking rate
print (rate)                        # printing current voice rate
engine.setProperty('rate', 120)     # setting up new voice rate

# VOLUME
volume = engine.getProperty('volume')   # getting to know current volume level (min=0 and max=1)
print (volume)                          # printing current volume level
engine.setProperty('volume',0.5)        # setting up volume level  between 0 and 1

# VOICE
voices = engine.getProperty('voices')       # getting details of current voice
#engine.setProperty('voice', voices[0].id)  # changing index, changes voices. o for male
engine.setProperty('voice', voices[1].id)   # changing index, changes voices. 1 for female

engine.say("This is simple text to speech python module")
engine.say('My current speaking rate is ' + str(rate))
engine.runAndWait()