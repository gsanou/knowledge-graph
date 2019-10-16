import requests
import re
import jieba
from py2neo import Graph, Node, Relationship

# graph = Graph('http://localhost:7474', username='neo4j', password='0905')
# graph.delete_all()
# reg = "[^0-9A-Za-z\u4e00-\u9fa5]"  ####### remove symbol rule
# level=1

def web_kg(entity):
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
    print("现在搜索得到的knowledge是：")
    print(knowledge)
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

        count_root = 1
        l = locals()
        root_node = Node(entity, name=entity)
        for node in nodes:
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
            node = str(node)
            node = node.replace("'type'", 'type').replace("'source'", 'source').replace("'target'", 'target')
            print(node + ',')
            # count_root += 1

# if __name__ == '__main__':
#     web_kg('水果')