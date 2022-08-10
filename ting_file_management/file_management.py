import sys


def txt_importer(path_file):
    if ".txt" in path_file:
        try:
            with open(path_file) as file:
                return file.read().splitlines()
        except FileNotFoundError:
            sys.stderr.write(f"Arquivo {path_file} não encontrado\n")
    else:
        sys.stderr.write("Formato inválido\n")
