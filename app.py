# morse.py
MORSE_CODE = {
    "A": ".-","B": "-...","C": "-.-.","D": "-..","E": ".","F": "..-.","G": "--.",
    "H": "....","I": "..","J": ".---","K": "-.-","L": ".-..","M": "--","N": "-.",
    "O": "---","P": ".--.","Q": "--.-","R": ".-.","S": "...","T": "-","U": "..-",
    "V": "...-","W": ".--","X": "-..-","Y": "-.--","Z": "--..",
    "1": ".----","2": "..---","3": "...--","4": "....-","5": ".....",
    "6": "-....","7": "--...","8": "---..","9": "----.","0": "-----",
    " ": "/"
}

REVERSE_MORSE = {v: k for k, v in MORSE_CODE.items()}


def text_to_morse(text: str) -> str:
    text = text.upper()
    return " ".join(MORSE_CODE.get(ch, "?") for ch in text)


def morse_to_text(morse_code: str) -> str:
    morse_code = morse_code.replace("/", " / ")
    words = [w.strip() for w in morse_code.split(" / ") if w.strip()]

    decoded_words = []
    for word in words:
        letters = word.split()
        decoded = []
        for letter in letters:
            if letter not in REVERSE_MORSE:
                raise ValueError(f"Invalid Morse sequence detected: {letter}")
            decoded.append(REVERSE_MORSE[letter])
        decoded_words.append("".join(decoded))

    return " ".join(decoded_words)
