from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_URL = "https://api.dictionaryapi.dev/api/v2/entries/en/"


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        word = request.form.get("word")
        if word:
            response = requests.get(API_URL + word)
            if response.status_code == 200:
                data = response.json()[0]  # take first meaning
                return render_template("result.html", word=word, data=data)
            else:
                error = "Word not found. Try another one!"
                return render_template("home.html", error=error)
    return render_template("home.html")


if __name__ == "__main__":
    app.run(debug=True)