from owlready2 import *
import uuid
# path = "/Users/yuhaomao/Desktop/AES-CN/owlready_test/hello.rdf"
# # iri= "http://www.semanticweb.org/yuhaomao/ontologies/2019/9/untitled-ontology-17"
# onto = get_ontology(path).load()

path = "/Users/yuhaomao/Desktop/MAD_JSON2RDF/hello2222.rdf"
# iri= "http://www.semanticweb.org/yuhaomao/ontologies/2019/9/untitled-ontology-17"
onto = get_ontology(path).load()

# print(onto.Drug)
# with onto:
#     class Drug(Thing):
#         pass
#     class Drug1(Thing):
#         pass
#     class Drug2(Thing):
#         pass
#     class Ingredient(Thing):
#         pass
#     class has_for_ingredient(ObjectProperty):
#         domain = [Drug]
#         range = [Ingredient]




# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# 添加单独一个class
def add_class(name, parent):
    with onto:
        # print("parent:")
        # print(parent)
        # print("name;")
        # print(name)
        if parent == "Thing" or parent == owl.Thing:
            # print("thingthingthing:")
            # print(parent)
            exec('class {}({}): pass'.format(name, parent))
        else:
            # print("else:")
            # print(parent)
            exec('class {}(onto.{}): pass'.format(name, parent))
        onto.save("hello2222.rdf")
# add_class("super", Thing)


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# 创建individual 属于某个class
def add_individual(class_name, individual_name):
    with onto:
        # print(class_name)
        exec('onto.{class_name}("{individual_name}")'.format(class_name=class_name, individual_name=individual_name))
        # exec('("{individual_name}")'.format(class_name=class_name, individual_name=individual_name))
    onto.save("hello2222.rdf")
# last_class = "Thing__devices"
# add_individual(last_class, "indsssvu") # parent应该是写thing就可以, 参考objectproperty，可以改成onto.classname


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# 创建data_property
# plan1
def add_dataproperty1(dataproperty_name,domain,range):
    with onto:
        onto_data_property = types.new_class(dataproperty_name, (DataProperty,))
        onto_data_property.domain = [domain]
        onto_data_property.range = [range]
# add_dataproperty("name1",Drug,str)

# plan2
# with onto:
#     class has_for_synonym(DataProperty):
#         domain = [Thing]
#         range = [int]
# onto.has_for_synonym = ["acetaminophen", "paracétamol"] # []里的两个参数没什么用好像

# plan3 推荐第三个
def add_dataproperty(dataproperty_name,domain_value,range_value):
    with onto:
        if domain_value == "Thing":
            exec('class {0}(DataProperty): \n domain=[{1}]  \n range=[{2}]'.format(dataproperty_name,domain_value,range_value))
        else:
            exec('class {0}(DataProperty): \n domain=[onto.{1}]  \n range=[{2}]'.format(dataproperty_name,domain_value,range_value))
    # onto.has_for_synonym = ["acetaminophen", "paracétamol"]
    onto.save("hello2222.rdf")
# add_dataproperty("hasversion","super","str")

def add_datapproperty_value(individual_name,dataproperty_name,value):
    with onto:
        print(type(value))
        if type(value) == str:
            exec('onto.{}.{} = ["{}"]'.format(individual_name,dataproperty_name,value))
        if type(value) == int:
            exec('onto.{}.{} = [{}]'.format(individual_name,dataproperty_name,value))
    onto.save("hello2222.rdf")
# add_datapproperty_value("aaa","has_for_synonym",123)
# onto.aaa.has_for_synonym = [123]


# onto.has_for_synonym = ["individual_id0", "ssss"]
# onto.save("hello2222.rdf")
# def add_dataproperty_value(data)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# 添加 data_property 的value
def add_data_value(individual_name,dataproperty_name,value):
    exec('onto.{0}.{1}.append("{2}")'.format(individual_name,dataproperty_name, value))
# add_data_value("my_drug","has_for_synonym","int")
# onto.my_drug.has_for_synonym.append("int")



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# 添加 object property
# def add_objectproperty(domain_name,objectproprety,range_name):
def add_objectproperty(domain_name,objectproprety,range_name):
    with onto:
        exec('class {0}(ObjectProperty): \n domain=[onto.{1}] \n range = [onto.{2}]'.format(objectproprety,domain_name,range_name))
    onto.save("hello2222.rdf")
        # class has_for_ingredient111111(ObjectProperty):
        #     domain = [onto.xxx]
        #     range = [onto.Ingredient]
# add_objectproperty("super","has_for_ingredient111111","Thing__devices")

# onto.save("hello2222.rdf")
# onto.aaa.has_for_synonym = [123]
# onto.save("hello2222.rdf")


def add_individual_individual_objectproperty(individual1,objectproperty,individual2):
    with onto:
        exec('onto.{0}.{1}.append(onto.{2})'.format(individual1,objectproperty,individual2))
    onto.save("hello2222.rdf")
# add_individual_individual_objectproperty("individual_id0","hasThing__devices","individual_id1")
# with onto:
#     class drug(Thing):
#         pass
#     class druggg(Thing):
#         pass
#     class hasss(ObjectProperty):
#         pass
        # domain = [onto.drug]
        # range = [onto.druggg]

# my_drug = onto.drug("aaa")
# acetaminophen = onto.druggg("bbb")

# my_drug.hasss = [acetaminophen]

# onto.aaa.hasss.append(onto.bbb)
# onto.save("hello2222.rdf")
