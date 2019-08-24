class Character:
    """
    A class used to represent a play
    
    Attributes
    ----------
    id_ : str
       A character's DraCor play ID used for API requests.
    
    name : str
       A character's name.
    
    gender : str
       A character's gender. Default to None.
    
    num_of_words : int
       A number of words character said in the play. Default to 0.
    
    spoken_text : list
       All character's phrases. Default to empty list.
    """

    def __init__(self, id_, name, gender=None, num_of_words=0, spoken_text=[]):
        self.id_ = id_
        self.name = name
        self.gender = gender
        self.spoken_text = spoken_text
        self.num_of_words = num_of_words
