"""
The module contains a utility functions

"""
import logging


class Utils:
    """
    The class contains the helper utility functions

    """
    def __init__(self):
        self.logger()

    @staticmethod
    def logger(log_file=None):
        """
        :param log_file: Not a necessary argument but when provided, the resulting log
            is written to a log file with the name provided;

        Declare default logging global configuration;

        Can allow for custom log file to be created;

        """
        logging.basicConfig(
            level=logging.INFO,
            filename='search.log' if log_file else None,
            format='%(asctime)s %(levelname)s %(message)s',
        )

        return

    @staticmethod
    def available_databases():
        """
        When run, the utility function returns and logs the available entrez databases

        """
        dbs = {"pubmed", "protein", "nuccore", "ipg",
               "nucleotide", "structure", "sparcle", "gtr",
               "protfam", "genome", "annotinfo", "assembly",
               "bioproject", "biosample", "blastdbinfo", "books",
               "cdd", "clinvar", "gap", "gapplus",
               "grasp", "dbvar", "gene", "gds",
               "geoprofiles", "homologene", "medgen", "mesh",
               "ncbisearch", "nlmcatalog", "omim", "orgtrack",
               "pmc", "popset", "proteinclusters", "pcassay",
               "biosystems", "pccompound", "pcsubstance", "biocollections",
               "seqannot", "snp", "sra" "taxonomy",
               }

        logging.info(f"Available databases: \n{dbs}")

        return dbs


if __name__ == '__main__':
    Utils()
