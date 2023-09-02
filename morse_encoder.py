import pygame
import time

# Initialize pygame mixer
pygame.mixer.init()

# Define Morse code timing (Standard Morse code timing :20 WPM)
DOT_DURATION = 200  # Duration of a dot in milliseconds (Standard: 50ms)
DASH_DURATION = 600  # Duration of a dash in milliseconds (Standard: 150ms)
UNIT_DURATION = DOT_DURATION  # Duration of a single unit

# Define Morse code representations
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    ' ': '/',',': '--..--', "'": '.----.', '"': '.-..-.', '&': '.-...', '@': '.--.-.', ')': '-.--.-', '(': '-.--.', ':': '---...', ';': '-.-.-.', '=': '-...-',
    '!': '-.-.--', '?': '..--..', '_': '..--.-', '/': '-..-.', '+': '.-.-.', '$': '...-..-',
    '.': '.-.-.-', '-': '-....-', '‧': '.-.-.-', '=': '-...-', ':': '---...', '(': '-.--.', ')': '-.--.-'
}

def play_morse_code(morse_code):
    for symbol in morse_code:
        if symbol == '.':
            pygame.mixer.Sound('dot.wav').play()
            time.sleep(DOT_DURATION / 1000)
        elif symbol == '-':
            pygame.mixer.Sound('dash.wav').play()
            time.sleep(DASH_DURATION / 1000)
        elif symbol == ' ':
            time.sleep(UNIT_DURATION / 1000)  # Pause for one unit between words
        else:
            continue

def logo():
    print(" __  __                       ______                     _           ")
    print("|  \/  |                     |  ____|                   | |          ")
    print("| \  / | ___  _ __ ___  ___  | |__   _ __   ___ ___   __| | ___ _ __ ")
    print("| |\/| |/ _ \| '__/ __|/ _ \ |  __| | '_ \ / __/ _ \ / _` |/ _ \ '__|")
    print("| |  | | (_) | |  \__ \  __/ | |____| | | | (_| (_) | (_| |  __/ |   ")
    print("|_|  |_|\___/|_|  |___/\___| |______|_| |_|\___\___/ \__,_|\___|_|   ")
    print("                                             Created by KNIGHTFALL   ")
    print()

def main():
    input_text = input("Enter text: ").upper()
    
    morse_code = ' '.join([MORSE_CODE_DICT[char] for char in input_text if char in MORSE_CODE_DICT])

    print("Morse Code:", morse_code)

    play_sound = input("Do you want to play the sound? (Y/N): ")
    if play_sound.lower() == 'y':
        play_morse_code(morse_code)

    run_again = input("Do you want to encode another text? (Y/N): ")
    if run_again.lower() != 'y':
        exit()
    else:
        main()

if __name__ == "__main__":
    logo()
    main()