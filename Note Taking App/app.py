#step 1 -import flask
from flask import Flask, render_template, request


#step 2-create object with a parameter __name__
app = Flask(__name__)

notes = []
#step-3 create an endpoint using route and bind them with functionality
@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        note = request.form.get("note")
        if note:
            notes.append(note)
        elif request.form.get("remove"):
            notes.pop()
        elif request.form.get("clear"):
            notes.clear()
    return render_template("home.html", notes=notes)

#step_4 run the app
if __name__ == '__main__':
    app.run(debug=True)
