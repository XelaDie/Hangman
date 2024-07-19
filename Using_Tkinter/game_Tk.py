import tkinter as tk
from tkinter import PhotoImage
from tts_Tk import toggle_tts, speak, speak_word
from tts_Tk import tts_menu, tts_stages, tts_htp, tts_wordlist, tts_guesser, tts_custom, tts_guess
from tts_Tk import tts_already, tts_good, tts_bad, tts_restart, tts_invalid
from random import randint
import re
import os

regex = '^[A-Za-z]+$'
easy_words = ["pizza", "hamburger", "shawarma", "salad", "cheese", "fajita", "fries"]
medium_words = ["elephant", "giraffe", "dolphin", "kangaroo", "alligator", "squirrel", "meerkat", "penguin", "octopus", "chimpanzee"]
hard_words = ["hippopotamus", "chrysanthemum", "quintessential", "juxtaposition", "cryptocurrency", "philanthropy", "unconventional"]
friend = False


def load_image(name):
    path = os.path.join(os.path.dirname(__file__), 'assets', f"{name}.png")
    return PhotoImage(file=path)

def show_message(window, message, fg):
    message_label = tk.Label(window, text=message, font=("Helvetica", 12), fg=fg)
    message_label.place(x=500, y=80)
    window.after(700, message_label.destroy)

def main_menu():
    root = tk.Tk()
    root.title("Hangman Game")
    root.geometry("800x800")
    global friend
    friend = False
    
    logo_img = load_image("logo")
    logo_label = tk.Label(root, image=logo_img)
    logo_label.image = logo_img
    logo_label.pack(pady=10)

    play_vs_comp_img = load_image("PVsC")
    play_vs_comp_btn = tk.Button(root, image=play_vs_comp_img, command=lambda: choose_wordlist(root))
    play_vs_comp_btn.image = play_vs_comp_img
    play_vs_comp_btn.pack(pady=10)

    play_vs_friend_img = load_image("PVsF")
    play_vs_friend_btn = tk.Button(root, image=play_vs_friend_img, command=lambda: play_vs_friend(root))
    play_vs_friend_btn.image = play_vs_friend_img
    play_vs_friend_btn.pack(pady=10)

    how_to_play_img = load_image("htp")
    how_to_play_btn = tk.Button(root, image=how_to_play_img, command=lambda: show_how_to_play(root))
    how_to_play_btn.image = how_to_play_img
    how_to_play_btn.pack(pady=10)

    toggle_tts_img = load_image("tts")
    toggle_tts_btn = tk.Button(root, image=toggle_tts_img, command=toggle_tts)
    toggle_tts_btn.image = toggle_tts_img
    toggle_tts_btn.pack(pady=10)

    exit_img = load_image("exit")
    exit_btn = tk.Button(root, image=exit_img, command=root.destroy)
    exit_btn.image = exit_img
    exit_btn.pack(pady=10)

    speak(tts_menu)

    root.mainloop()

    
def choose_wordlist(parent):
    parent.destroy()

    wordlist_window = tk.Tk()
    wordlist_window.title("Choose Wordlist")
    wordlist_window.geometry("800x800")

    logo_img = load_image("logo")
    logo_label = tk.Label(wordlist_window, image=logo_img)
    logo_label.image = logo_img
    logo_label.pack(pady=10)

    easy_img = load_image("easy")
    easy_btn = tk.Button(wordlist_window, image=easy_img, command=lambda: start_game(wordlist_window, easy_words))
    easy_btn.image = easy_img
    easy_btn.pack(pady=10)

    medium_img = load_image("medium")
    medium_btn = tk.Button(wordlist_window, image=medium_img, command=lambda: start_game(wordlist_window, medium_words))
    medium_btn.image = medium_img
    medium_btn.pack(pady=10)

    hard_img = load_image("hard")
    hard_btn = tk.Button(wordlist_window, image=hard_img, command=lambda: start_game(wordlist_window, hard_words))
    hard_btn.image = hard_img
    hard_btn.pack(pady=10)

    custom_img = load_image("custom")
    custom_btn = tk.Button(wordlist_window, image=custom_img, command=lambda: custom_wordlist(wordlist_window))
    custom_btn.image = custom_img
    custom_btn.pack(pady=10)
    
    speak(tts_wordlist)

