# -*- coding: utf-8 -*-
import json
import codecs
from configobj import ConfigObj
from rdflib import URIRef, BNode, Literal
from rdflib import Graph
import re
import uuid
from owlready2 import *
from owl_test import *

last_status = ""
last_class = "Thing"
i_new = "Thing"

class JSON2RDF:
    """
    """

    def __init__(self):
        '''This is the init. method

        :returns:  s.

        TODO: init based on the mapping file
        The mapping file defines:
             1. JSON Key -> predicateURI
             2. primary key -> subject
             3. atomic JSON object's type: to determine a tuple: primary key
                is_a type (optional)

        '''
        self.g = Graph()
    #
    # def node_factory(self, node_type):
    #     pass
    #
    # def add_triple(self, s, p, o):
    #     s_node = URIRef(s)
    #     p_node = URIRef(p)
    #     o_node = Literal(o)
    #     self.g.add((s_node, p_node, o_node))
    #
    # def getSerializedStr(self):
    #     return self.g.serialize(format='xml')
    #
    # def getSerializedStrByFormat(self, output_format):
    #     return self.g.serialize(format=output_format)
    #
    # def clear(self):
    #     self.g = Graph()
    #
    # def json_object_translator(self, json_obj):
    #     keys = json_obj.keys()
    #     idURI = ""
    #     if "ID" in keys:
    #         idURI = Vocabulary.ID_PREFIX + json_obj["ID"]
    #         if "Category" in keys:
    #             self.add_triple(idURI, Vocabulary.CATEGORY, json_obj["Category"])
    #         if "Telephone" in keys:
    #             self.add_triple(idURI, Vocabulary.TELEPHONE, json_obj["Telephone"])
    #         if "Name" in keys:
    #             self.add_triple(idURI, Vocabulary.NAME, json_obj["Name"])
    #         if "District" in keys:
    #             self.add_triple(idURI, Vocabulary.DISTRICT, json_obj["District"])
    #         if "Longitude" in keys:
    #             self.add_triple(idURI, Vocabulary.LONGITUDE, json_obj["Longitude"])
    #         if "Latitude" in keys:
    #             self.add_triple(idURI, Vocabulary.LATITUDE, json_obj["Latitude"])
    #         if "MoreInfo" in keys:
    #             self.add_triple(idURI, Vocabulary.MOREINFO, json_obj["MoreInfo"])
    #     else:
    #         pass # TODO: Log errors
    #
    #
    # def translate(self, json_str):
    #     '''This function is used to extract URIs.
    #     :param json_str: valid JSON string.
    #     :type json_str: str.
    #     :returns:  str. RDF string for the input json_str.
    #
    #     '''
    #     try:
    #         raw_data = json.loads(json_str)
    #         print ('pass')
    #         for json_obj in raw_data:
    #             self.json_object_translator(json_obj)
    #         return self.getSerializedStr()
    #     except ValueError:
    #         print ('exception')


class Vocabulary(object):
    #TODO: initialize this class from configuration file
    #Object_ID_Prefix
    ID_PREFIX = "http://openisdm.com/MAD/facility/"
    #Attributes
    NAME = "http://openisdm.com/MAD/property/hasName"
    TYPE = "http://openisdm.com/MAD/property/hasType"
    CATEGORY = "http://openisdm.com/MAD/property/hasCategory"
    DISTRICT = "http://openisdm.com/MAD/property/hasDistrict"
    ADDRESS = "http://openisdm.com/MAD/property/hasAddress"
    TELEPHONE = "http://openisdm.com/MAD/property/hasTelephone"
    LATITUDE = "http://openisdm.com/MAD/property/latitude"
    LONGITUDE = "http://openisdm.com/MAD/property/longitude"
    MOREINFO = "http://openisdm.com/MAD/property/moreInfo"
    #Facility Categories
    SHELTER_INDOOR = "SHELTER INDOOR"
    SHELTER_OUTDOOR = "SHELTER OUTDOOR"
    MEDICAL = "MEDICAL"
    RESCUE = "RESCUE"
    LIVELIHOOD = "LIVELIHOOD"
    COMMUNICATION = "COMMUNICATION"
    VOLUNTEER_ASSOCIATION = "VOLUNTEER ASSOCIATION"
    TRANSPORTATION = "TRANSPORTATION"




def reset_test_data():
    config = ConfigObj()
    config.filename = 'mapping.conf'
    config['ObjectTypeUri'] = "http://cool_uri/facility"
    config['ObjectId'] = "ID"
    config['Attributes'] = {}
    config['Attributes']["Name"] = "http://cool_uri/hasName"
    config['Attributes']["Type"] = "http://cool_uri/hasType"
    config['Attributes']["District"] = "http://cool_uri/hasDistrict"
    config['Attributes']["Address"] = "http://cool_uri/hasAddress"
    config['Attributes']["Telephone"] = "http://cool_uri/hasTelephone"
    config['Attributes']["Latitude"] = "http://cool_uri/hasLatitude"
    config['Attributes']["Longitude"] = "http://cool_uri/hasLongitude"
    config['Attributes']["MoreInfo"] = "http://cool_uri/hasMoreInfo"
    config.write()


