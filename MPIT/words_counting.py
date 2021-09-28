import re
from collections import Counter


def count_words(path):
    with open(path, mode='r', encoding='utf-8') as text:
        all_words = re.findall(r"[0-9a-zA-Z-']+", text.read())
        all_words = [word.upper() for word in all_words]
        print('\nTotal Words:', len(all_words))

        word_counts = Counter()
        for word in all_words:
            word_counts[word] += 1

        print('\nTOP 20 Words:')
        for word in word_counts.most_common(20):
            if len(word[0]) <= 3:
                print('{}\t\t{}'.format(word[0], word[1]))
            else:
                print('{}\t{}'.format(word[0], word[1]))


count_words('shakespeare.txt')
