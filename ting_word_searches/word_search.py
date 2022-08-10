def exists_word(word, instance):
    word_occurrences = list()
    for index, item in enumerate(instance._data[0]["linhas_do_arquivo"]):
        if word.lower() in item.lower():
            word_occurrences.append({"linha": index + 1})
    word_results = list()
    if word_occurrences:
        word_results = [
            {
                "palavra": word,
                "arquivo": instance._data[0]["nome_do_arquivo"],
                "ocorrencias": word_occurrences,
            }
        ]
    return word_results


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
