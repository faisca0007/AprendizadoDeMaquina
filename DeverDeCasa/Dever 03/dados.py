import csv

# Dados que serão gravados no arquivo CSV
dados = [
    ["Nome", "Idade"],  # Cabeçalho do CSV
    ["Ana", 25],
    ["Bruno", 30],
    ["Carla", 22],
    ["Daniel", 28],
    ["Eduardo", 35]
]

# Criando o arquivo dados.csv
with open("dados.csv", mode="w", newline="") as arquivo:
    writer = csv.writer(arquivo)  # Cria um escritor para o arquivo CSV
    writer.writerows(dados)  # Escreve todas as linhas no arquivo

print("Arquivo 'dados.csv' criado com sucesso!")

import csv

# Lendo o arquivo dados.csv e armazenando os dados em uma lista
dados_lista = []
with open("dados.csv", mode="r") as arquivo:
    reader = csv.reader(arquivo)  # Lê o arquivo CSV
    next(reader)  # Pula o cabeçalho
    for linha in reader:  # Para cada linha no arquivo (exceto o cabeçalho)
        dados_lista.append({"Nome": linha[0], "Idade": int(linha[1])})

# Função para verificar se o nome digitado está na lista
def verificar_nome(nome_digitado):
    pessoa_encontrada = None
    for pessoa in dados_lista:
        if pessoa["Nome"].lower() == nome_digitado.lower():
            pessoa_encontrada = pessoa
            break
    
    return pessoa_encontrada

# Pedir ao usuário para digitar um nome
nome_usuario = input("Digite um nome: ")

# Verificando se o nome digitado está na lista
pessoa = verificar_nome(nome_usuario)

if pessoa:
    # Encontrando a pessoa mais velha na lista
    pessoa_mais_velha = max(dados_lista, key=lambda x: x["Idade"])

    # Verificando se a pessoa é a mais velha
    if pessoa["Nome"] == pessoa_mais_velha["Nome"]:
        print(f"{pessoa['Nome']} tem {pessoa['Idade']} anos, é a pessoa mais velha da lista.")
    else:
        print(f"{pessoa['Nome']} tem {pessoa['Idade']} anos, não é a pessoa mais velha da lista.")
else:
    print("Nome não encontrado.")
