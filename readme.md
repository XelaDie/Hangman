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

## How to Play
1. The game randomly selects a word from a predefined list.
2. Players guess letters one at a time.
3. Correct guesses reveal the letter in the word.
4. Incorrect guesses decrease the number of remaining attempts.
5. The game ends when the word is fully guessed or the attempts run out.
