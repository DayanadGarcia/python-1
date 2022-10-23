from flask import Flask, render_template, request
from random import randint

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
  var = "Game: adivinhe o número correto"

  if request.method == "GET":
    return render_template("index.html", var = var)
  else:
    numero = randint(1, 10)
    palpite = int(request.form.get("name"))
    if numero == palpite:
      return '<h1>Resultado: Você ganhou!!!!</h1>'
    else:
      return '<h1>Resultado: Você perdeu!!!!</h1>'


@app.route('/<string:nome>')
def error(nome):
  var = f'Página ({nome}) não existe!'
  return render_template("error.html", var = var)
