"""
The module contains a class that:

    1. Provides a list of the names of all valid Entrez databases

    2. Provides statistics for a single database, including lists of indexing fields and available link names

"""


class Info:
    """
    This class implements the EInfo utility wrapper

    """

    def __init__(self):
        self.url = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/einfo.fcgi'


if __name__ == '__main__':
    Info()
