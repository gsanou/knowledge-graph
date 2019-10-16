from urllib import request
from lxml import etree
import codecs
from urllib import parse
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# from py2neo import Graph, Node, Relationship
#
# graph = Graph('http://localhost:7474', username='neo4j', password='0905')
# graph.delete_all()

class BaiduBaike():
    def __init__(self):
        pass

    def get_html(self, url):
        return request.urlopen(url).read().decode('utf-8').replace('&nbsp;', '')

    def info_extract_baidu(self, word):
        url = "http://baike.baidu.com/item/%s" % parse.quote(word)
        print(url)
        selector = etree.HTML(self.get_html(url))
        info_list = list()
        info_list.append(self.extract_baidu(selector))
        polysemantics = self.checkbaidu_polysemantic(selector)
        if polysemantics:
            info_list += polysemantics
        infos = [info for info in info_list if len(info) > 2]
        print(infos)
        return infos

    def extract_baidu(self, selector):
        info_data = {}
        if selector.xpath('//h2/text()'):
            info_data['current_semantic'] = selector.xpath('//h2/text()')[0].replace('    ', '').replace('（','').replace('）','')
        else:
            info_data['current_semantic'] = ''
        if info_data['current_semantic'] == '目录':
            info_data['current_semantic'] = ''

        info_data['tags'] = [item.replace('\n', '') for item in selector.xpath('//span[@class="taglist"]/text()')]
        if selector.xpath("//div[starts-with(@class,'basic-info')]"):
            for li_result in selector.xpath("//div[starts-with(@class,'basic-info')]")[0].xpath('./dl'):
                attributes = [attribute.xpath('string(.)').replace('\n', '') for attribute in li_result.xpath('./dt')]
                values = [value.xpath('string(.)').replace('\n', '') for value in li_result.xpath('./dd')]
                for item in zip(attributes, values):
                    info_data[item[0].replace('    ', '')] = item[1].replace('    ', '')
        return info_data

    def checkbaidu_polysemantic(self, selector):
        semantics = ['https://baike.baidu.com' + sem for sem in
                     selector.xpath("//ul[starts-with(@class,'polysemantList-wrapper')]/li/a/@href")]
        names = [name for name in selector.xpath("//ul[starts-with(@class,'polysemantList-wrapper')]/li/a/text()")]
        info_list = []
        if semantics:
            for item in zip(names, semantics):
                selector = etree.HTML(self.get_html(item[1]))
                info_data = self.extract_baidu(selector)
                info_data['current_semantic'] = item[0].replace('    ', '').replace('（','').replace('）','')
                if info_data:
                    info_list.append(info_data)
        # print(info_list)
        return info_list


baidu = BaiduBaike()
while(1):
    word = input('enter an word:')
    contentss = baidu.info_extract_baidu(word)
#     root_node = Node("Root_"+word, name=word)
#     count_root = 1
#     l = locals()
#     for contents in contentss:
#         # print("contents:")
#         # print(contents)
#         # print(type(contents))
#         for content in contents:
#
#             # create node
#             l['test_node_' + str(count_root)] = Node(word, name=contents[content])
#             graph.create(l['test_node_' + str(count_root)])
#
#             # create relationship
#             l['node_' + str(count_root) + "_root_node"] = Relationship(root_node, content, l['test_node_' + str(count_root)])
#             graph.create(l['node_' + str(count_root) + "_root_node"])