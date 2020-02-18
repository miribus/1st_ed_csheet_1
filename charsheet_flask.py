import sys, os
import character_gui
import social_class_gui
import dice_gui
import char_races_gui
import char_classes_gui
from flask import Flask, request, render_template, redirect, url_for, Response
from werkzeug.utils import secure_filename

info = ""
name = ""
choice = ""
method = False
methodv = False
methodv_choice = False
soclass = False
soclassdef = ""
abilities = ""
result = False
retry = False
classes = []

app = Flask(__name__)
if __name__ == '__main__':
    app.run(debug=True)


@app.route('/', methods=["POST", "GET"])
def mainpage():
    global name, choice, method, methodv, methodv_choice, soclass, abilities, result, info, soclassdef
    name = ""
    choice = ""
    method = False
    methodv = False
    methodv_choice = False
    soclass = False
    abilities = ""
    result = False
    soclassdef = ""
    info = ""
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
    elif choice == "1":
        methodv_choices = dice_gui.methodv_choices
        #name = character_gui.playerSheet("NewChar", methodv, abilities, methodv_choice)
        name.methodv = True
        name.methodv_choice = True
        methodv = True
        methodv_choice = True
        print(name.methodv)
        return render_template('methodv_classes.html', methodv_choices=methodv_choices)
    return render_template('base_abilities.html',
                           STR=name.char_abilities["STR"],
                           INT=name.char_abilities["INT"],
                           WIS=name.char_abilities["WIS"],
                           DEX=name.char_abilities["DEX"],
                           CON=name.char_abilities["CON"],
                           CHA=name.char_abilities["CHA"],
                           CMS=name.char_abilities["CMS"])



@app.route("/self_rolls", methods=["POST", "GET"])
def selfrolls():
    global name, choice, soclass
    name.char_abilities["STR"] = int(request.form['str'])
    name.char_abilities["INT"] = int(request.form['int'])
    name.char_abilities["WIS"] = int(request.form['wis'])
    name.char_abilities["DEX"] = int(request.form['dex'])
    name.char_abilities["CON"] = int(request.form['con'])
    name.char_abilities["CHA"] = int(request.form['cha'])
    name.char_abilities["CMS"] = int(request.form['cms'])
    soclass = int(request.form['social'])
    if name.char_abilities["STR"] < 18:
        exceptional_str = False
        name.char_abilities['EX_STR'] = False
    elif name.char_abilities["STR"] not in range(1, 101) and str(name.char_abilities) != "00":
        exceptional_str = False
        name.char_abilities['EX_STR'] = False
    else:
        name.char_abilities['EX_STR'] = int(request.form['ex_str'])

    name, valid = character_gui.selfrolls(choice, name)
    if int(soclass) not in range(1, 101) and str(soclass) != "00":
        valid = False
    elif name.char_abilities["STR"] not in range(1, 101) and str(name.char_abilities) != "00":
        valid = False
    if not valid:
        #return "Illegal Character rolls, try again."
        return '''
               <html>
                    <head>
                        <title>1st Edition AD&D Character Generator 1985</title>
                    </head>
                    <style>
                            hlR {
                                color: red;
                                }
                            hlG {
                                color: green;
                                }
                            hlB {
                                color: blue;
                                }
                            body {
                                background-color:#c2adeb;
                                }
                            fixed {
                                font-family: "Courier New", Monospace, monospace;
                                }
                            table, th, td {
                                border: 1px solid black;
                                border-collapse: collapse;
                                }
                            th, td {
                              padding: 5px;
                              text-align: left;
                              font-weight: bold;
                                    }
                    </style>
                    <body>
                        <h1>1st Edition AD&D Character Generator 1985 Edition</h1>
                        <form action="/" method="POST">
                            <p>
                                    Illegal Character rolls, try again.
                            </p>
                            <p><input type="submit" value="Next"></p>
                            <br>
                        </form>
                    </body>
                </html>
                '''
    else:
        #return str(name.char_abilities["STR"])
        return render_template('base_abilities.html',
                               STR=name.char_abilities["STR"],
                               INT=name.char_abilities["INT"],
                               WIS=name.char_abilities["WIS"],
                               DEX=name.char_abilities["DEX"],
                               CON=name.char_abilities["CON"],
                               CHA=name.char_abilities["CHA"],
                               CMS=name.char_abilities["CMS"])


@app.route("/methodv_chosen", methods=["POST", "GET"])
def methodv_chosen():
    global name, abilities, choice, methodv_choice, methodv
    choice = request.form['choices']
    print("140")
    abilities, choice = dice_gui.unearthed(choice)
    name.methodv = True
    name.methodv_choice = True
    methodv = True
    methodv_choice = True
    print("146", name.methodv)
    return render_template('base_abilities.html',
                           STR=name.char_abilities["STR"],
                           INT=name.char_abilities["INT"],
                           WIS=name.char_abilities["WIS"],
                           DEX=name.char_abilities["DEX"],
                           CON=name.char_abilities["CON"],
                           CHA=name.char_abilities["CHA"],
                           CMS=name.char_abilities["CMS"])


@app.route("/social_class", methods=["POST", "GET"])
def social_class():
    global name, choice, soclass, soclassdef
    if not soclass:
        choice = str(request.form['choices'])
    name = social_class_gui.social_class(name, choice, soclass)
    soclassdef = social_class_gui.soclass_definition[name.social_class]
    return render_template('base_abilities_2_soclass.html',
                           STR=name.char_abilities["STR"],
                           INT=name.char_abilities["INT"],
                           WIS=name.char_abilities["WIS"],
                           DEX=name.char_abilities["DEX"],
                           CON=name.char_abilities["CON"],
                           CHA=name.char_abilities["CHA"],
                           CMS=name.char_abilities["CMS"],
                           SOCIALCLASS=name.social_class,
                           SOCIALCLASSDEF=soclassdef
                           )


