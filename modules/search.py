"""
The module contains a class that :

    1. Provides a list of UIDs matching a text query

    2. Posts the results of a search on the History server

    3. Downloads all UIDs from a dataset stored on the History server

    4. Combines or limits UID datasets stored on the History server

    5. Sorts sets of UIDs

"""


class Search:
    """
    This class implements a wrapper for the ESearch utility

    """

    def __init__(self):
        self.url = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi'


if __name__ == '__main__':
    Search()
