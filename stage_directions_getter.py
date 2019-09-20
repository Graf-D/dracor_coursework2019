import os

from corpus import Corpus
from play import Play
from character import Character


ruscor = Corpus('rus')

plays_to_analyse = {'Булгаков, Михаил Афанасьевич': [],
                    'Гумилёв, Николай Степанович': [],
                    'Прутков, Козьма': [],
                    'Тургенев, Иван Сергеевич': [],
                    'Чехов, Антон Павлович': []}

for play in ruscor.plays:
    if play.author in plays_to_analyse.keys():
        plays_to_analyse[play.author].append(play)

for author, plays in plays_to_analyse.items():
    for play in plays:
        with open(os.path.join('stage_texts', 'corpus', play.name.replace('-', '_') + '.txt'), 'w', encoding='utf-8') as f:
            f.write(play.stage_text)
