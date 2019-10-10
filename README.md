**Corpus**

This is a class describing and “containing” the whole drama corpus. An object of class initializes with just a single argument – name of a corpus such as `“ger”`, `“rus"` and others that are in DraCor.

There are property containing all the plays in the corpus. First time you use corpus.plays it can take a while to get all the content via requests to API, but after that it will be cached and you can access any play fast.

**Play**

An object of this class represents some play. It initializes with four required arguments: corpus it belongs to (Corpus class object), name in DraCor to make requests about this play, human readable title (actual title of the play, for example _'Пустая ссора'_) and author’s name; also, there are three optional arguments: years the play was written and staged and so called normalized year taking both previous into account (see DraCor documentation for more information) which are None if unknown. In fact, title and author could be optional arguments too, but in purposes of following data processing I’ve made it impossible to initialize play object with no these parameters.

As Corpus object “contains” all the plays, Play object “contains” all the characters. Once they would be got via API, they will be cached and then could be accessed fast.

**Character**

An object of Character class initializes with id in a play and human readable actual name as a required arguments and gender (None if unknown), number of words said in a play (default to 0 for characters which appear but say nothing) and all the phrases (default to empty list for the same case)
