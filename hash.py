import hashlib

def gerar_hash(codigo, algoritmo='sha256'):
    """
    Gera um hash para o código fornecido usando o algoritmo especificado.
    
    :param codigo: O texto ou código que será convertido em hash.
    :param algoritmo: O algoritmo de hash a ser utilizado ('md5', 'sha1', 'sha256', etc.).
    :return: O hash do código em formato hexadecimal.
    """
    # Cria um objeto hash baseado no algoritmo especificado
    hash_obj = hashlib.new(algoritmo)
    
    # Atualiza o objeto hash com o código em bytes
    hash_obj.update(codigo.encode('utf-8'))
    
    # Retorna o hash em formato hexadecimal
    return hash_obj.hexdigest()

def main():
    # Solicita o código ou texto do usuário
    codigo = input("Digite o código ou texto a ser criptografado em hash: ")
    
    # Solicita o algoritmo de hash do usuário
    algoritmos_disponiveis = ['md5', 'sha1', 'sha256', 'sha512']
    print("Algoritmos disponíveis:", ', '.join(algoritmos_disponiveis))
    algoritmo = input(f"Escolha o algoritmo de hash ({', '.join(algoritmos_disponiveis)}): ").lower()
    
    # Verifica se o algoritmo escolhido é válido
    if algoritmo not in algoritmos_disponiveis:
        print("Algoritmo inválido. Usando 'sha256' por padrão.")
        algoritmo = 'sha256'
    
    # Gera e exibe o hash
    hash_gerado = gerar_hash(codigo, algoritmo)
    print(f'O hash gerado com o algoritmo {algoritmo} é: {hash_gerado}')

if __name__ == "__main__":
    main()