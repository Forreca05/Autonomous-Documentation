import os

def read_file(filepath: str) -> str:
    """Lê todo o conteúdo do ficheiro e devolve como string."""
    if not os.path.isfile(filepath):
        raise FileNotFoundError(f"O ficheiro {filepath} não existe.")
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

def write_file(filepath: str, content: str) -> None:
    """Escreve o conteúdo no ficheiro, substituindo se já existir."""
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

