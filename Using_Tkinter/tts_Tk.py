from gtts import gTTS
from playsound import playsound
import time
import keyboard
import os

isEnabled = False

def toggle_tts():
    global isEnabled
    if isEnabled:
        isEnabled = False
        message="Text-to-speech is disabled"
        tts = gTTS(text=message, lang='en')
        filename = "DataFlair.mp3"
        tts.save(filename)
        playsound(filename)
        os.remove(filename)
    else:
        isEnabled = True
        speak("Text-to-speech is enabled")

def skip():
    start_time = time.time()
    while True:
        skip = keyboard.is_pressed("ctrl")
        if skip:
            return True
        elapsed_time = time.time() - start_time
        if elapsed_time >= 1:
            return False

def speak(message):
    global isEnabled
    if not isEnabled:
        return
    if(skip()): return
    try:
        tts = gTTS(text=message, lang='en')
        filename = "DataFlair.mp3"
        tts.save(filename)
        playsound(filename)
        os.remove(filename)
        
    except Exception as e: print(f"An error occurred: {e}")
    
def speak_word(message):
    global isEnabled
    if not isEnabled:
        return
    if(skip()): return
    try:
        for i in message:
            tts = gTTS(text=i, lang='en')
            filename = "DataFlair.mp3"
            tts.save(filename)
            playsound(filename)
            os.remove(filename)
        
    except Exception as e: print(f"An error occurred: {e}")
    
    
tts_menu = """
MENU:
Play the game against the computer
Play the game against a friend
How to play
Disable text-to-speech
Exit
"""

tts_htp = """
How to Play Hangman:
1, Choose to play against the computer or a friend.
2, If playing against the computer, select a wordlist difficulty.
3, Guess letters or the whole word to reveal the hidden word.
4, You have 6 tries before the game is over.
5, If you guess the word correctly, you win.
6, If you fail to guess the word in 6 tries, you lose.
"""

tts_wordlist = """
Choose a wordlist difficulty:
Easy
Medium
Hard
Custom
"""

tts_custom = "Enter custom words separated by commas: "

tts_guess = "Try to guess a letter or the word: "

tts_already = "You already guessed this letter!"

tts_guesser = "Friend, please enter the word to be guessed: "

tts_good = "Great job, you guessed a letter!"

tts_bad = "Wrong guess! Try again!"

tts_invalid = "Invalid input!"

tts_restart = "Want to Restart?"

tts_stages=[
"The noose is currently empty",
"You are on your first mistake, the head is drawn.",
"You are on your second mistake, the torso is drawn.",
"You are on your third mistake, the left arm is drawn.",
"You are on your forth mistake, the right arm is drawn. Two more mistakes and you lose",
"You are on your fifth mistake, the left leg is drawn. Two more mistakes and you lose",
"You are on your last mistake, the man is hunged"   
]