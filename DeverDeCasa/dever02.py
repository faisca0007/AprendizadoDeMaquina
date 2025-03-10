def solicitar_entrada():
    """Solicita ao usuário que insira uma frase e verifica se a entrada não está vazia."""
    frase = input("Digite uma frase: ").strip()
    while not frase:
        print("A frase não pode estar vazia. Tente novamente.")
        frase = input("Digite uma frase: ").strip()
    return frase

def analisar_frase(frase):
    """Realiza a análise da frase e retorna as informações solicitadas."""
    # Contagem de caracteres (incluindo espaços)
    num_caracteres = len(frase)
    
    # Contagem de palavras
    palavras = frase.split()
    num_palavras = len(palavras)
    
    # Maior palavra
    maior_palavra = max(palavras, key=len) if palavras else ""
    
    return num_caracteres, num_palavras, maior_palavra, palavras

def manipular_frase(frase, palavras):
    """Realiza a manipulação e formatação da frase."""
    # Inversão da frase por caracteres
    frase_invertida_caracteres = frase[::-1]
    
    # Inversão da ordem das palavras
    frase_invertida_palavras = " ".join(palavras[::-1])
    
    # Frase em maiúsculas e minúsculas
    frase_maiusculas = frase.upper()
    frase_minusculas = frase.lower()
    
    # Tupla de palavras
    tupla_palavras = tuple(palavras)
    
    return frase_invertida_caracteres, frase_invertida_palavras, frase_maiusculas, frase_minusculas, tupla_palavras

def exibir_resultados(num_caracteres, num_palavras, maior_palavra, frase_invertida_caracteres, frase_invertida_palavras, frase_maiusculas, frase_minusculas, tupla_palavras):
    """Exibe os resultados de forma formatada."""
    print(f"\nResultado da Análise e Formatação da Frase:\n")
    print(f"Número de caracteres da frase: {num_caracteres}")
    print(f"Número de palavras na frase: {num_palavras}")
    print(f"A palavra com maior comprimento: {maior_palavra}")
    print(f"Frase invertida (por caracteres): {frase_invertida_caracteres}")
    print(f"Frase invertida (por palavras): {frase_invertida_palavras}")
    print(f"Frase em maiúsculas: {frase_maiusculas}")
    print(f"Frase em minúsculas: {frase_minusculas}")
    print(f"Tupla das palavras da frase: {tupla_palavras}")

def main():
    # Solicitar a entrada do usuário
    frase = solicitar_entrada()
    
    # Analisar a frase
    num_caracteres, num_palavras, maior_palavra, palavras = analisar_frase(frase)
    
    # Manipular e formatar a frase
    frase_invertida_caracteres, frase_invertida_palavras, frase_maiusculas, frase_minusculas, tupla_palavras = manipular_frase(frase, palavras)
    
    # Exibir os resultados
    exibir_resultados(num_caracteres, num_palavras, maior_palavra, frase_invertida_caracteres, frase_invertida_palavras, frase_maiusculas, frase_minusculas, tupla_palavras)

if __name__ == "__main__":
    main()
