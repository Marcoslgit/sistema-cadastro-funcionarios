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
        "\n Escolha uma opção: \n1 - cadastrar um funcionário \n2 - Mostrar lista de funcionários \n3 - Atualizar funcionário \n0 - sair \n"
    )

    if op == "1":
        nome = input("Qual o nome do funcionário? ")
        cargo = input("Qual o cargo do funcionário? ")
        salario = float(input("Qual o salário do funcionário? "))

        cursor.execute(
            """
            INSERT INTO funcionarios (nome, cargo, salario) VALUES (?, ?, ?)
            """,
            (nome, cargo, salario),
        )
        conexao.commit()

    elif op == "2":
        cursor.execute("SELECT * FROM funcionarios")
        funcionarios = cursor.fetchall()

        print("\n--- Funcionários cadastrados ---")
        print("Quantidade de funcionários:", len(funcionarios))

        for funcionario in funcionarios:
            salario = f"{funcionario[3]:,.2f}"
            salario = salario.replace(",", "X").replace(
                ".", ",").replace("X", ".")

            print(
                f"ID: {funcionario[0]} | "
                f"Nome: {funcionario[1]} | "
                f"Cargo: {funcionario[2]} | "
                f"Salário: R$ {salario}"
            )

    elif op == "3":
        id_func = int(
            input("Digite o ID do funcionário que deseja atualizar: "))

        cursor.execute(
            "SELECT * FROM funcionarios WHERE id = ?",
            (id_func,),
        )

        if cursor.fetchone() is None:
            print("Funcionário não encontrado.")
        else:
            nome = input("Qual o nome do novo funcionário? ")
            cargo = input("Qual o novo cargo do funcionário? ")
            salario = float(input("Qual o novo salário do funcionário? "))

            cursor.execute(
                """
                UPDATE funcionarios
                SET nome = ?, cargo = ?, salario = ?
                WHERE id = ?
                """,
                (nome, cargo, salario, id_func),
            )
            print("Funcionário atualizado com sucesso.")
            conexao.commit()

    elif op == "0":
        break

conexao.commit()
conexao.close()
