import requests
import re
import jieba
from py2neo import Graph, Node, Relationship

# graph = Graph('http://localhost:7474', username='neo4j', password='0905')
# graph.delete_all()
# reg = "[^0-9A-Za-z\u4e00-\u9fa5]"  ####### remove symbol rule
# level=1
class OwnThink():
    def __init__(self):
        pass

    def web_kg(self,entity):
        # global level
        url = 'https://api.ownthink.com/kg/knowledge?entity=%s' % entity
        # print("搜索的url是：")
        # print(url)
        sess = requests.get(url)
        text = sess.text
        # print("搜索到的text是：")
        # print(text)
        response = eval(text)
        knowledge = response['data']
        # print("现在搜索得到的knowledge是：")
        # print(knowledge)
        # if not knowledge:
        #     print("knowledge = empty")
        # if knowledge:
        #     print("knowledge != empty")
        nodes = []
        if knowledge:
            for avp in knowledge['avp']:
                # if avp[1] == knowledge['entity']:
                #     continue
                node = {'source': knowledge['entity'], 'target': avp[1], 'type': "resolved", 'rela': avp[0]}
                nodes.append(node)
            print(nodes)
            # count_root = 1
            # l = locals()
            # root_node = Node(entity, name=entity)
            # for node in nodes:
                # l['test_node_' + str(count_root)] = Node(entity, name=node.get("target"))
                # graph.create(l['test_node_' + str(count_root)])

                # child_node_string = node.get("target")                  ####### child node create
                # result = jieba.cut(child_node_string, HMM=False)        ####### jieba cut
                # tmp = " ".join(result)                                  ####### jieba cut
                # child_node_string = re.sub(reg, ' ', child_node_string) ####### remove symbols
                # first_word = re.split(r'\s', child_node_string)[0]      ####### first word in targert
                # print("第一个词语是：")
                # print(first_word)
                # print("entity 是：")
                # print(entity)
                # if level < 2 and first_word != entity:
                #     print("当前level < 2")
                #     level += 1
                #     web_kg(first_word)
                # else:
                #     print("当前level > 2")
                #     level = 1
                #     continue
                # if level == 2:
                #     level = 1

                # l['node_' + str(count_root) +"_root_node"] = Relationship(root_node, node.get("rela"), l['test_node_' + str(count_root)])
                # graph.create(l['node_' + str(count_root) +"_root_node"])
                #
                # node = str(node)
                # node = node.replace("'type'", 'type').replace("'source'", 'source').replace("'target'", 'target')
                # print(node + ',')
                # count_root += 1

if __name__ == '__main__':
    web_kg('吃饭')

#  百度百科：
# [{'current_semantic': '词语释义', 'tags': ['字词'], '中文名': '吃饭', '拼音': 'chī  fàn', '粤语发音': 'hek3 faan6', '韩语翻译': '먹다', '日文翻译': '食べる', '英语翻译': 'have a meal', '德语翻译': 'essen', '法语翻译': 'manger', '拉丁语翻译': 'Comede', '意大利语翻译': 'mangiare'},
#  {'current_semantic': '章小东著图书', 'tags': ['出版物', '书籍'], '书名': '吃饭', '作者': '章小东', 'ISBN': '978-7-208-11349-7/1·1122', '页数': '156页', '定价': '32.00元', '出版社': '上海人民出版社', '出版时间': '2013年8月', '插页': '2', '字数': '225.000'}]
# {'current_semantic': '钱钟书同名作品', 'tags': ['文学作品', '字词', '书籍', '中国文学'], '中文名': '吃饭', '作者': '钱钟书', '字': '默存', '号': '槐聚'},

# ownthink:
# [{'source': '吃饭[词语释义]', 'target': '吃饭', 'type': 'resolved', 'rela': '中文名'},
#  {'source': '吃饭[词语释义]', 'target': 'chīfàn', 'type': 'resolved', 'rela': '拼音'},
#  {'source': '吃饭[词语释义]', 'target': 'hek3faan6', 'type': 'resolved', 'rela': '粤语发音'},
#  {'source': '吃饭[词语释义]', 'target': '먹다', 'type': 'resolved', 'rela': '韩语翻译'},
#  {'source': '吃饭[词语释义]', 'target': '食べる', 'type': 'resolved', 'rela': '日文翻译'},
#  {'source': '吃饭[词语释义]', 'target': 'haveameal', 'type': 'resolved', 'rela': '英语翻译'},
#  {'source': '吃饭[词语释义]', 'target': 'essen', 'type': 'resolved', 'rela': '德语翻译'},
#  {'source': '吃饭[词语释义]', 'target': 'manger', 'type': 'resolved', 'rela': '法语翻译'},
#  {'source': '吃饭[词语释义]', 'target': 'Comede', 'type': 'resolved', 'rela': '拉丁语翻译'},
#  {'source': '吃饭[词语释义]', 'target': 'mangiare', 'type': 'resolved', 'rela': '意大利语翻译'}]
