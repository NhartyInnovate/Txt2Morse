from flask import Flask, render_template, request
from app import text_to_morse, morse_to_text

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
    error = ""
    mode = "text2morse"
    input_text = ""

    if request.method == "POST":
        input_text = request.form.get("text", "")
        mode = request.form.get("mode", "text2morse")

        try:
            if mode == "morse2text":
                result = morse_to_text(input_text)
            else:
                result = text_to_morse(input_text)
        except ValueError as e:
            error = str(e)

    return render_template("index.html", result=result, error=error, mode=mode, input_text=input_text)

if __name__ == "__main__":
    app.run(debug=True)
