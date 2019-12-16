import rdflib
import json
from individual_sort import *
import json

def create_class(parent,child):
    context = [parent,child]
    jsondata = json.dumps(context, indent=4, separators=(',', ': '))
    filename = "filename.json"
    f = open(filename, 'a')
    f.write(jsondata)
    f.close()

def query_class():

    """
    查询class和parent_class
    """

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

def query_individual(a,rdf_about):
    """
    查询所有的 ?s
    如果 rdf：type是 namedindividual的话 输出
    """
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
    result = []
    for i in t:
        # print(str(i[1]))
        # print(str(i[1])[-15:])
        # print("xxxxx")
        # print(i)
        if str(i[1])[-15:] == "NamedIndividual":
            # print(i[0].split("#")[1])
            result.append(i[0].split("#")[1])
            # query_individual_content_individual(rdf_about, str(i[0].split("#")[1]),a)
    return result

def individual_or_not(a,individual_name,rdf_about):
    """
    给定一个value 判断这个value是不是individual
    是的话return true
    不是的话 return false
    """
    g = rdflib.Graph()
    g.parse("/Users/yuhaomao/Desktop/MAD_JSON2RDF/hello2222.rdf", format="xml")

    q = "SELECT ?type WHERE { <" + rdf_about + "#" + individual_name + "> rdf:type ?type .}"
    x = g.query(q)
    t = list(x)
    print(t)
    if len(t) == 0:
        return False
    else:
        if t[0][0].split("#")[1] == "NamedIndividual" or t[1][0].split("#")[1] == "NamedIndividual":
            return True

def query_individual_content_individual(rdf_about,individual_name,dict):
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
            target = individual_name
            value = i[1].split("#")[1]
            replace_item = {target:value}
            a = dict
            replace(a,"a",replace_item)
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

def read_dictionary(a):
    if type(a) == dict:
        for i in a:
            # print(i)
            query_individual_content(a,i,rdf_about)
            if type(a[i]) == list or type(a[i]) == dict:
                read_dictionary(a[i])
            if type(a[i]) == str:
                print(a[i])

    if type(a) == str:
        print(a)

    if type(a) == list:
        for i in a:
            read_dictionary(i)

def query_individual_content(a,individual_name,rdf_about):
    """
    查询 individual的content
    dataproperty和value放在result里 存成一个 dictionary
    subindividual存在sub individuals里，存成一个list
    """
    g = rdflib.Graph()
    print("????????????????????????????")
    print(individual_name)
    g.parse("/Users/yuhaomao/Desktop/MAD_JSON2RDF/hello2222.rdf", format="xml")
    q = "SELECT ?p ?o  WHERE { <" + rdf_about + "#" + individual_name + "> ?p ?o .}"
    x = g.query(q)
    t = list(x)
    result = {}
    sub_individuals = {}
    for i in t:
        print("========")
        print(i)
        dataproperty = i[0].split("#")[-1]
        dataproperty_value = i[1].split("#")[-1]
        if dataproperty_value != "NamedIndividual" and dataproperty != "type":
            if dataproperty_value in individual_list:
                if dataproperty in sub_individuals :
                    if type(sub_individuals[dataproperty]) == str:
                        copy = sub_individuals[dataproperty]
                        tmp = [copy,dataproperty_value]
                        sub_individuals[dataproperty] = tmp
                    if type(sub_individuals[dataproperty]) == list:
                        sub_individuals[dataproperty].append(dataproperty_value)
                else:
                    sub_individuals[dataproperty] = dataproperty_value
            else:
                a = str(i[1])
                result[dataproperty] = a
    print(result)
    print(sub_individuals)
    return result,sub_individuals

def create_json(individual_name,dict):
    """
    根据individual 查询所有的content，
    如果content里面有别的individual的话，再递归
    定义一个dictionary，查询回来的结果直接dict[key] = value
    """
    all_individual_contents = query_individual_content(a,individual_name,rdf_about)
    datavalue = all_individual_contents[0]
    subindividual = all_individual_contents[1]
    for i in datavalue:
        dict[i] = datavalue[i]

    for i in subindividual:
        print("////////////////////////////////")
        print(i)
        print(subindividual[i])
        if type(subindividual[i]) == str:
            empty1 = {}
            dict[i] = create_json(subindividual[i],empty1)
        if type(subindividual[i]) == list:
            count = 0
            yigelist = []
            for x in subindividual[i]:
                yigelist.append({})
                dict[i] = create_json(x, yigelist[count])
                yigelist[count] = dict[i]
                count += 1
            count = 0
            dict[i] = yigelist

    print(dict)
    return dict



if __name__ == "__main__":
    a = {}
    #
    # rdf_about = rdf_about()
    rdf_about = "file:///Users/yuhaomao/Desktop/MAD_JSON2RDF/hello2222.rdf"
    print(rdf_about)
    # # create()
    # individual_list = query_individual(a,rdf_about)
    individual_list = ['individual_id10', 'individual_id29', 'individual_id40', 'individual_id92', 'individual_id43', 'individual_id93', 'individual_id84', 'individual_id23', 'individual_id69', 'individual_id31', 'individual_id17', 'individual_id48', 'individual_id24', 'individual_id85', 'individual_id21', 'individual_id41', 'individual_id58', 'individual_id82', 'individual_id12', 'individual_id88', 'individual_id55', 'individual_id9', 'individual_id51', 'individual_id3', 'individual_id94', 'individual_id14', 'individual_id60', 'individual_id32', 'individual_id59', 'individual_id16', 'individual_id53', 'individual_id70', 'individual_id38', 'individual_id67', 'individual_id63', 'individual_id89', 'individual_id33', 'individual_id6', 'individual_id95', 'individual_id11', 'individual_id77', 'individual_id19', 'individual_id28', 'individual_id83', 'individual_id86', 'individual_id96', 'individual_id30', 'individual_id78', 'individual_id0', 'individual_id20', 'individual_id42', 'individual_id71', 'individual_id5', 'individual_id56', 'individual_id75', 'individual_id74', 'individual_id39', 'individual_id73', 'individual_id7', 'individual_id4', 'individual_id64', 'individual_id26', 'individual_id22', 'individual_id65', 'individual_id47', 'individual_id81', 'individual_id27', 'individual_id66', 'individual_id2', 'individual_id68', 'individual_id1', 'individual_id62', 'individual_id76', 'individual_id52', 'individual_id72', 'individual_id15', 'individual_id46', 'individual_id8', 'individual_id18', 'individual_id34', 'individual_id36', 'individual_id87', 'individual_id13', 'individual_id35', 'individual_id57', 'individual_id44', 'individual_id50', 'individual_id80', 'individual_id45', 'individual_id37', 'individual_id79', 'individual_id90', 'individual_id61', 'individual_id54', 'individual_id49', 'individual_id25', 'individual_id91']
    individuals = {"individual_id22":["individual_id23",{"individual_id24":["individual_id25",{"individual_id26":"individual_id27"},{"individual_id28":"individual_id29"}]}]}
    # read_dictionary(individuals)
    dict = {}
    create_json("individual_id0",dict)


    filename = 'names.json'
    with open(filename, 'w') as file_obj:
        json.dump(dict, file_obj)
        
    # query_individual_content(a,"individual_id1",rdf_about)