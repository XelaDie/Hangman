RESET = "\033[0m"
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"

msg_menu = f"""
{BLUE}MENU:{RESET}
    1. {CYAN}Play the game against the computer{RESET}
    2. {CYAN}Play the game against a friend{RESET}
    3. {CYAN}How to play{RESET}
    4. {CYAN}Enable/Disable Text-to-speach{RESET} 
    5. {CYAN}Exit{RESET}
"""

msg_htp = """
How to Play Hangman:
    1. Choose to play against the computer or a friend.
    2. If playing against the computer, select a wordlist difficulty.
    3. Guess letters or the whole word to reveal the hidden word.
    4. You have 6 tries before the game is over.
    5. If you guess the word correctly, you win!
    6. If you fail to guess the word in 6 tries, you lose.
"""

msg_wordlist = f"""Choose a wordlist difficulty:
    1. {GREEN}Easy{RESET}
    2. {YELLOW}Medium{RESET}
    3. {RED}Hard{RESET}
    4. {MAGENTA}Custom{RESET}
"""

msg_choice = "Enter your choice: "

msg_custom = "Enter custom words separated by commas: "

msg_guess = "Try to guess a letter or the word: "

msg_already = f"{RED}Aleardy guessed this letter!{RESET}"

msg_guesser = f"{YELLOW}Friend, please enter the word to be guessed: {RESET}"

msg_good = f"{GREEN}Great Job, you guessed a letter!{RESET}"

msg_bad = f"{RED}Wrong guess! Try again!{RESET}"

msg_invalid = f"{RED}Invalid Input!{RESET}"

msg_won = f"""{GREEN}Congratulations! You guessed the word correctly!{RESET}
        The Word was: {YELLOW}"""

msg_lost = f"""{RED}You lost! Better luck next time!{RESET}
        The Word was: {YELLOW}"""

msg_end = f"""{BLUE}

###########################################################
            Thanks for playing Hangman! Goodbye!
###########################################################

{RESET}
"""

msg_interrupt = f"""{RED}

###########################################################
  Game interrupted. Thanks for playing Hangman! Goodbye!
###########################################################

{RESET}
"""

msg_restart = f"""{MAGENTA}
┌─────────────────────────────────────────────────┐
│                                                 │
│     ____ ____ ____ ___ ____ ____ ___    __.     │
│     |__/ |___ [__   |  |__| |__/  |      _]     │
│     |  \ |___ ___]  |  |  | |  \  |      .      │
│                                                 │
└─────────────────────────────────────────────────┘
                     Enter Y/N{RESET}
"""

logo = f"""
###########################################################{YELLOW}
 _____                                              _____ 
( ___ )--------------------------------------------( ___ )
 |   |                                              |   | 
 |   |                                              |   | 
 |   |      _  _ ____ _  _ ____ _  _ ____ _  _      |   | 
 |   |      |__| |__| |\ | | __ |\/| |__| |\ |      |   | 
 |   |      |  | |  | | \| |__] |  | |  | | \|      |   | 
 |   |                                              |   | 
 |___|                                              |___| 
(_____)--------------------------------------------(_____){RESET}"""

line="""
###########################################################
"""

msg_stages = [f"""
      _______
     |/      |
     |
     |
     |
     |
     |
    _|___
          """,
    f"""
      _______
     |/      |
     |      {RED}(_){RESET}
     |
     |
     |
     |
    _|___
          """,
    f"""
      _______
     |/      |
     |      (_)
     |       {RED}|{RESET}
     |       {RED}|{RESET}
     |
     |
    _|___
          """,
    f"""
      _______
     |/      |
     |      (_)
     |      {RED}\{RESET}|
     |       |
     |
     |
    _|___
          """,
    f"""
      _______
     |/      |
     |      (_)
     |      \|{RED}/{RESET}
     |       |
     |
     |
    _|___
          """,
    f"""
      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      {RED}/{RESET}
     |
    _|___
          """,
    f"""
      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / {RED}\\{RESET}
     |
    _|___
          """
]