@app.route("/roll_soclass_choice", methods=["POST", "GET"])
def soclass_choice():
    global name, choice, soclass
    return render_template("/roll_soclass_choice.html")


@app.route("/choose_race", methods=["POST", "GET"])
def choose_race():
    global name, choice
    gender = request.form['choices']
    name, class_limit = char_races_gui.check_display_mins(name, gender)
    name.char_gender = gender
    print(name.methodv, "181")
    #class_limit = str(class_limit)
    if not name.methodv:
        return render_template("show_race_choices.html", class_limit=class_limit)
    else:
        name.char_race = "Human"
        #choose_class()
        return redirect(url_for('choose_class'))

@app.route("/race_chosen_choose_class", methods=["POST", "GET"])
def race_chosen():
    global retry
    global name
    global result
    global info
    global classes
    global soclassdef
    ninfo = ""
    if not retry:
        name.char_race = request.form['choices']
    #return name.char_race
    if not retry:
        name.char_class = []
        classes, name = char_classes_gui.race_classes(name)
    if len(info) > 0:
        ninfo = info
    if len(classes) > 0 and len(ninfo) > 0:
        return render_template('show_class_choices.html', classes=classes, info=ninfo,
                               STR=name.char_abilities["STR"],
                               INT=name.char_abilities["INT"],
                               WIS=name.char_abilities["WIS"],
                               DEX=name.char_abilities["DEX"],
                               CON=name.char_abilities["CON"],
                               CHA=name.char_abilities["CHA"],
                               CMS=name.char_abilities["CMS"],
                               SOCIALCLASS=name.social_class,
                               SOCIALCLASSDEF=soclassdef
                               )
    elif retry:
        return render_template('show_class_choices.html', classes=classes, info=ninfo,
                               STR=name.char_abilities["STR"],
                               INT=name.char_abilities["INT"],
                               WIS=name.char_abilities["WIS"],
                               DEX=name.char_abilities["DEX"],
                               CON=name.char_abilities["CON"],
                               CHA=name.char_abilities["CHA"],
                               CMS=name.char_abilities["CMS"],
                               SOCIALCLASS=name.social_class,
                               SOCIALCLASSDEF=soclassdef
                               )
    elif len(classes) > 0:
        return render_template('show_class_choices.html', classes=classes, info=ninfo,
                               STR=name.char_abilities["STR"],
                               INT=name.char_abilities["INT"],
                               WIS=name.char_abilities["WIS"],
                               DEX=name.char_abilities["DEX"],
                               CON=name.char_abilities["CON"],
                               CHA=name.char_abilities["CHA"],
                               CMS=name.char_abilities["CMS"],
                               SOCIALCLASS=name.social_class,
                               SOCIALCLASSDEF=soclassdef
                               )
    else:
        classes = ["None"]
        return render_template('show_class_choices.html', classes=classes, info=ninfo,
                               STR=name.char_abilities["STR"],
                               INT=name.char_abilities["INT"],
                               WIS=name.char_abilities["WIS"],
                               DEX=name.char_abilities["DEX"],
                               CON=name.char_abilities["CON"],
                               CHA=name.char_abilities["CHA"],
                               CMS=name.char_abilities["CMS"],
                               SOCIALCLASS=name.social_class,
                               SOCIALCLASSDEF=soclassdef
                               )

@app.route("/class_chosen", methods=["POST", "GET"])
def choose_class():
    global name, choice, info, retry
    print(choice, name.methodv, "CHOICES")

    if name.methodv:
        print(name.methodv, "methodv")
        print(name.char_race, "race")
        choice = name.char_race
    else:
        choice = request.form["choices"]
        print(choice, "???/")

    name, result = char_classes_gui.choose_classes(name, choice)
    print(result, "result? line 247")
    if not result:
        info = "This choice isn't valid, rolls are too low, try again."
        print(info)
        retry = True
        return redirect(url_for('race_chosen'))
    else:
        return '''
               <html>
                    <head>
                        <title>1st Edition AD&D Character Generator 1985</title>
                    </head>
                    <style>
                            hlR {
                                color: red;
                                }
                            hlG {
                                color: green;
                                }
                            hlB {
                                color: blue;
                                }
                            body {
                                background-color:#c2adeb;
                                }
                            fixed {
                                font-family: "Courier New", Monospace, monospace;
                                }
                            table, th, td {
                                border: 1px solid black;
                                border-collapse: collapse;
                                }
                            th, td {
                              padding: 5px;
                              text-align: left;
                              font-weight: bold;
                                    }
                    </style>
                    <body>
                        <h1>1st Edition AD&D Character Generator 1985 Edition</h1>
                        <form action="/char_builder" method="POST">
                            <p><input type="submit" value="Yes"></p>
                            <br>
                        </form>
                        <form action="/race_chosen_choose_class" method="POST">
                            <p>
                                    This selection is valid, do you choose it?<br>
                                    If you chose Method V, any abilities below minimum, will be adjusted to class minimums.
                            </p>
                            <p><input type="submit" value="No"></p>
                            <br>
                        </form>
                    </body>
                </html>
                '''


@app.route("/char_builder", methods=["POST", "GET"])
def character_builder_1():
    global name
    name = character_gui.savingthrows(name)
    print(name.char_saves)
    name = character_gui.racebonuses(name)
    return render_template('/char_builder.html', name=name)
