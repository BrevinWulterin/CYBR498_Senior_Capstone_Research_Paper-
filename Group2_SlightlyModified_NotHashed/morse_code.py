#!/usr/bin/env python3

"""
Python program to translate to and from Morse code.

https://en.wikipedia.org/wiki/Morse_code
"""

# fmt: off
MORSE_CODE_DICT = {
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.", "G": "--.",
    "H": "....", "I": "..", "J": ".---", "K": "-.-", "L": ".-..", "M": "--", "N": "-.",
    "O": "---", "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...", "T": "-", "U": "..-",
    "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--", "Z": "--..", "1": ".----",
    "2": "..---", "3": "...--", "4": "....-", "5": ".....", "6": "-....", "7": "--...",
    "8": "---..", "9": "----.", "0": "-----", "&": ".-...", "@": ".--.-.",
    ":": "---...", ",": "--..--", ".": ".-.-.-", "'": ".----.", '"': ".-..-.",
    "?": "..--..", "/": "-..-.", "=": "-...-", "+": ".-.-.", "-": "-....-",
    "(": "-.--.", ")": "-.--.-", "!": "-.-.--", " ": "/"
}  # Exclamation mark is not in ITU-R recommendation
# fmt: on
REVERSE_DICT = {value: key for key, value in MORSE_CODE_DICT.items()}


def encrypt(message: str) -> str:
    """
    >>> encrypt("Sos!")
    '... --- ... -.-.--'
    >>> encrypt("SOS!") == encrypt("sos!")
    True
    """
    return " ".join(MORSE_CODE_DICT[char] for char in message.upper())


def decrypt(message: str) -> str:
    """
    >>> decrypt('... --- ... -.-.--')
    'SOS!'
    """
    return "".join(REVERSE_DICT[char] for char in message.split())


def main() -> None:
    """
    >>> s = "".join(MORSE_CODE_DICT)
    >>> decrypt(encrypt(s)) == s
    True
    """
    message = "Morse code here!"
    print(message)
    message = encrypt(message)
    print(message)
    message = decrypt(message)
    print(message)


if __name__ == "__main__":
    main()
I stay out too late
Got nothing in my brain
That's what people say, mm-mm
That's what people say, mm-mm
I go on too many dates
But I can't make 'em stay
At least that's what people say, mm-mm
That's what people say, mm-mm
But I keep cruisin'
Can't stop, won't stop movin'
It's like I got this music in my mind
Sayin', "It's gonna be alright"
'Cause the players gonna play, play, play, play, play
And the haters gonna hate, hate, hate, hate, hate
