# app.py

from flask import Flask  # Importa a biblioteca Flask

app = Flask(__name__)  # Cria o servidor

# Quando alguém acessar o site na página inicial (/), essa função é chamada
@app.route('/')
def home():
    return 'Olá! Bem-vindo ao meu primeiro servidor Flask 😄'

# Inicia o servidor
if __name__ == '__main__':
    app.run(debug=True)
