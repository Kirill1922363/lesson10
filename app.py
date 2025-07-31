from flask import Flask, render_template, request, url_for

app = Flask(__name__)

COUNTRIES = [
    {"name": "Італія", "date": "15.08.2023", "price": "1200€"},
    {"name": "Іспанія", "date": "20.08.2023", "price": "950€"},
    {"name": "Франція", "date": "10.09.2023", "price": "1100€"},
]

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        if not request.form.get("name", "").strip():
            return render_template("login.html", error="Будь ласка, введіть ім'я")
        return render_template("welcome.html", username=request.form["name"])
    return render_template("login.html")

@app.route("/countries")
def countries():
    return render_template("countries.html", countries=COUNTRIES)

if __name__ == '__main__':
    app.run(debug=True)