def custom_wordlist(parent):
    parent.destroy()

    custom_window = tk.Tk()
    custom_window.title("Enter Custom Words")
    custom_window.geometry("800x800")

    label = tk.Label(custom_window, text="Enter custom words separated by commas:", font=("Calibri", 32))
    label.pack(pady=(200,50))

    entry = tk.Entry(custom_window, width=20, font=("Helvetica", 24))
    entry.pack(pady=10)

    submit_img = load_image("submit")
    submit_btn = tk.Button(custom_window, image=submit_img, command=lambda: submit_custom_words(custom_window, entry.get()))
    submit_btn.image = submit_img
    submit_btn.pack(pady=10)
    
    speak(tts_custom)

def submit_custom_words(parent, words):
    words = words.split(',')
    words = [word.strip().lower() for word in words if re.search(regex, word.strip().lower())]
    if words:
        start_game(parent, words)
    else:
        show_message(parent, "Invalid Input", "red")
        speak(tts_invalid)

def play_vs_friend(parent):
    parent.destroy()
    global friend
    friend = True
    
    friend_window = tk.Tk()
    friend_window.title("Enter Word")
    friend_window.geometry("800x800")

    label = tk.Label(friend_window, text="Friend, please enter the word to be guessed:", font=("Calibri", 32))
    label.pack(pady=(200,50))

    entry = tk.Entry(friend_window, width=20, font=("Helvetica", 24))
    entry.pack(pady=10)

    submit_img = load_image("submit")
    submit_btn = tk.Button(friend_window, image=submit_img, command=lambda: submit_friend_word(friend_window, entry.get()))
    submit_btn.image = submit_img
    submit_btn.pack(pady=10)
    
    speak(tts_guesser)

def submit_friend_word(parent, word):
    word = word.lower().strip()
    if re.search(regex, word):
        start_game(parent, [word])
    else:
        show_message(parent, "Please enter a valid word.", "red")
        speak(tts_invalid)

def show_how_to_play(parent):
    parent.destroy()

    htp_window = tk.Tk()
    htp_window.title("How to Play")
    htp_window.geometry("800x800")

    htp_bg_img = load_image("hpt")
    bg_label = tk.Label(htp_window, image=htp_bg_img)
    bg_label.image = htp_bg_img
    bg_label.place(relwidth=1, relheight=1)

    back_img = load_image("back")
    back_btn = tk.Button(htp_window, image=back_img, command=lambda: back_to_main_menu(htp_window))
    back_btn.image = back_img
    back_btn.pack(pady=(700,0),padx=(450,0))
    
    speak(tts_htp)

def back_to_main_menu(window):
    window.destroy()
    main_menu()

