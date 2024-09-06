import hashlib

def hash_file(filename, hash_algorithm='sha256'):
    """Gera um hash de um arquivo usando o algoritmo especificado."""
    hash_func = getattr(hashlib, hash_algorithm)()
    with open(filename, 'rb') as file:
        for chunk in iter(lambda: file.read(4096), b""):
            hash_func.update(chunk)
    return hash_func.hexdigest()

# Nome do arquivo a ser transformado em hash
filename = 'texto.txt'
hash_value = hash_file(filename)
print(f'O hash SHA-256 do arquivo {filename} é: {hash_value}')