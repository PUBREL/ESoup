"""
The module contains a class that :

    1. Provides a list of UIDs matching a text query

    2. Posts the results of a search on the History server

    3. Downloads all UIDs from a dataset stored on the History server

    4. Combines or limits UID datasets stored on the History server

    5. Sorts sets of UIDs

"""
import logging
import requests
import json
from utils.utils import Utils


class Search:
    """
    This class implements a wrapper for the ESearch utility

    """

    def __init__(self):
        """
        Declare an Entrez esearch endpoint url

        """

        self.url = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi'

        """
        Instantiate the Utils class to set global logging configurations
        
        Pass in a log_file argument in the logger function if you want the logs 
        to be saved on a file
        
        """
        Utils().logger()

    def search(self, term, db="pubmed", api_key=None,
               rettype="uilist", retmode='json',
               retstart=None, retmax=None, sort=None,
               field=None, idtype=None, datetype=None,
               reldate=None, mindate=None, maxdate=None,
               webenv=None, usehistory='y'):
        """
        The function is responsible for sending requests to NCBI


        :param api_key:


        :param db: Database to search. Value must be a valid Entrez database name
            See ../utils/utils.py module for available databases
            (default = pubmed).


        :param term: Entrez text query


        :param rettype: Retrieval type. There are two allowed values for ESearch: 'uilist' (default),
            which displays the standard XML output, and 'count', which displays only the <Count> tag.


        :param retmode: Retrieval type. Determines the format of the returned output.
            The default value is ‘xml’ for ESearch XML, but ‘json’ is also supported to return output in JSON format.


        :param retstart: Sequential index of the first UID in the retrieved set to be shown in the XML output
            (default=0, corresponding to the first record of the entire set).
            This parameter can be used in conjunction with retmax to download an arbitrary subset of UIDs
            retrieved from a search.


        :param retmax: Total number of UIDs from the retrieved set to be shown in the XML output (default=20).
            By default, ESearch only includes the first 20 UIDs retrieved in the XML output.
            If usehistory is set to 'y', the remainder of the retrieved set will be stored on the History server;
             otherwise these UIDs are lost. Increasing retmax allows more of the retrieved UIDs to be
             included in the XML output, up to a maximum of 100,000 records. To retrieve more than 100,000 UIDs,
             submit multiple esearch requests while incrementing the value of retstart


        :param sort: Specifies the method used to sort UIDs in the ESearch output.
            The available values vary by database (db) and may be found in the Display Settings menu on an
            Entrez search results page. If usehistory is set to ‘y’, the UIDs are loaded onto the History Server in the
            specified sort order and will be retrieved in that order by ESummary or EFetch.
            Example values are ‘relevance’ and ‘name’ for Gene and ‘first+author’ and ‘pub+date’ for PubMed.
            Users should be aware that the default value of sort varies from one database to another, and that the
            default value used by ESearch for a given database may differ from that used on NCBI web search pages.


        :param field: Search field. If used, the entire search term will be limited to the specified Entrez field.


        :param idtype: Specifies the type of identifier to return for sequence databases
            (nuccore, nucest, nucgss, popset, protein). By default, ESearch returns GI numbers in its output.
            If idtype is set to ‘acc’, ESearch will return accession.version identifiers rather than GI numbers.


        :param datetype: Type of date used to limit a search. The allowed values vary between Entrez databases,
            but common values are 'mdat' (modification date), 'pdat' (publication date) and 'edat' (Entrez date).
            Generally an Entrez database will have only two allowed values for datetype.


        :param reldate: When reldate is set to an integer n, the search returns only those items that have a date
            specified by datetype within the last n days.


        :param (maxdate, maxdate): Date range used to limit a search result by the date specified by datetype.
            These two parameters (mindate, maxdate) must be used together to specify an arbitrary date range.
            The general date format is YYYY/MM/DD, and these variants are also allowed: YYYY, YYYY/MM


        :param webenv: Web environment string returned from a previous ESearch, EPost or ELink call. When provided,
            ESearch will post the results of the search operation to this pre-existing WebEnv, thereby appending the
            results to the existing environment. In addition, providing WebEnv allows query keys to be used in term so
            that previous search sets can be combined or limited. As described above, if WebEnv is used,
             usehistory must be set to 'y'.


        :param usehistory: When usehistory is set to 'y', ESearch will post the UIDs resulting from the search operation
            onto the History server so that they can be used directly in a subsequent E-utility call.
            Also, usehistory must be set to 'y' for ESearch to interpret query key values included in term
            or to accept a WebEnv as input.

        """

        # assemble the arguments in a single variable for ease of use in the requests parameters
        parameters = {
            "api_key": api_key, "db": db, 'term': term,
            "rettype": rettype, "retmode": retmode, "retstart": retstart,
            "retmax": retmax, "sort": sort, "field": field, "idtype": idtype,
            "datetype": datetype, "reldate": reldate, "maxdate": maxdate, "mindate": mindate,
            "webenv": webenv, "usehistory": usehistory
        }

        try:
            """
            Send a POST request to the entrez endpoint url;
            
            Note that a GET request can still be used but a POST request is preferred 
            
            """
            handles = requests.post(url=self.url, data=parameters)

        except Exception as e:
            """
            Handle any exceptions and errors here; 
            
            Log the error and raise an Exception 
            
            """
            logging.error(e)
            raise e

        """
        Json parse the handles here and convert them into a valid json format
        
        """
        results = json.loads(handles.text)

        return results


if __name__ == '__main__':
    Search()
