import sqlite3
conexao = sqlite3.connect("empresadb")
cursor = conexao.cursor()

cursor.execute ("""
CREATE TABLE IF NOT EXISTS funcionarios (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  nome TEXT NOT NULL,
  cargo TEXT NOT NULL,
  salario REAL NOT NULL
)
""")

nome = input("Digite o nome do funcionário: ")
cargo = input("Digite o cargo do funcionário: ")
salario = float(input("Digite o salário do funcionario: "))

cursor.execute("""
INSERT INTO funcionarios (nome, cargo, salario) VALUES (?, ?, ?)
""", (nome, cargo, salario))

conexao.commit()
conexao.close()




