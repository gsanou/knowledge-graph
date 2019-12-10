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
        # print("xxxxx")
        # print(i)
        if str(i[1])[-15:] == "NamedIndividual":
            print("individual")
            print(i[0])
            query_individual_content_individual(rdf_about, str(i[0].split("#")[1]))


def query_individual_content_individual(rdf_about,individual_name):
    print("individual name")
    print(individual_name)
    g = rdflib.Graph()
    # g.parse("/Users/yuhaomao/Desktop/MAD_JSON2RDF/hello2222.rdf", format="xml")
    g.parse("/Users/yuhaomao/Desktop/MAD_JSON2RDF/hello2222.rdf", format="xml")

    q = "SELECT ?s ?p WHERE{<" + rdf_about + "#" + individual_name + "> ?s ?p . ?p rdf:type <http://www.w3.org/2002/07/owl#NamedIndividual> .}"
    # q = "SELECT ?s ?p WHERE{<file:///Users/yuhaomao/Desktop/MAD_JSON2RDF/hello2222.rdf#individual_id60> ?s ?p . ?p rdf:type <http://www.w3.org/2002/07/owl#NamedIndividual> .}"
    x = g.query(q)
    t = list(x)
    print(t)
    if len(t) == 0:
        print("KKKKOOOONNNNGGGG")
    else:
        for i in t:
            print("yyyyyyyyyyyyyyyyyy")
            print(i[1].split("#")[1])
            print("cccccc")
        # child = i[0].split("#")[1]
        # print(child)


def rdf_about():
    g = rdflib.Graph()
    # g.parse("/Users/yuhaomao/Desktop/MAD_JSON2RDF/hello2222.rdf", format="xml")
    result = g.parse("/Users/yuhaomao/Desktop/MAD_JSON2RDF/hello2222.rdf", format="xml")
    for i in result:
        rdf_about = i[0].split("#")[0]
        break
    return rdf_about
if __name__ == "__main__":
    rdf_about = rdf_about()
    print(rdf_about)
    # create()
    # query_class()
    query_individual()
    # query_individual_content_individual(rdf_about,"individual_id61")
