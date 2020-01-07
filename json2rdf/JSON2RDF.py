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
count = 0
last_individual = ""
last_objectproperty = ""

def main():
    # path = "/Users/yuhaomao/Desktop/MAD_JSON2RDF/hello2222.rdf"
    # # iri= "http://www.semanticweb.org/yuhaomao/ontologies/2019/9/untitled-ontology-17"
    # onto = get_ontology(path).load()

    add_class("super", Thing)
    # j2r = JSON2RDF()
    # reset_test_data()
    # filename  = "test_json"
    # with codecs.open('/Users/yuhaomao/Desktop/JSON_Sample/BasicFunctionBlocks/BasicFunctionBlocks/robotic/CCTARoSDK_Multi_Robot_Move_PTP.json', 'r', encoding='utf8') as f:
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
    global count
    global last_individual
    global last_objectproperty
    # global i_new
    datas_type = str(type(datas))

    if datas_type == "<class 'list'>":

        tmp_last_individual = last_individual
        tmp_last_objectproperty = last_objectproperty

        for i in datas:
            # print("line172")
            # print(i)
            # i_new = str(i).replace(" ","_")
            datas_process(i)
            last_individual = tmp_last_individual
            last_objectproperty = tmp_last_objectproperty


    if datas_type == "<class 'dict'>":
        # print("zero: create individual uuid")
        # individual_id = uuid.uuid4()
        individual_id = "individual_id" + str(count)
        count += 1
        if last_class == "Thing":
            add_individual("super", individual_id)
        else:
            add_individual(last_class,individual_id)

        if last_individual == "" or last_objectproperty == "":
            pass
        else:
            add_individual_individual_objectproperty(last_individual,last_objectproperty,individual_id)

        last_individual = individual_id

        # tmp_last_individual = last_individual
        # tmp_last_objectproperty = last_objectproperty

        last_status = "dict"
        for i in datas:
            i_new = last_class+"__"+string_process(i)
            # print("line202")
            # print(i)
            # print(str(type(datas.get(i))))
            tmp = last_class
            tmp_last_individual = last_individual
            tmp_last_objectproperty = last_objectproperty

            if str(type(datas.get(i))) == "<class 'dict'>":
                add_class(i_new,last_class)
                objectproperty_name = "has"+ str(i_new)
                # print("xxxxxxxx")
                # print(objectproperty_name)

                if last_class == "Thing":
                    add_objectproperty("super", objectproperty_name, i_new)
                else:
                    add_objectproperty(last_class,objectproperty_name,i_new)

                last_class = i_new
                last_individual = individual_id
                last_objectproperty = objectproperty_name

                # add_class("xxzzxxzx", "xxx")
                # print("i_new_209:")
                # print(i_new)
                # print("         first: create class XXX and lemma class(subclass)")
                # print("         second: create dataproperty hasXXX")
                # print("shi _____dict")
                datas_process(datas.get(i))
                last_class = tmp
                last_individual = tmp_last_individual
                last_objectproperty = tmp_last_objectproperty

            if str(type(datas.get(i))) == "<class 'list'>":
                add_class(i_new, last_class)

                objectproperty_name = "has" + str(i_new)
                # print("xxxxxxxx")
                # print(objectproperty_name)
                if last_class == "Thing":
                    add_objectproperty("super", objectproperty_name, i_new)
                else:
                    add_objectproperty(last_class, objectproperty_name, i_new)

                last_class = i_new
                last_objectproperty = objectproperty_name

                # print("i_new_219")
                # print(i_new)
                # print("         first: create class XXX and lemma class(subclass)")
                # print("         second: create dataproperty hasXXX")
                # print("shi _____list")
                datas_process(datas[i])
                last_class = tmp
                last_individual = tmp_last_individual
                last_objectproperty = tmp_last_objectproperty
                # pass


            if str(type(datas.get(i))) == "<class 'str'>" or str(datas.get(i)) == "True" or str(type(datas.get(i))) == "false":
                data_property_name = "has"+ i
                add_dataproperty(data_property_name,tmp,"str")
                add_data_value(individual_id,data_property_name,datas.get(i))
                # datas_process(datas[i])
                # last_class = tmp
                # last_individual = tmp_last_individual
                # last_objectproperty = tmp_last_objectproperty


            if str(type(datas.get(i))) == "<class 'int'>":
                data_property_name = "has" + i
                add_dataproperty(data_property_name, tmp, "int")
                add_data_value(individual_id, data_property_name, datas.get(i))
                # datas_process(datas.get(i))


            if str(type(datas.get(i))) == "<class 'float'>":
                # print(datas.get(i))
                data_property_name = "has" + i
                add_dataproperty(data_property_name, tmp, "int")
                add_data_value(individual_id, data_property_name, datas.get(i))
                # datas_process(datas.get(i))
            # last_class = tmp
            # last_individual = tmp_last_individual
            # last_objectproperty = tmp_last_objectproperty


    if datas_type == "<class 'str'>":
        # print("之前dataproporty的value")
        print("sssssssssssssssssssss")
        print(datas)


    if datas_type == "<class 'int'>":
        # print("之前dataproporty的value")
        print("iiiiiiiiiiiiiiiiiii")
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