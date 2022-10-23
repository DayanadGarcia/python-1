## Python API

#### Passos para criar uma API com flask

```python
#terminal
sudo apt-get install python3-venv
```

```python
#terminal
python3 -m venv env
```

```python
#terminal - ativar ambiente virtual
source env/bin/activate
```

```python
#terminal - desativar ambiente virtual
deactivate
```

```python
pip install flask
```

```python
#arquivo: meusite.py
from flask import Flask
app = Flask(__name__)

@app.route('/')
def ola_mundo():
	return 'Olá Mundo!'
```

```python
#para subir o servidor:
export FLASK_APP=meusite.py
.
.
.
flask run
```

```python
#para ativar o debug e atualizar com alterações. . .
export FLASK_ENV=development
```