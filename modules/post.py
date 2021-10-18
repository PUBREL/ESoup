"""
The module contains a class that

    1. Uploads a list of UIDs to the Entrez History server

    2. Appends a list of UIDs to an existing set of UID lists attached to a Web Environment

"""


class Post:
    """
    This class implements the EPost Wrapper

    """

    def __init__(self):
        self.url = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/epost.fcgi'


if __name__ == '__main__':
    Post()
