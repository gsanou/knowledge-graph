import os
from py2neo import Graph, Node, Relationship,Database,NodeMatcher,RelationshipMatcher

graph = Graph('http://localhost:7474', username='neo4j', password='0905')

matcher = NodeMatcher(graph)
rmatcher = RelationshipMatcher(graph)

########################################
# example1：
# 已知node的信息
# 然后根据node的信息进行查询
# 可以查询关系
# 可以查询节点id
########################################

# a = matcher.match("Root_吃饭", name="吃饭").first()   #a Node
# b = matcher.match("吃饭", name="manger").first()
# r1 = rmatcher.match({a,b}).first()   # a Relationship
# print("r1（a和b的关系）:")
# print(r1)
# print("\n")
#
# c = matcher.match("吃饭", name="吃饭").first()
# r2 = rmatcher.match({a,c}).first()
# print("r2（a和c的关系）:")
# print(r2)
# print("\n")
#
# print("c节点的id")
# print(c)
# print("\n")


########################################
# example2:
# 不知道node的具体信息，只知道名字
# node存在的话
# 输出所有node ID
########################################

# a = list(matcher.match(name="水果"))
# print(a)

########################################
# example3:
# 知道id
# 查询相邻的关系
# start n=node(886) return n
########################################

# from test_neo4j import *
# id = 868
# # neo4j_client = Neo4j_client()
# # # neighbors = neo4j_client.driver.session().write_transaction(neo4j_client.get_neighbors_relations,'Graph', '吃饭')
# command = 'start n=node(%d) return n' % id
# Graph.run(command)
from ownthink import *
sizhi = OwnThink()

sizhi.web_kg('吃饭')