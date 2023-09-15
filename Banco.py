#importando SQLite
import sqlite3 as lite

# criando conexao
con = lite.connect('dados.db')

# criando tabela
with con:
    cur=con.cursor()
    cur.execute("CREATE TABLE formulario(id INTEGER PRIMARY KEY AUTOINCREMENT,Nome TEXT, Email TEXT,Telefone TEXT,Dia_em DATE,Estado TEXT,ASSUNTO TEXT)")

    