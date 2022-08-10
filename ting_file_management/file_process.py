from .file_management import txt_importer


def process(path_file, instance):
    data = txt_importer(path_file)
    content = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(data),
        "linhas_do_arquivo": data
    }
    if not len(instance):
        instance.enqueue(content)
        print(content)


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
