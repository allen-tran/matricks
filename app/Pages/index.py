from flask import Flask, redirect, url_for, render_template

app = Flask(__name__, template_folder='../templates')

@app.route("/home")
def home():
    return render_template("base.html")

if __name__ == "__main__":
    app.run(debug = True)