def start_game(parent, wordlist):
    parent.destroy()

    game_window = tk.Tk()
    game_window.title("Hangman Game")
    game_window.geometry("800x800")
    
    word = wordlist[randint(0, len(wordlist) - 1)]
    guessed_letters = []
    tries = 0
    discovered_word = "-" * len(word)

    hangman_img = load_image("h1")
    hangman_label = tk.Label(game_window, image=hangman_img)
    hangman_label.image = hangman_img
    hangman_label.pack(pady=(50, 10))

    def status():
        speak(tts_stages[tries])
        speak(f"What has been discovered is")
        speak_word(discovered_word)
        speak(tts_guess)
    
    def guess_letter(letter):
        nonlocal tries, discovered_word
        if letter in guessed_letters:
            show_message(game_window, "You already guessed this letter.", "red")
            speak(tts_already)
        else:
            guessed_letters.append(letter)
            if letter in word:
                show_message(game_window, "Great Job, you guessed a letter!", "green")
                speak(tts_good)
                indices = [i for i, l in enumerate(word) if l == letter]
                for i in indices:
                    discovered_word = discovered_word[:i] + letter + discovered_word[i + 1:]
                label_word.config(text=discovered_word)
                if discovered_word == word:
                    end_game(game_window, "Congratulations", "You guessed the word correctly!", wordlist, f"h{tries + 1}f")
                else: status()
            else:
                show_message(game_window, "Incorrect guess. Try again.", "red")
                speak(tts_bad)
                tries += 1
                hangman_img = load_image(f"h{tries + 1}")
                hangman_label.config(image=hangman_img)
                hangman_label.image = hangman_img
                if tries == 6:
                    end_game(game_window, "Game Over", f"You lost! The word was: {word}", wordlist, "h7")
                else: status()

    def guess_word():
        nonlocal tries
        guessed_word = entry.get().strip().lower()
        if guessed_word == word:
            end_game(game_window, "Congratulations", "You guessed the word correctly!", wordlist, f"h{tries + 1}f")
        else:
            show_message(game_window, "Incorrect guess. Try again.", "red")
            speak(tts_bad)
            tries += 1
            hangman_img = load_image(f"h{tries + 1}")
            hangman_label.config(image=hangman_img)
            hangman_label.image = hangman_img
            if tries == 6:
                end_game(game_window, "Game Over", f"You lost! The word was: {word}", wordlist, "h7")
            else: status()

    label_word = tk.Label(game_window, text=discovered_word, font=("Helvetica", 24))
    label_word.pack(pady=(0, 50))

    letters_frame = tk.Frame(game_window)
    letters_frame.pack(pady=25)

    for i, letter in enumerate("abcdefghijklmnopqrstuvwxyz"):
        letter_img = load_image(letter)
        letter_btn = tk.Button(letters_frame, image=letter_img, command=lambda l=letter: guess_letter(l))
        letter_btn.image = letter_img
        letter_btn.grid(row=i // 13, column=i % 13, padx=2, pady=2)

    entry = tk.Entry(game_window, width=20, font=("Helvetica", 24))
    entry.pack(pady=10)

    guess_img = load_image("guess")
    guess_btn = tk.Button(game_window, image=guess_img, command=guess_word)
    guess_btn.image = guess_img
    guess_btn.pack(pady=10)
    
    status()
    
    game_window.mainloop()

def end_game(window, title, message, wordlist, h=0):
    window.destroy()

    end_window = tk.Tk()
    end_window.title(title)
    end_window.geometry("800x800")

    logo_img = load_image("restartlogo")
    logo_label = tk.Label(end_window, image=logo_img)
    logo_label.image = logo_img
    logo_label.pack(pady=10)
        
    h_img = load_image(h)
    h_label = tk.Label(end_window, image=h_img)
    h_label.image = h_img
    h_label.pack(pady=10)

    message_label = tk.Label(end_window, text=message, font=("Helvetica", 24))
    message_label.pack(pady=10)

    restart_img = load_image("restart")
    restart_btn = tk.Button(end_window, image=restart_img, command=lambda: restart(end_window, wordlist))
    restart_btn.image = restart_img
    restart_btn.pack(pady=10)

    bcktomenu_img = load_image("bcktomenu")
    bcktomenu_btn = tk.Button(end_window, image=bcktomenu_img, command=lambda: back_to_main_menu(end_window))
    bcktomenu_btn.image = bcktomenu_img
    bcktomenu_btn.pack(pady=10)

    speak(message)
    speak(tts_restart)
    

def restart(window, wordlist):
    global friend
    if(friend): play_vs_friend(window)
    else: start_game(window, wordlist)
        

if __name__ == "__main__":
    main_menu()
