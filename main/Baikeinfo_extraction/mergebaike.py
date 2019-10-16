from baidubaike import *
import jieba
from py2neo import Graph, Node, Relationship

graph = Graph('http://localhost:7474', username='neo4j', password='0905')
graph.delete_all()

def collect_infos(word):
    baidu = BaiduBaike()
    # + ownthink api 输出
    # + 开源库的输出
    # + 最后都添加到merge_infos里面
    merge_infos = list()
    baidu_infos = baidu.info_extract_baidu(word)
    merge_infos += baidu_infos
    print("merge infos:")
    print(merge_infos)
    return merge_infos

def merge_infos_semantic(infos):
    sems_all = [item['current_semantic'] for item in infos]
    print("sems_all")
    print(sems_all)
    '''merge infos by semantics'''
    update_infos = list()
    for sem in set(sems_all):
        print("sem:")
        print(sem)
        sems_dict = {}
        for item in infos:
            if item['current_semantic'] == sem:
                sems_dict.update(item)
        update_infos.append(sems_dict)
    print("update")
    print(type(update_infos))
    print(update_infos)
    return update_infos

def rank_infos(infos):
    att_nums = 0
    cover = 0.0
    score_dict = {}
    ranked_infos = list()
    covered_list = []
    covered_rate = 0.6
    covered_index = 0

    for info in infos:
        att_nums += len(info)
    for index, info in enumerate(infos):
        info['score'] = len(info)/att_nums
        info['tags'] = ' '.join(info['tags'])
        score_dict[index] = info['score']
    score_dict = sorted(score_dict.items(), key=lambda asd:asd[1], reverse=True)
    '''rank the infos'''
    for tmp in score_dict:
        cover += tmp[1]
        if cover < covered_rate:
            covered_index += 1
        else:
            continue
        ranked_infos.append(infos[tmp[0]])
    '''print'''
    for index, info in enumerate(ranked_infos):
        print(index, info['score'], info['current_semantic'], info)

    return ranked_infos, covered_index

def compute_similarity(a, b):
    return len(set(a).intersection(set(b)))

def merge_infos_sim(infos, covered_index):
    for index in range(0, covered_index):
        for index_ in range(index + 1, covered_index):
            score_attr = compute_similarity(infos[index].keys(), infos[index_].keys())
            score_val = compute_similarity(infos[index].values(), infos[index_].values())

            score_pair = compute_similarity([key + str(value) for key, value in infos[index].items()],
                                            [key + str(value) for key, value in infos[index_].items()])

            print(index, index_, score_attr, score_val, score_pair)

def merge_infos(word):
    infos = collect_infos(word)
    update_infos = merge_infos_semantic(infos)
    ranked_infos, covered_index = rank_infos(update_infos)

    return ranked_infos

def storage_neo4j(knowledgess):
    for knowledges in knowledgess:
        for knowledge in knowledges:

            # create node
            node = Node(word,name = knowledges[knowledge])
            graph.create(node)

            # create relationship
            rela = Relationship(root_node, knowledge, node)
            graph.create(rela)

while(1):
    word = input('enter an word to search:\n')
    root_node = Node("Root_" + word, name=word)
    print("infos .....")
    infos = collect_infos(word)
    print("update_infos")
    update_infos = merge_infos_semantic(infos)
    storage_neo4j(update_infos)
    # print("ranked_infos")
    # ranked_infos, covered_index = rank_infos(update_infos)
    # print("merge_infos_sim .....")
    # merge_infos_sim(ranked_infos, covered_index)