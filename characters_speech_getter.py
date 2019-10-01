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
            dir_ = os.path.join('characters_speech', play.name.split('-')[0], 'corpus')
            play_name = play.name.split('-')[1]
            with open(os.path.join(dir_,
                                   f'{character.gender}_{play_name}_{character.id_}.txt'),
                      'w', encoding='utf-8') as f:
                f.write(' '.join(character.spoken_text))        
