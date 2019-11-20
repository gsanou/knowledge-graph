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
