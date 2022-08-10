def word_occurrence(word, instance, complete=False):
    word_occurrences = list()
    for index, item in enumerate(instance._data[0]["linhas_do_arquivo"]):
        if word.lower() in item.lower():
            if complete:
                word_occurrences.append({"linha": index + 1, "conteudo": item})
            else:
                word_occurrences.append({"linha": index + 1})
    word_results = list()
    word_results = [
        {
            "palavra": word,
            "arquivo": instance._data[0]["nome_do_arquivo"],
            "ocorrencias": word_occurrences,
        }
    ]
    return word_results if word_occurrences else []


def exists_word(word, instance):
    return word_occurrence(word, instance)


def search_by_word(word, instance):
    return word_occurrence(word, instance, True)
