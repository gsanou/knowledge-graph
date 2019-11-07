from SPARQLWrapper import SPARQLWrapper, JSON

sparql = SPARQLWrapper("http://localhost:3030/db/query")
sparql.setQuery('''
    # PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    # SELECT ?s
    # WHERE { ?s ?p ?o .}
    # LIMIT 3
    
    SELECT ?subject ?predicate ?object
    WHERE {
        ?subject ?predicate ?object
    }
    LIMIT 25
    
    
    '''
)

sparql.setReturnFormat(JSON)
results = sparql.query().convert()

for result in results:
    print(result)