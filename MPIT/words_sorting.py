def sort_words(string):
    words_lst = string.split(sep=",")
    words_lst = sorted(words_lst, key=lambda x: x.lower())
    return ', '.join(words_lst)
