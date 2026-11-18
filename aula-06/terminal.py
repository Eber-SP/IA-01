import sqlite3

DB_PATH = "_bancoDeDados\estoque\estoque.db"

nomeUsuario = input("Digite o seu nome: ")
promptDoUsuario = input("Digite a sua consulta SQL: ")

print(f"Olá {nomeUsuario}. A sua consulta foi: {promptDoUsuario}!")

if not promptDoUsuario.upper().startswith("SELECT"):
    print("Por segurança, apenas consultas SELECT são permitidas.")
else:
    try:
        with sqlite3.connect(DB_PATH) as conn:
            conn.row_factory = sqlite3.Row
            cur = conn.cursor()
            cur.execute(promptDoUsuario)
            resultado = [dict(linha) for linha in cur.fetchall()]

            for item in resultado:
                print(item)

    except sqlite3.Error as erro:
        print(f"Erro ao executar SQL: {erro}")
