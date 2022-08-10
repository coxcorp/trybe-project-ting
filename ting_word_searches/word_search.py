def word_occurrence(word, instance, content=None):
    word = word.lower()
    word_occurrences = list()
    for index, item in enumerate(instance._data[0]["linhas_do_arquivo"]):
        if word in item.lower():
            if content == "line":
                word_occurrences.append({"linha": index + 1})
            else:
                word_occurrences.append({"linha": index + 1, "conteudo": item})
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


def exists_word(word, instance):
    return word_occurrence(word, instance, "line")


def search_by_word(word, instance):
    return word_occurrence(word, instance)
