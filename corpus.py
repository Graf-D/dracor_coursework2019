import requests
from functools import lru_cache
from play import Play


class WrongNameError(Exception):
    """
    An exception raised if there is no corpus in DraCor with the name,
    set as the name attribute for Corpus (check Corpus class documentation)
    """

class Corpus:
    """
    A class used to represent a whole drama corpus
    
    Attributes
    ----------
    name : str
        Should be 'ger' for German one, 'greek' for Greek, 'rom' for Roman,
        'rus' for Russian, 'shake' for Shakespeare and 'span' for Spanish.
    """

    BASE_URL = 'https://dracor.org/api/corpora'

    def __init__(self, name):
        if name.lower() in ['ger', 'greek', 'rom', 'rus', 'shake', 'span']:
            self.name = name.lower()
        else:
            raise WrongNameError(f'There is no such corpus with the name {name.lower()}')

    @property
    def url(self):
        """
        A corpus' URL for API requests. For example,
        https://dracor.org/api/corpora/rus for 'rus' name attribute value.
        """
        return f'{self.BASE_URL}/{self.name}'

    @property
    @lru_cache()
    def plays(self):
        """
        All plays (see Play class documentation) in a corpus.
        """
        corpus_content = requests.get(self.url).json()

        plays = []
        for drama in corpus_content['dramas']:
            printed_year = drama['printYear'] and int(drama['printYear'])
            written_year = drama['writtenYear'] and int(drama['writtenYear'])
            normalized_year = drama['yearNormalized'] and int(drama['yearNormalized'])
    
            plays.append(Play(self, drama['name'], drama['title'], drama['author']['name'],
                              printed_year, written_year, normalized_year))

        return plays
