from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/activity/1")
def activity_one_hardcoded():
    return "Please do five jumping jacks."

@app.route("/activity/2")
def activity_two_hardcoded():
    return "if x + 2 = 5, what is x?"

@app.route("/activity/3")
def activity_three_hardcoded():
    return "Write a personal essay about your favorite childhood memory."

@app.route("/activity/4")
def activity_four_hardcoded():
    return "What is capital of Kentucky?"

@app.route("/activity/5")
def activity_five_hardcoded():
    return "List 5 US presidents."

@app.route("/activity/6")
def activity_six_hardcoded():
    return "Draw a picture of a tree."

@app.route("/activity/7")
def activity_seven_hardcoded():
    return "Arrange a set of Tangrams in a square."