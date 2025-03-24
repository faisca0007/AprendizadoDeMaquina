import random
import pandas as pd

def main():
    # Passo 1: Criar a lista de frutas com repetições
    frutas = ["maçã", "banana", "laranja", "uva", "maçã", "melão", "mamão", "banana"]
    
    print("Lista original de frutas:")
    print(frutas)
    print("\n")
    
    # Passo 2: Criar lista para armazenar frutas e quantidades
    frutas_quantidade = []
    
    # Passo 3: Gerar quantidades aleatórias para cada fruta da lista
    for fruta in frutas:
        quantidade = random.randint(0, 100)  # Quantidade aleatória entre 0 e 100
        frutas_quantidade.append((fruta, quantidade))
    
    print("Lista de frutas com quantidades geradas:")
    for item in frutas_quantidade:
        print(f"{item[0]}: {item[1]}")
    print("\n")
    
    # Passo 4: Gravar as frutas e quantidades no arquivo 'minhas_frutas.txt'
    with open('minhas_frutas.txt', 'w', encoding='utf-8') as file:
        for fruta, quantidade in frutas_quantidade:
            file.write(f"{fruta},{quantidade}\n")
    
    print("Arquivo 'minhas_frutas.txt' criado com sucesso!\n")
    
    # Passo 5: Ler o arquivo e somar as quantidades das frutas repetidas
    try:
        dados = pd.read_csv('minhas_frutas.txt', names=["Fruta", "Quantidade"])
        
        print("Dados lidos do arquivo:")
        print(dados)
        print("\n")
        
        # Agrupar por fruta e somar as quantidades
        dados_agrupados = dados.groupby('Fruta', as_index=False).sum()
        
        # Ordenar por quantidade (decrescente)
        dados_agrupados = dados_agrupados.sort_values('Quantidade', ascending=False)
        
        # Exibir o DataFrame resultante
        print("Quantidade total por fruta:")
        print(dados_agrupados)
        
        # Salvar resultados em um novo arquivo CSV
        dados_agrupados.to_csv('frutas_agrupadas.csv', index=False)
        print("\nResultados salvos em 'frutas_agrupadas.csv'")
        
    except FileNotFoundError:
        print("Erro: Arquivo 'minhas_frutas.txt' não encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    main()