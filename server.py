import os
from random import randint

from flask import Flask, render_template

# ---------create flask app
app = Flask(__name__)

# ---------gen random number
random_number = randint(1, 9)


# ---------homepage
@app.route('/')
def home():
    return render_template("index.html")


# ---------run server when you run this script
if __name__ == "__main__":
    app.run(debug=True)