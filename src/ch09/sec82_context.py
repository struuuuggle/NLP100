# -*- coding: utf-8 -*-
from random import randint

CORPUS_PATH = "./sec81_corpus.txt"
OUTPUT_PATH = "./sec82_context.txt"

if __name__ == '__main__':
    # vocab = defaultdict(lambda: len(vocab))
    with open(CORPUS_PATH) as f:
        words = f.read().rstrip().split(' ')

    # with open(OUTPUT_PATH, 'w') as f:
    #     for i, t in tqdm(enumerate(words)):
    #         vocab[t]
    #         d = randint(1, 5)
    #         for j in range(1, d + 1):
    #             if i+j < len(words) and t != "" and words[i+j] != "":
    #                 f.write(f'{t}\t{words[i+j]}\n')
    #             if i-j >= 0 and t != "" and words[i-j] != "":
    #                 f.write(f'{t}\t{words[i-j]}\n')

    # joblib.dump(dict(vocab), 'vocab.joblib')

    with open(OUTPUT_PATH, 'w') as f:
        for i, _ in enumerate(words):
            d = randint(1, 5)
            start = max(i - d, 0)
            end = min(i + d + 1, len(words))
            for j in range(start, end):
                if i != j:
                    print(f'{words[i]}\t{words[j]}', file=f)
