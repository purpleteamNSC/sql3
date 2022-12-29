import sqlite3

conexao = sqlite3.connect('basededados.db')
cursor = conexao.cursor()

#cursor.execute('CREATE TABLE IF NOT EXISTS clientes('
#                'id INTEGER PRIMARY KEY AUTOINCREMENT,'
#                'nome TEXT,'
#                'peso REAL'
#                ')')

#cursor.execute('INSERT INTO clientes(nome, peso) VALUES (?, ?)',('Maria', 50))
#cursor.execute('INSERT INTO clientes(nome, peso) VALUES (:nome, :peso)',{'nome':'Joaozinho','peso': 25})
#cursor.execute('INSERT INTO clientes VALUES (:id, :nome, :peso)',{'id': None,'nome':'Daniel','peso': 113})
#conexao.commit()

cursor.execute('UPDATE clientes SET nome=:nome WHERE id=:id',{'nome':'Joana','id':2})
conexao.commit()


cursor.execute('SELECT * FROM clientes')

for linha in cursor.fetchall():
    print(linha)

cursor.close()
conexao.close()