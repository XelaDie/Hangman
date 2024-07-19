# Hangman Game

## Description
This project consists of two versions of the Hangman game: one that runs in the terminal and another with a graphical user interface (GUI) using Tkinter.

## Installation
1. Clone the repository:
   ```
   git clone https://github.com/XelaDie/Hangman.git
   ```
2. Navigate to the project directory:
   ```
   cd hangman-game
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Running the Game
### Terminal Version
To play the Hangman game in the terminal, navigate to the Using_Terminal directory and run:
   ```
   python game_Ter.py
   ```
### Tkinter Version
To play the Hangman game with a GUI, navigate to the Using_Tkinter directory and run:
   ```
   python game_Tk.py
   ```

## Features
1. Main Menu: Choose to play against the computer, play against a friend, view how to play, enable/disable text-to-speech (TTS), or exit.
2. Word Selection: Select a difficulty level (easy, medium, hard) or provide a custom word list, or have a friend pick a word for you to guess.
3. Gameplay: Guess letters or the whole word to reveal the hidden word. You have 6 tries before the game is over. If you guess the word correctly, you win. If you fail to guess the word in 6 tries, you lose.
4. TTS: You can enable or disable tts. When enabled, it can be skipped by pressing "ctrl" in both versions.
