import requests
import re
import jieba
from py2neo import Graph, Node, Relationship

g = Graph('http://localhost:7474', username='neo4j', password='0905')
g.delete_all()
# tx = graph.begin()
# a = Node("person", name = "AAA")
# tx.create(a)
# b = Node("person", name = "BBB")
# tx.create(b)
#
# ab = Relationship(a,"不认识",b)
# tx.create(ab)
# tx.commit()
# graph.exit(ab)


tx = g.begin()
a = Node(label="明星", name="张鹤伦")
tx.create(a)
b = Node(label="明星", name="张伦")
ab = Relationship(a, "师兄弟", b)
tx.create(ab)
tx.commit()
g.exists(ab)


# reg = "[^0-9A-Za-z\u4e00-\u9fa5]"  ####### remove symbol rule
# level=1
# # current_node = {}
#
# def web_kg(entity):
#     global level
#     global current_node
#     url = 'https://api.ownthink.com/kg/knowledge?entity=%s' % entity
#     # print("搜索的url是：")
#     # print(url)
#     sess = requests.get(url)
#     text = sess.text
#     # print("搜索到的text是：")
#     # print(text)
#     response = eval(text)
#     knowledge = response['data']
#     print("现在搜索得到的knowledge是：")
#     print(knowledge)
#     # if not knowledge:
#     #     print("knowledge = empty")
#     # if knowledge:
#     #     print("knowledge != empty")
#     nodes = []
#     if knowledge:
#         for avp in knowledge['avp']:
#             # if avp[1] == knowledge['entity']:
#             #     continue
#             node = {'source': knowledge['entity'], 'target': avp[1], 'type': "resolved", 'rela': avp[0]}
#             nodes.append(node)
#
#         count_root = 1
#         l = locals()
#         if level == 1:
#             root_node = Node(entity, name=entity)
#         else:
#             root_node = current_node
#         for node in nodes:
#             # create node
#             l['test_node_' + str(count_root)] = Node(entity, name=node.get("target"))
#             current_node = l['test_node_' + str(count_root)]
#             graph.create(l['test_node_' + str(count_root)])
#             print("当前node 是")
#             print(current_node)
#             print(root_node)
#             print(type(root_node))
#             # create relationship
#             l['node_' + str(count_root) + "_root_node"] = Relationship(root_node, node.get("rela"),l['test_node_' + str(count_root)])
#             graph.create(l['node_' + str(count_root) + "_root_node"])
#             count_root += 1
#
#             child_node_string = node.get("target")                  ####### child node create
#             result = jieba.cut(child_node_string, HMM=False)        ####### jieba cut
#             tmp = " ".join(result)                                  ####### jieba cut
#             child_node_string = re.sub(reg, ' ', child_node_string) ####### remove symbols
#             first_word = re.split(r'\s', child_node_string)[0]      ####### first word in targert
#             print("第一个词语是：")
#             print(first_word)
#             print("entity 是：")
#             print(entity)
#             if level < 2 and first_word != entity:
#                 print("当前level < 2")
#                 level += 1
#                 web_kg(first_word)
#             else:
#                 print("当前level > 2")
#                 # level = 1
#                 continue
#     else:
#         level -= 1
#             # if level == 2:
#             #     level = 1
#
#             # l['node_' + str(count_root) +"_root_node"] = Relationship(root_node, node.get("rela"), l['test_node_' + str(count_root)])
#             # graph.create(l['node_' + str(count_root) +"_root_node"])
#
#             # node = str(node)
#             # node = node.replace("'type'", 'type').replace("'source'", 'source').replace("'target'", 'target')
#             # print(node + ',')
#             # count_root += 1
#
# if __name__ == '__main__':
#     web_kg('水果')