import os

from corpus import Corpus
from play import Play


corpus = Corpus('rus')

centuries = {18: 'XVIII',
             19: 'XIX',
             20: 'XX'}

files = {i: f'{centuries[i // 100 + 1]}_{i-9}-{i}.txt'
         for i in range(1749, 1949, 10)}

for play in corpus.plays:
    for year, filename in files.items():
        if (play.normalized_year is not None) and (play.normalized_year <= year):
            with open(os.path.join('epochs', 'corpus', filename), 'a', encoding='utf-8') as f:
                f.write(play.stage_text)            
