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
        if character.num_of_words > 3:
            with open(os.path.join('characters_speech', 'corpus',
                                   f'{character.gender}_{play.name}_{character.id_}.txt'),
                      'w', encoding='utf-8') as f:
                f.write(' '.join(character.spoken_text))        
