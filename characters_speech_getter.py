import os
import functools
import operator

from corpus import Corpus
from play import Play
from character import Character

from stage_directions_getter import plays_to_analyse


plays = functools.reduce(operator.concat, plays_to_analyse.values())
for play in plays:
    for character in play.characters:
        with open(os.path.join('characters_speech', 'corpus',
                               f'{character.gender}_{play.name}_{character.id_}.txt'),
                  'w', encoding='utf-8') as f:
            print(character.spoken_text, file=f)        
