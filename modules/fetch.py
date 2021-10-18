"""
The module contains a class that:

    1. Returns formatted data records for a list of input UIDs

    2. Returns formatted data records for a set of UIDs stored on the Entrez History server

"""


class Fetch:
    """
    The class implements the EFetch utility wrapper

    """
    def __init__(self):
        self.url = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi'


if __name__ == '__main__':
    Fetch()
