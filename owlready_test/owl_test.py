from owlready2 import *
# path = "/Users/yuhaomao/Desktop/new_robot.owl"
iri= "http://www.semanticweb.org/yuhaomao/ontologies/2019/9/untitled-ontology-17"
onto = get_ontology(iri)
with onto:
    class Drug(Thing):
        pass
    class Ingredient(Thing):
        pass
    class has_for_ingredient(ObjectProperty):
        domain = [Drug]
        range = [Ingredient]


my_drug = Drug("my_drug")
acetaminophen = Ingredient("acetaminophen")
my_drug.has_for_ingredient = [acetaminophen]
onto.save("hello.rdf")




# add_class() 可以通过调用的时候选择class名字并且选择父节点
def add_class(name, parent, onto):
    with onto:
        exec('class {}({}): pass'.format(name, parent))

