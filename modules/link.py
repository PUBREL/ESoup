"""
The module contains a class that:

    1. Returns UIDs linked to an input set of UIDs in either the same or a different Entrez database

    2. Returns UIDs linked to other UIDs in the same Entrez database that match an Entrez query

    3. Checks for the existence of Entrez links for a set of UIDs within the same database

    4. Lists the available links for a UID

    5. Lists LinkOut URLs and attributes for a set of UIDs

    6. Lists hyperlinks to primary LinkOut providers for a set of UIDs

    7. Creates hyperlinks to the primary LinkOut provider for a single UID

"""


class Link:
    """
    The class implements the ELink Entrez utility wrapper

    """
    def __init__(self):
        self.url = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/elink.fcgi'


if __name__ == '__main__':
    Link()
