import rdflib
import json
from individual_sort import *
import json

checked_list = []


def check_subindividual(check_list,a,individual,rdf_about,individual_list):
    # if len(individual_list) == 0:
    #     return individual
    if individual not in check_list:
        check_list.append(individual)
        subinviduals_dict = query_individual_content(a, individual, rdf_about)[1]
        individual_list.remove(individual)
        subindividual = []
        for subindi in subinviduals_dict:
            if type(subinviduals_dict[subindi]).__name__ == "str":
                subindividual.append(subinviduals_dict[subindi])
            elif type(subinviduals_dict[subindi]).__name__ == "list":
                for xx in subinviduals_dict[subindi]:
                    subindividual.append(xx)
        # print("subindividuals list:")
        # print(subindividual)
        if len(subindividual) == 1:
            for strindividual in subindividual:
                check_subindividual(check_list,a,strindividual,rdf_about,individual_list)
        elif len(subindividual) > 1:
            for listindividual in subindividual:
                check_subindividual(check_list,a,listindividual,rdf_about,individual_list)


def query_class():

    """
    查询class和parent_class
    但是没用到
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


def query_individual(a,rdf_about):
    """
    查询所有的 ?s
    如果 rdf：type是 namedindividual的话 输出
    """
    g = rdflib.Graph()
    g.parse("/Users/yuhaomao/Downloads/material_flow_0.0.2.owl", format="xml")

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
        if str(i[1])[-15:] == "NamedIndividual":
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
    """
    查询rdf_about的值
    """
    g = rdflib.Graph()
    # g.parse("/Users/yuhaomao/Desktop/MAD_JSON2RDF/hello2222.rdf", format="xml")
    result = g.parse("/Users/yuhaomao/Downloads/material_flow_0.0.2.owl", format="xml")
    for i in result:
        rdf_about = i[0].split("#")[0]
        break
    return rdf_about


def read_dictionary(a):
    """
    读dictionary 里的key和value
    没用到
    """
    if type(a).__name__ == "dict":
        for i in a:
            # print(i)
            query_individual_content(a,i,rdf_about)
            if type(a[i]).__name__ == "list" or type(a[i]).__name__ == "dict":
                read_dictionary(a[i])
            if type(a[i]).__name__ == "str":
                print(a[i])

    if type(a).__name__ == "str":
        print(a)

    if type(a).__name__ == "list":
        for i in a:
            read_dictionary(i)

def query_individual_content(a,individual_name,rdf_about):
    """
    查询 individual的content
    dataproperty和value放在result里 存成一个 dictionary
    subindividual存在sub individuals里，存成一个list
    """
    g = rdflib.Graph()
    # print("????????????????????????????")
    # print(individual_name)
    g.parse("/Users/yuhaomao/Downloads/material_flow_0.0.2.owl", format="xml")
    q = "SELECT ?p ?o  WHERE { <" + rdf_about + "#" + individual_name + "> ?p ?o .}"
    x = g.query(q)
    t = list(x)
    result = {}
    sub_individuals = {}
    for i in t:
        # print("========")
        # print(i)
        dataproperty = i[0].split("#")[-1]
        dataproperty_value = i[1].split("#")[-1]
        if dataproperty_value != "NamedIndividual" and dataproperty != "type":
            if dataproperty_value in individual_list:
                if dataproperty in sub_individuals :
                    if type(sub_individuals[dataproperty]).__name__ == "str":
                        copy = sub_individuals[dataproperty]
                        tmp = [copy,dataproperty_value]
                        sub_individuals[dataproperty] = tmp
                    else:
                        sub_individuals[dataproperty].append(dataproperty_value)
                else:
                    sub_individuals[dataproperty] = dataproperty_value
            else:
                a = str(i[1])
                result[dataproperty] = a
    # print(result)
    # print(sub_individuals)
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
        if type(subindividual[i]).__name__ == "str":
            empty1 = {}
            dict[i] = create_json(subindividual[i],empty1)
        if type(subindividual[i]).__name__ == "list":
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
    rdf_about = rdf_about()
    # rdf_about = "file:///Users/yuhaomao/Desktop/MAD_JSON2RDF/hello2222.rdf"
    print(rdf_about)
    individual_list = query_individual(a,rdf_about)
    # individual_list = ['material_3', 'material_flow_1', 'function_block_3',
    #                    'process_1', 'material_2', 'material_flow_state_2',
    #                    'implemented_function_block_2', 'material_4',
    #                    'function_block_4', 'function_block_1', 'material_flow_state_1',
    #                    'function_block_5', 'implemented_process_1', 'pre_state_2',
    #                    'implemented_function_block_5', 'relation_object_2', 'relation_object_1',
    #                    'function_block_2', 'relation_subject_1', 'pre_state_1', 'application_1',
    #                    'implemented_function_block_1', 'material_relation_2', 'implemented_function_block_4',
    #                    'relation_subject_2', 'material_relation_1', 'implemented_function_block_3',
    #                    'post_state_1', 'material_1']
    
    print(individual_list)

    dict = {}
    # for i in individual_list:
    #     print("individual :::")
    #     print(i)
    #
    #     subinviduals = query_individual_content(a, i, rdf_about)[1]
    #     # subinviduals = {'has_implemented_process': 'implemented_process_1'}
    #     print("sub sub sub sub sub ")
    #     print(subinviduals)
    #
    #     for x in subinviduals:
    #         print("subindividuals        subindividuals")
    #         if type(subinviduals[x]).__name__ == "str":
    #             item = {i:subinviduals[x]}
    #             print("itemmmmmmmmmm        str")
    #             print(item)
    #             print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    #             print(dict)
    #             replace(dict,"dict",item)
    #             print(dict)
    #         if type(subinviduals[x]).__name__ == "list":
    #             for xx in subinviduals[x]:
    #                 print("itemmmmmmmmmm        list")
    #                 item = {i:xx}
    #                 print(item)
    #                 replace(dict,"dict",item)
    #                 print("dictttttttttttttttttttttttdicttttttttttttttttttttttt")
    #                 print(dict)
    #             # item = {i: subinviduals[x]}
    #             # print("itemmmmmmmmmm        list")
    #             # print(item)
    #             # for xx in item:
    #
    #     print(dict)
    #     # create_json("individual_id0",dict)
    #
    #     # filename = 'names.json'
    #     # with open(filename, 'w') as file_obj:
    #     #     json.dump(dict, file_obj)
    #
    #     # query_individual_content(a,"individual_id1",rdf_about)

    for a in range(len(individual_list)):
        i = individual_list[0]
        # print("individuaaaaa individuaaaaa individuaaaaa individuaaaaa")
        # print(i)
        check_subindividual(checked_list, a, i, rdf_about, individual_list)
        if len(individual_list) == 0:
            result = i
            break

    print(result)
    # create_json("material_flow_1",dict)
    # filename = 'names.json'
    # with open(filename, 'w') as file_obj:
    #     json.dump(dict, file_obj)