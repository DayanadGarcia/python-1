from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def ola_mundo():
	return render_template("index.html")

@app.route('/<string:nome>')
def error(nome):
  var = f'Página ({nome}) não existe!'
  return render_template("error.html", var = var)
