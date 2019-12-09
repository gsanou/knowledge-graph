import rdflib
import json

def create_class(parent,child):
    context = [parent,child]
    jsondata = json.dumps(context, indent=4, separators=(',', ': '))
    filename = "filename.json"
    f = open(filename, 'a')
    f.write(jsondata)
    f.close()

def query_class():
    g = rdflib.Graph()
    g.parse("/Users/yuhaomao/Desktop/MAD_JSON2RDF/hello2222.rdf", format="xml")
    # <a,?,?>
    q = """
    SELECT ?subject ?object
	    WHERE { ?subject rdfs:subClassOf ?object }
    """
    x = g.query(q)
    t = list(x)
    for i in t:
        print(i)
        child = i[0].split("#")[1]
        parent = i[1].split("#")[1]
        print(child)
        print(parent)
        # create_class(parent,child)
        # jsondata = json.dumps(jsontext, indent=4, separators=(',', ': '))

def query_individual():
    g = rdflib.Graph()
    g.parse("/Users/yuhaomao/Desktop/MAD_JSON2RDF/hello2222.rdf", format="xml")

    q = """
        SELECT ?individual ?type
    	WHERE 
    	{ ?individual rdf:type ?type .
    	}
        """
    x = g.query(q)
    t = list(x)
    for i in t:
        # print(str(i[1]))
        # print(str(i[1])[-15:])
        if str(i[1])[-15:] == "NamedIndividual":
            print("individual")
            print(i[0])

def query_individual_content():
    g = rdflib.Graph()
    # g.parse("/Users/yuhaomao/Desktop/MAD_JSON2RDF/hello2222.rdf", format="xml")
    g.parse("/Users/yuhaomao/Desktop/MAD_JSON2RDF/hello2222.rdf", format="xml")
            # / Users / yuhaomao / Desktop / MAD_JSON2RDF / hello2222.rdf

    q = """
        SELECT ?s ?p
        WHERE
        {
         <file:///Users/yuhaomao/Desktop/MAD_JSON2RDF/hello2222.rdf#individual_id1> ?s ?p .
        }
        """

    x = g.query(q)
    t = list(x)
    print(t)
    for i in t:
        print(i)

if __name__ == "__main__":
    # create()
    # query_class()
    # query_individual()
    query_individual_content()