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

a = matcher.match("Root_吃饭", name="吃饭").first()   #a Node
b = matcher.match("吃饭", name="manger").first()
r1 = rmatcher.match({a,b}).first()   # a Relationship
print("r1（a和b的关系）:")
print(r1)
print("\n")

c = matcher.match("吃饭", name="吃饭").first()
r2 = rmatcher.match({a,c}).first()
print("r2（a和c的关系）:")
print(r2)
print("\n")

print("c节点的id")
print(c)
print("\n")


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

########################################

# a = matcher.get(868)
# print(a)
#
# b = list(rmatcher.match({a}))
# print(b)

########################################
# example4:
# 知道两个点的ID
# 查询两个点之间的关系
# 886 和 887 是node 的id地址
# 如果有关系的话    输出 "node1 - [关系]-> node2
# 如果没有关系的话  输出None
########################################

# nodeA_ID = matcher.get(886)
# nodeB_ID = matcher.get(887)
# find_relationship = graph.match_one({nodeA_ID,nodeB_ID})
# print(find_relationship)

########################################
# example5:
#
########################################