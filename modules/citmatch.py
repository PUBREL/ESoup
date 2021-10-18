"""
The module contains a class that:

    1. Retrieves PubMed IDs (PMIDs) that correspond to a set of input citation strings.

"""


class CitMatch:
    """
    The class implements the ECitMatch Entrez utility wrapper

    """

    def __init__(self):
        self.url = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/ecitmatch.cgi'


if __name__ == '__main__':
    CitMatch()
