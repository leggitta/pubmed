from Bio import Entrez
import os
import pandas as pd

class Query(pd.DataFrame):
    def search(self, email, term, db='pmc', retmax=int(1e5)):
        Entrez.email = email
        handle = Entrez.esearch(db=db, term=term, retmax=retmax)
        results = Entrez.read(handle)
        id_list = r['IdList']
