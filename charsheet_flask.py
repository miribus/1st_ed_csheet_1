import character_gui, sys, os
from flask import Flask, request, render_template, redirect, url_for, Response
from werkzeug.utils import secure_filename

name = ""
choice = ""
method = False
methodv = False
methodv_choice = False
soclass = ""

app = Flask(__name__)
if __name__ == '__main__':
    app.run(debug=True)

@app.route('/', methods=["POST", "GET"])
def mainpage():
    choices = character_gui.rollchoices
    return render_template('rollsheet.html', choices=choices)

@app.route("/race_choices", methods=["POST", "GET"])
def racepage():
    #print("y")
    global method, methodv, methodv_choice, name, choice
    methodv_choice, methodv, abilities, choice = character_gui.roll_method(str(request.form['choices']), method)
    name = character_gui.playerSheet("NewChar", methodv, abilities, methodv_choice)
    if choice == "3":
        return render_template('selfrolls.html')
    return choice

@app.route("/self_rolls", methods=["POST", "GET"])
def selfrolls():
    global name, choice, soclass
    name.char_abilities["STR"] = str(request.form['str'])
    name.char_abilities["INT"] = str(request.form['int'])
    name.char_abilities["WIS"] = str(request.form['wis'])
    name.char_abilities["DEX"] = str(request.form['dex'])
    name.char_abilities["CON"] = str(request.form['con'])
    name.char_abilities["CHA"] = str(request.form['cha'])
    name.char_abilities["CMS"] = str(request.form['cms'])
    soclass = str(request.form['social'])
    name, valid = character_gui.selfrolls(choice, name)
    if not valid:
        return "Illegal Character rolls, try again."
    else:
        return str(name.char_abilities["STR"])