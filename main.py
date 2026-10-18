import sqlite3
conexao = sqlite3.connect("empresadb")
cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS funcionarios (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  nome TEXT NOT NULL,
  cargo TEXT NOT NULL,
  salario REAL NOT NULL
)
""")
while True:
    op = input(
        "\n Escolha uma opção: \n1 - cadastrar um funcionário \n2 - Mostrar lista de funcionários \n3 - sair \n")
    if op == "1":
        nome = input("Qual o nome do funcionário? ")
        cargo = input("Qual o cargo do funcionário? ")
        salario = float(input("Qual o salário do funcionário? "))

        cursor.execute("""
    INSERT INTO funcionarios (nome, cargo, salario) VALUES (?, ?, ?)
""", (nome, cargo, salario))

    

    elif op == "2":
          cursor.execute("SELECT * FROM funcionarios")
          funcionarios = cursor.fetchall()
          print("\n --- Funcionarios cadastrados ---")
          for funcionario in funcionarios:
                    print(funcionario)
          conexao.commit()
    elif op == "3":
        break



conexao.commit()


conexao.close()