def main():
    # path = "/Users/yuhaomao/Desktop/MAD_JSON2RDF/hello2222.rdf"
    # # iri= "http://www.semanticweb.org/yuhaomao/ontologies/2019/9/untitled-ontology-17"
    # onto = get_ontology(path).load()

    add_class("super", Thing)
    # j2r = JSON2RDF()
    # reset_test_data()
    # filename  = "test_json"
    # with codecs.open('/Users/yuhaomao/Desktop/MAD_JSON2RDF/111111.json', 'r', encoding='utf8') as f:
    with codecs.open('/Users/yuhaomao/Desktop/PublicDevice/Device.json', 'r', encoding='utf8') as f:
        json_str = f.read()

    datas = json.loads(json_str)
    print("json_str:")
    print(datas)
    datas_process(datas)
    # for individual in datas:
    #     print("individual:")
    #     print(individual)
    #     a = str(type(datas.get(individual)))
    #     print(a)
    #     if a == "<class 'dict'>":
    #         print("xxxxxxxxxxxxx")
    #     if a =="<class 'list'>":
    #         print("cccccccccc")

        # for i in data3.get(individual):
        #     print("i:")
        #     print(i)


def datas_process(datas):
    global last_status
    global last_class
    # global i_new
    datas_type = str(type(datas))
    # print("line 162:")
    # print(datas_type)

    if datas_type == "<class 'list'>":
        # print("zero: create UUID hasobject")
        # print("first: create class and lemma class(subclass)")
        # print("second: create dataproperty hasXXX")
        # print("forth: create dataproperty hasobject")
        # print("for i in list:            datas_process[i]")
        for i in datas:
            # print("line172")
            # print(i)
            # i_new = str(i).replace(" ","_")
            datas_process(i)

    if datas_type == "<class 'dict'>":
        # print("zero: create individual uuid")
        individual_id = uuid.uuid4()
        add_individual("super", individual_id)
        # print("for i in dictionary:")
        # print("if  .get(i) 是dict 或者list的话就创建class")
        # print("         first: create class XXX and lemma class(subclass)")
        # print("         second: create dataproperty hasXXX")
        # # print("third: create individual UUID")
        # print("else: .get(i)是string或者int的话，就创建data property")
        # print("datas_process(dictionary.get(i))")
        last_status = "dict"
        for i in datas:
            i_new = last_class+"__"+string_process(i)
            # print("line202")
            # print(i)
            # print(str(type(datas.get(i))))
            tmp = last_class
            if str(type(datas.get(i))) == "<class 'dict'>":
                add_class(i_new,last_class)
                last_class = i_new
                # add_class("xxzzxxzx", "xxx")
                print("i_new_209:")
                print(i_new)
                # print("         first: create class XXX and lemma class(subclass)")
                # print("         second: create dataproperty hasXXX")
                # print("shi _____dict")
                datas_process(datas.get(i))
                last_class = tmp
            if str(type(datas.get(i))) == "<class 'list'>":
                add_class(i_new, last_class)
                last_class = i_new
                print("i_new_219")
                print(i_new)
                # print("         first: create class XXX and lemma class(subclass)")
                # print("         second: create dataproperty hasXXX")
                # print("shi _____list")
                datas_process(datas[i])
                last_class = tmp
                # pass

            if str(type(datas.get(i))) == "<class 'str'>":
                # print("shi_____str")
                datas_process(datas[i])
            if str(type(datas.get(i))) == "<class 'int'>":
                print(datas.get(i))
            if str(type(datas.get(i))) == "<class 'float'>":
                print(datas.get(i))
            if str(datas.get(i)) == "True":
                print("true")
            if str(type(datas.get(i))) == "false":
                print("false")


    if datas_type == "<class 'str'>":
        # print("之前dataproporty的value")
        print(datas)


    if datas_type == "<class 'int'>":
        # print("之前dataproporty的value")
        print(datas)


def string_process(datas):
    punctuation = '/\\s!,;:?"\''
    def removePunctuation(text):
        text = re.sub(r'[{}]+'.format(punctuation), '', text)
        return text.strip()
    return removePunctuation(datas)

if __name__ == "__main__":
    # g = Graph()
    main()
    # value_str = "'audi': 'bmw'"
    # value_dic = {'audi': 'bmw'}
    # value_list = ['audi', 'bmw']
    #
    # # text_process(value)
    # datas_process(value_str)
    # datas_process(value_dic)
    # datas_process(value_list)