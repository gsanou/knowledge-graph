from owlready2 import *
import uuid
path = "/Users/yuhaomao/Desktop/AES-CN/owlready_test/hello.rdf"
# iri= "http://www.semanticweb.org/yuhaomao/ontologies/2019/9/untitled-ontology-17"
onto = get_ontology(path).load()
# print(onto.Drug)
with onto:
    class Drug(Thing):
        pass
#     class Drug1(Thing):
#         pass
#     class Drug2(Thing):
#         pass
#     class Ingredient(Thing):
#         pass
#     class has_for_ingredient(ObjectProperty):
#         domain = [Drug]
#         range = [Ingredient]

# my_drug111 = Drug("individual")
# acetaminophen = Ingredient("acetaminophen")
# my_drug.has_for_ingredient = [acetaminophen]
# onto.save("hello111.rdf")

# 添加单独一个class
def add_class(name, parent,onto):
    with onto:
        exec('class {}({}): pass'.format(name, parent))
# add_class("xxx", Thing,onto)

# 创建uuid属于某个class
def add_individual(class_name, parent_class, individual_name,onto):
    print(individual_name)
    print(type(individual_name))
    with onto:
        # exec('class {class_name}({parent}): pass'.format(class_name=class_name, parent=parent_class))
        exec('{class_name}("{individual_name}")'.format(class_name=class_name, individual_name=individual_name))
# add_individual("Drug",Thing, "indivu",onto)

# 创建data_property
# plan1
def add_dataproperty(dataproperty_name,domain,range):
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
        exec('class {0}(DataProperty): \n domain=[{1}]  \n range=[{2}]'.format(dataproperty_name,domain_value,range_value))
    onto.has_for_synonym = ["acetaminophen", "paracétamol"]
# add_dataproperty("has_for_synonym","Thing","str")

# 添加 data_property 的value

onto.save("hello.rdf")

