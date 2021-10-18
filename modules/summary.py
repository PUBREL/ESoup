"""
The module contains a class that:

    1. Returns document summaries (DocSums) for a list of input UIDs

    2. Returns DocSums for a set of UIDs stored on the Entrez History server

"""


class Summary:
    """
    The class implements the wrapper for the ESummary utility

    """

    def __init__(self):
        self.url = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi'


if __name__ == '__main__':
    Summary()
