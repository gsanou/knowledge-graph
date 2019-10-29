#!usr/bin/env python
# -*- coding:utf-8 -*-

# pip install py2neo==2.0.8

from py2neo import Graph, Node, Relationship
# from ownthink import *

# 连接数据库
graph = Graph('http://localhost:7474', username='neo4j', password='0905')
# graph = Graph()
graph.delete_all()

# 创建结点，类型是robot，剩下是属性
node1 = Node('robot', label=["aaa","bbb","ccc"], name="家务型机器人", page=3, property="我也不知道")
node2 = Node('robot', label="lalala", name="操作型机器人", age=2)
# node3 = Node('robot', label="lily",   name="程控型机器人", age=23)
# node4 = Node('robot', label="asdasd", name="数控形机器人", age=23)
# node5 = Node('robot', label="asdaasasasd", name="搜救类机器人", age=5)
# node6 = Node('robot', label="asdaasasasd", name="平台型机器人", age=55)
# node7 = Node('robot', label="asdaasasasd", name="示教再现型机器人", age=555)
# node8 = Node('robot', label="asdaasasasd", name="感觉控制型机器人", age=5555)
# node9 = Node('robot', label="asdaasasasd", name="适应控制型机器人", age=55555)
# node10 = Node('robot', label="asdaasasasd", name="学习控制型机器人", age=555555)
# node11 = Node('robot', label="asdaasasasd", name="智能机器人", age=55555555)




# 把结点放到到图上去
# for node in [node1, node2, node3, node4, node5, node6, node7, node8, node9, node10, node11]:
for node in [node1, node2]:
    graph.create(node)


# create(n:Person:Student {name:"aaa",school:"bbb"})

# Match (n)
# where labels(n)= ['Person',"Student"]
# return n


