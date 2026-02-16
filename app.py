from flask import Flask, render_template, request
import time

# winsound is Windows-only, so keep it optional
try:
    import winsound
except ImportError:
    winsound = None

app = Flask(__name__)

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


def play_morse(morse_code: str):
    """Plays morse audio on Windows; safely no-ops elsewhere."""
    if winsound is None:
        return  # avoid crashing on non-Windows servers

    for symbol in morse_code:
        if symbol == ".":
            winsound.Beep(800, 200)
        elif symbol == "-":
            winsound.Beep(800, 600)
        elif symbol == " ":
            time.sleep(0.2)
        elif symbol == "/":
            time.sleep(0.6)


def text_to_morse(text: str) -> str:
    text = text.upper()
    out = []
    for char in text:
        out.append(MORSE_CODE.get(char, "?"))
    return " ".join(out)


def morse_to_text(morse_code: str) -> str:
    # accept either " / " or "/" as word separator
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


@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
    error = ""
    mode = "text2morse"

    if request.method == "POST":
        user_input = request.form.get("text", "")
        mode = request.form.get("mode", "text2morse")

        try:
            if mode == "morse2text":
                result = morse_to_text(user_input)
            else:
                result = text_to_morse(user_input)

            # Optional: play morse only when generating morse
            # play_morse(result)  # Uncomment if you want it (Windows only)

        except ValueError as e:
            error = str(e)

    return render_template("index.html", result=result, error=error, mode=mode)


if __name__ == "__main__":
    app.run(debug=True)
