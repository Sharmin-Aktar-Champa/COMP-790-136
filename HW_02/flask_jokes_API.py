from crypt import methods
from flask import Flask

app = Flask(__name__)

@app.route("/chickenjoke", methods=["GET"])
def getChickenJoke():
    return "Why did the  chicken cross the streets? Ha! ha, ha!"

if __name__ == '__main__':
    app.run(debug=True)
