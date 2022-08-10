import sys


def txt_importer(path_file):
    if ".txt" in path_file:
        try:
            with open(path_file) as file:
                return file.read().splitlines()
        except FileNotFoundError:
            print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
    else:
        print("Formato inválido", file=sys.stderr)
