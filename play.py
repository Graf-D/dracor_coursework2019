import requests
from functools import lru_cache

from character import Character


class Play:
    """
    A class used to represent a play
    
    Attributes
    ----------
    corpus : Corpus
        A corpus, to which the play belongs. See the Corpus class documentation.
    
    id_ : str
       A play's DraCor ID used for API requests.
    
    title : str
       A play's title.
    
    author : str
       A play's author.
    
    printed_year : int
       A year the play was printed for a first time. None if unknown.
    
    written_year : int
       A year the play was written. None if unknown.
    """

    def __init__(self, corpus, name, title, author,
                 printed_year=None, written_year=None, normalized_year=None):
        self.corpus = corpus
        self.name = name
        self.title = title
        self.author = author
        self.printed_year = printed_year
        self.written_year = written_year
        self.normalized_year = normalized_year

    @property
    def url(self):
        """
        A play's URL for API requests.
        """
        return f'{self.corpus.url}/play/{self.name}'

    @property
    @lru_cache()
    def characters(self):
        """
        All characters (see Character class documentation) in the play.
        """

        temp = {}
        cast_url = f'{self.url}/cast'
        cast = requests.get(cast_url).json()
        for elem in cast:
            temp[elem['id']] = Character(elem['id'], elem['name'],
                                               elem['gender'], int(elem['numOfWords']))

        spoken_text_url = f'{self.url}/spoken-text-by-character'
        all_spoken_text = requests.get(spoken_text_url).json()
        for text in all_spoken_text:
            temp[text['id']].spoken_text = text['text']
        
        characters = []
        for id_, character in temp.items():
            characters.append(character)

        return characters

    @property
    @lru_cache()
    def stage_text(self):
        """
        All stage directions given in the play.
        """
        stage_url = f'{self.url}/stage-directions'
        return requests.get(stage_url).text
