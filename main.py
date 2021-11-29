import pysolr

endpoint = "https://api.archives-ouvertes.fr/search/LIFAT"

solr = pysolr.Solr(endpoint)

res = solr.search("")
for article in res:
    print(article)


