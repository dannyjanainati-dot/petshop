import os
import mysql.connector
from dotenv import load_dotenv

# Etapa 1: carregar as configurações do arquivo .env
# Isso permite usar dados de conexão sem escrever senhas diretamente no código.
load_dotenv()


# Etapa 2: criar a classe Pet para representar cada animal do sistema
# Ela organiza os dados do pet em um objeto mais fácil de manipular.
class Pet:
    def __init__(self, id, nome, raca, idade, nome_dono, especie_id):
        self.id = id
        self.nome = nome
        self.raca = raca
        self.idade = idade
        self.nome_dono = nome_dono
        self.especie_id = especie_id

    def __str__(self):
        # Formata os dados do pet para impressão na tela.
        return f"[{self.id}] {self.nome} ({self.raca}) — {self.idade} anos | Dono: {self.nome_dono}"


# Etapa 3: função para cadastrar um novo pet no banco de dados
# Aqui o usuário informa os dados e eles são salvos na tabela pets.
def cadastrar(conexao, cursor):
    print("\n--- Cadastrar novo pet ---")

    # Passo 1: coletar os dados básicos do pet.
    nome = input("Nome do pet: ")
    raca = input("Raça: ")
    idade = input("Idade (anos): ")
    nome_dono = input("Nome do dono: ")

    # Passo 2: mostrar as espécies disponíveis para o usuário escolher.
    print("\nEspécies disponíveis:")
    cursor.execute("SELECT id, nome FROM especies")
    for especie in cursor.fetchall():
        print(especie)  # Exemplo: (1, 'Cachorro')
    especie_id = input("Digite o id da espécie: ")

    # Passo 3: inserir os dados no banco com SQL seguro.
    cursor.execute(
        "INSERT INTO pets (nome, raca, idade, nome_dono, especie_id) VALUES (%s, %s, %s, %s, %s)",
        (nome, raca, idade, nome_dono, especie_id)
    )
    conexao.commit()
    print("Pet cadastrado com sucesso!")


# Etapa 4: função para buscar pets pelo nome
# Ela consulta o banco e exibe os resultados que combinam com a busca.
def buscar(cursor):
    print("\n--- Buscar pet por nome ---")
    nome = input("Digite o nome do pet: ")

    # SQL para encontrar pets cujo nome contenha o texto digitado.
    SELECT = "SELECT id, nome, raca, idade, nome_dono, especie_id FROM pets WHERE nome LIKE %s"
    cursor.execute(SELECT, (f"%{nome}%",))
    pets = cursor.fetchall()

    if pets:
        print("\n--- Pets encontrados ---")
        for pet_data in pets:
            pet = Pet(*pet_data)
            print(pet)
    else:
        print("Nenhum pet encontrado com esse nome.")


# Etapa 5: função para listar todos os pets cadastrados
# Serve para mostrar todos os registros salvos no banco.
def listar(cursor):
    print("\n--- Listar todos os pets ---")
    cursor.execute("SELECT id, nome, raca, idade, nome_dono, especie_id FROM pets")
    pets = cursor.fetchall()

    if pets:
        print("\n--- Todos os pets ---")
        for pet_data in pets:
            pet = Pet(*pet_data)
            print(pet)
    else:
        print("Nenhum pet cadastrado.")


# Etapa 6: menu principal do sistema
# Aqui o usuário escolhe entre cadastrar, buscar, listar ou sair.
def menu():
    conexao = None
    cursor = None
    try:
        # Passo 1: abrir a conexão com o banco de dados.
        conexao = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
        )
        cursor = conexao.cursor()

        # Passo 2: repetir o menu até o usuário decidir sair.
        while True:
            print("\n=== Sistema do Petshop ===")
            print("1. Cadastrar")
            print("2. Buscar")
            print("3. Listar todos")
            print("0. Sair")
            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                cadastrar(conexao, cursor)
            elif opcao == "2":
                buscar(cursor)
            elif opcao == "3":
                listar(cursor)
            elif opcao == "0":
                print("Encerrando...")
                break
            else:
                print("Opção inválida. Tente de novo.")

    except mysql.connector.Error as erro:
        # Caso ocorra algum problema na conexão, mostra a mensagem do erro.
        print("Erro ao acessar o banco de dados:", erro)
    finally:
        # Passo 3: fechar o cursor e a conexão ao terminar.
        if cursor is not None:
            cursor.close()
        if conexao is not None and conexao.is_connected():
            conexao.close()


# Etapa 7: iniciar o programa.
menu()
