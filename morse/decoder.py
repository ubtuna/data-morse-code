"""
This module provides functions to decode Morse code back into text.

Functions:
- decode(morse): Decodes Morse code into text, where words are separated by a pipe (|)
  and letters by a space.
- decode_word(morse_word): Decodes a single Morse-encoded word into letters.
"""
from morse.mapping import MORSE

# Reverse mapping: Morse code -> letter
MORSE_REVERSE = {code: letter for letter, code in MORSE.items()}


def decode(morse):
    """
    Decodes the given Morse code into text.
    Words (separated by |) become space-separated words.
    """
    words = morse.split("|")
    return " ".join(decode_word(word) for word in words)


def decode_word(morse_word):
    """
    Decodes a single Morse-encoded word into letters.
    """
    letters = [MORSE_REVERSE[code] for code in morse_word.split()]
    return "".join(letters)


if __name__ == "__main__":
    # Example usage for one word
    EXAMPLE_MORSE = ".... .."
    DECODED_WORD = decode_word(EXAMPLE_MORSE)
    print(f"Decoded word '{EXAMPLE_MORSE}' to text: '{DECODED_WORD}'")

    # Example usage for one sentence
    EXAMPLE_MORSE = ".... ..|--. ..- -.-- ..."
    DECODED_TEXT = decode(EXAMPLE_MORSE)
    print(f"Decoded '{EXAMPLE_MORSE}' to text: '{DECODED_TEXT}'")
