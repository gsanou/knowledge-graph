import requests
import re
from py2neo import Graph, Node, Relationship

graph = Graph('http://localhost:7474', username='neo4j', password='0905')
graph.delete_all()

def web_kg(entity):
    url = 'https://api.ownthink.com/kg/knowledge?entity=%s' % entity
    sess = requests.get(url)
    text = sess.text

    print(text)

    response = eval(text)
    knowledge = response['data']

    nodes = []
    for avp in knowledge['avp']:
        if avp[1] == knowledge['entity']:
            continue
        node = {'source': knowledge['entity'], 'target': avp[1], 'type': "resolved", 'rela': avp[0]}
        nodes.append(node)

    count = 1
    l = locals()
    root_node = Node(entity, name=entity)
    for node in nodes:
        l['test_node' + str(count)] = Node(entity, name=node.get("target"))
        graph.create(l['test_node' + str(count)])

        l['test_node' + str(count) +"test_node"] = Relationship(root_node, node.get("rela"), l['test_node' + str(count)])
        graph.create(l['test_node' + str(count) +"test_node"])

        node = str(node)
        node = node.replace("'type'", 'type').replace("'source'", 'source').replace("'target'", 'target')
        print(node + ',')
        count += 1

if __name__ == '__main__':
    web_kg('水果')