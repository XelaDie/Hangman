from gtts import gTTS
from playsound import playsound
import time
import keyboard
import os

RESET = f"\033[0m"
RED = f"\033[91m"
GREEN = f"\033[92m"
YELLOW = "\033[93m"

def toggle_tts(tts):
    filename='DataFlair.mp3'
    try:
        if tts: 
            message = "Text-to-speech is enabled"
            print(f"{GREEN}{message}{RESET}")
            print("You can skip TTS before it starts by pressing CTRL")
        else: 
            message = "Text-to-speech is disabled"
            print(f"{RED}{message}{RESET}")
        
        speech = gTTS(text=message, lang='en')
        speech.save(filename)
        playsound(filename)
        os.remove(filename)
        return tts
    
    except Exception as e:
        print(f"An error occurred: {e}")

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
    if(skip()): return
    filename='DataFlair.mp3'
    speech = gTTS(text=message, lang='en')
    speech.save(filename)
    playsound(filename)
    os.remove(filename)
    
def speak_word(message):
    if(skip()): return
    for i in message:
        filename='DataFlair.mp3'
        speech = gTTS(text=i, lang='en')
        speech.save(filename)
        playsound(filename)
        os.remove(filename)



tts_menu = """
MENU:
Press 1 to play the game against the computer
Press 2 to Play the game against a friend
Press 3 for How to play
Press 4 to disable text-to-speech
Press 5 to Exit
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
Press 1 to Select Easy
Press 2 to Select Medium
Press 3 to Select Hard
Press 4 to Select Custom
"""

tts_custom = "Enter custom words separated by commas: "

tts_guess = "Try to guess a letter or the word: "

tts_already = "You already guessed this letter!"

tts_guesser = "Friend, please enter the word to be guessed: "

tts_good = "Great job, you guessed a letter!"

tts_bad = "Wrong guess! Try again!"

tts_invalid = "Invalid input!"

tts_won = "Congratulations! You guessed the word correctly! The word was: "

tts_lost = "You lost! Better luck next time! The word was: "

tts_end = "Thanks for playing Hangman! Goodbye!"

tts_restart = "Want to Restart? Enter Y for yes, or N for no"

tts_stages=[
"The noose is currently empty",
"You are on your first mistake, the head is drawn.",
"You are on your second mistake, the torso is drawn.",
"You are on your third mistake, the left arm is drawn.",
"You are on your forth mistake, the right arm is drawn. Two more mistakes and you lose",
"You are on your fifth mistake, the left leg is drawn. Two more mistakes and you lose",
"You are on your last mistake, the man is hunged"   
]