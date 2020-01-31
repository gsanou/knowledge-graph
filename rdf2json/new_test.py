from rdf2json import *
dict = {}
a = []
rdf_about = rdf_about()

# individual_list = ['material_3', 'function_block_3',
#                        'process_1', 'material_2', 'material_flow_state_2',
#                        'implemented_function_block_2', 'material_4',
#                        'function_block_4', 'function_block_1', 'material_flow_state_1',
#                        'function_block_5', 'implemented_process_1', 'pre_state_2',
#                        "material_flow_1",'implemented_function_block_5', 'relation_object_2', 'relation_object_1',
#                        'function_block_2', 'relation_subject_1', 'pre_state_1', 'application_1',
#                        'implemented_function_block_1', 'material_relation_2', 'implemented_function_block_4',
#                        'relation_subject_2', 'material_relation_1', 'implemented_function_block_3',
#                        'post_state_1', 'material_1']
# individual_list = ["material_flow_state_2"]
individual_list = query_individual(a,rdf_about)
print(individual_list)
checked_list = []


def check_subindividual(check_list,a,individual,rdf_about,individual_list):
    # if len(individual_list) == 0:
    #     return individual
    if individual not in check_list:
        check_list.append(individual)
        subinviduals_dict = query_individual_content(a, individual, rdf_about)[1]
        individual_list.remove(individual)
        subindividual = []
        for subindi in subinviduals_dict:
            if type(subinviduals_dict[subindi]).__name__ == "str":
                subindividual.append(subinviduals_dict[subindi])
            elif type(subinviduals_dict[subindi]).__name__ == "list":
                for xx in subinviduals_dict[subindi]:
                    subindividual.append(xx)
        # print("subindividuals list:")
        # print(subindividual)
        if len(subindividual) == 1:
            for strindividual in subindividual:
                check_subindividual(check_list,a,strindividual,rdf_about,individual_list)
        elif len(subindividual) > 1:
            for listindividual in subindividual:
                check_subindividual(check_list,a,listindividual,rdf_about,individual_list)
    
    
    
    
# for i in individual_list:
# while len(individual_list) != 0:
for a in range(len(individual_list)):
    i = individual_list[0]
    # print("individuaaaaa individuaaaaa individuaaaaa individuaaaaa")
    # print(i)
    check_subindividual(checked_list,a,i,rdf_about,individual_list)
    if len(individual_list) == 0:
        result = i
        break

print(result)