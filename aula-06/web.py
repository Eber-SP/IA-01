import sqlite3
from flask import Flask, request

app = Flask(__name__)

DB_PATH = "_bancoDeDados\estoque\estoque.db"

@app.route("/api/ola", methods=['POST'])
def rota_ola():
    dados = request.get_json()
    nome = dados.get("nome", "")
    local = dados.get("endereco", "")
    return f"Olá {nome}, vc mora em {local}"

@app.route("/api/chat") # EXERCÍCIO 1
def rota_chat():
    return "Seu nome é NOME, e seu prompt é: PROMPT"

@app.route("/api/consulta") # EXERCÍCIO 2
def rota_consulta():
    return "SELECT * FROM TABELA"

@app.route("/api/ollama") # EXERCÍCIO 3
def rota_ollama():
    return "RESPOSTA DO OLLAMA"

if (__name__) == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)