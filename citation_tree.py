from Bio import Entrez
Entrez.email = "leggitta3@gmail.com"

pmid = 21135640

# get list of ids that cite this article
h = Entrez.elink(
    dbfrom="pubmed", linkname="pubmed_pubmed_citedin", id=pmid)
r = Entrez.read(h)
h.close()

cited_by = [int(l['Id']) for l in r[0]['LinkSetDb'][0]['Link']]
print(cited_by)

# get list of ids that this article cites
h = Entrez.elink(
    dbfrom="pubmed", linkname="pubmed_pubmed_refs", id=24752654)
r = Entrez.read(h)
h.close()

cites = [int(l['Id']) for l in r[0]['LinkSetDb'][0]['Link']]
print(cites)
