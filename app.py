from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def extrañar():
    mensaje = (
        "Te extraño, aunque nunca fuiste mío del todo. "
        "Fuiste ese 'casi' que dolió como si hubiera sido un 'todo'. "
        "No fuiste un amor, pero fuiste algo. "
        "Y ese algo todavía me duele como si hubieras sido todo."
    )
    return render_template("extrañar.html", mensaje=mensaje)

@app.route('/si')
def si():
    return render_template("si.html")

@app.route('/no')
def no():
    return render_template("no.html")

if __name__ == '__main__':
    app.run(debug=True)
