from ux_Ter import logo, line, msg_menu, msg_stages, msg_htp, msg_wordlist, msg_guesser, msg_choice, msg_custom, msg_guess
from ux_Ter import msg_already, msg_good, msg_bad, msg_won, msg_lost, msg_restart, msg_end, msg_invalid, msg_interrupt
from tts_Ter import toggle_tts, speak, speak_word
from tts_Ter import tts_menu, tts_stages, tts_htp, tts_wordlist, tts_guesser, tts_custom, tts_guess
from tts_Ter import tts_already, tts_good, tts_bad, tts_won, tts_lost, tts_restart, tts_end, tts_invalid
from random import randint
import re

regex = '^[A-Za-z]+$'
RESET = "\033[0m"
RED = "\033[91m"

def mainmenu():
    print(logo)
    isEnabled = False
    while True:
        print(line)
        print(msg_menu)
        if isEnabled: speak(tts_menu)
        choice = input(msg_choice)
        
        if choice == '1':   # Against Computer
            choose_wordlist(isEnabled)
        elif choice == '2': # Against Friend
            play_game(True, [], isEnabled)
        elif choice == '3': # How to Play
            print(line)
            print(msg_htp)
            if isEnabled: speak(tts_htp)
        elif choice == '4': # Enable/Disable tts
            isEnabled = not isEnabled
            toggle_tts(isEnabled)
        elif choice == '5': # Exit
            print(msg_end)
            if isEnabled: speak(tts_end)
            return
        else:
            print(msg_invalid)
            if isEnabled: speak(tts_invalid)

def choose_wordlist(isEnabled):
    easy = ["pizza", "hamburger", "shawarma", "salad", "cheese", "fajita", "fries"]
    medium = ["elephant", "giraffe", "dolphin", "kangaroo", "alligator", "squirrel", "meerkat", "penguin", "octopus", "chimpanzee"]
    hard = ["hippopotamus", "chrysanthemum", "quintessential", "juxtaposition", "cryptocurrency", "philanthropy", "unconventional"]
    
    while True:
        print(line)
        print(msg_wordlist)
        if isEnabled: speak(tts_wordlist)
        
        choice = input(msg_choice)
        if choice == '1':
            play_game(False, easy, isEnabled)
            return
        elif choice == '2':
            play_game(False, medium, isEnabled)
            return
        elif choice == '3':
            play_game(False, hard, isEnabled)
            return
        elif choice == '4':
            isValid = True
            if isEnabled: speak(tts_custom)
            custom_wordlist = input(msg_custom).split(',')
            for i in range(len(custom_wordlist)):
                custom_wordlist[i] = custom_wordlist[i].lower().strip()
                if not re.search(regex, custom_wordlist[i]):
                    print(msg_invalid)
                    if isEnabled: speak(tts_invalid)
                    isValid = False
                    break
            if isValid:
                play_game(False, custom_wordlist, isEnabled)
                return
        else:
            print(msg_invalid)
            if isEnabled: speak(tts_invalid)

def play_game(friend, wordlist, isEnabled):
    print(line)
    won = False
    lost = False

    if not friend:
        if len(wordlist) == 1: word = wordlist[0]
        else: word = wordlist[randint(0, len(wordlist) - 1)]
    else:
        while True:
            if isEnabled: speak(tts_guesser)
            word = input(msg_guesser).lower().strip()
            if re.search(regex, word):
                break
            else:
                print(msg_invalid)
                if isEnabled: speak(tts_invalid)
        
    guessed_letters = []
    guessed_word = ""
    tries = 0
    discovered_word = "-" * len(word)
    tts_discovered_word = ""
    indices = []
    
    while not won and not lost:
        print(msg_stages[tries])
        if isEnabled: speak(tts_stages[tries])
        print(discovered_word, '\n')
        if isEnabled: 
            speak(f"What has been discovered is")
            speak_word(discovered_word)
        
        if tries == 6:
            lost = True
            msg_l = msg_lost + word + RESET
            print(msg_l)
            if isEnabled: speak(tts_lost + word)
            break
        
        if isEnabled: speak(tts_guess)
        guess = input(msg_guess)
        if not re.search(regex, guess):
            print(msg_invalid)
            if isEnabled: speak(tts_invalid)
            continue
        guess = guess.lower()
        
        if len(guess) == 1:  # User guessed a letter
            if guess in guessed_letters:
                print(msg_already)
                if isEnabled: speak(tts_already)
                continue
            guessed_letters.append(guess)
            indices = [i for i in range(len(word)) if word.startswith(guess, i)]
            
            if len(indices) > 0:
                for i in indices:
                    discovered_word = discovered_word[:i] + guess + discovered_word[i + 1:]
                print(msg_good)
                if isEnabled: speak(tts_good)
            else:
                tries += 1
                print(msg_bad)
                if isEnabled: speak(tts_bad)
        else:  # User guessed the word
            guessed_word = guess
            if guessed_word == word:
                won = True
                msg_w = msg_won + word + RESET
                print(msg_w)
                if isEnabled: speak(tts_won + word)
            else:
                tries += 1
                print(msg_bad)
                if isEnabled: speak(tts_bad)
        
        if discovered_word == word:
            won = True
            msg_w = msg_won + word + RESET
            print(msg_w)
            if isEnabled: speak(tts_won + word)
    
    while True:
        print(msg_restart)
        if isEnabled: speak(tts_restart)
        reset = input()
        reset = reset.lower()
        if reset == "y":
            play_game(friend, wordlist, isEnabled)
            break
        elif reset == "n":
            return
        else:
            print(msg_invalid)
            if isEnabled: speak(tts_invalid)

if __name__ == "__main__":
    try:
        mainmenu()
    except KeyboardInterrupt:
        print(msg_interrupt)
