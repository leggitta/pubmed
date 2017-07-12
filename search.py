from Bio import Entrez
import pandas as pd

Entrez.email = "leggitta3@gmail.com"

term = "ppg blood pressure"

query_handle = Entrez.egquery(term=term)
query_record = Entrez.read(query_handle)
results = query_record['eGQueryResult']
query_table = pd.DataFrame(results)
print(query_table)
