"""
The file contains a class that:

    1. Provides spelling suggestions for terms within a single text query in a given database.

"""


class Spell:
    """
    This class implements the ESpell Utility wrapper

    """
    def __init__(self):
        self.url = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/espell.fcgi'


if __name__ == '__main__':
    Spell()
