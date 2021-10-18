"""
The module contains a class that :

    1. Provides the number of records retrieved in all Entrez databases by a single text query.

"""


class GQuery:
    """
    The class implements the EGQuery utility wrapper

    """

    def __init__(self):
        self.url = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/egquery.fcgi'


if __name__ == '__main__':
    GQuery()

