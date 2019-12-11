import copy

index_list = []
flag = False


def iteration(a,target):
    global index_list
    global flag
    for i in a:
        if i == str(target) and type(a) == dict:
            # print("i")
            # print(index_result)
            flag = True
            index_list.append(i)
            break

        if i == str(target) and type(a) == list:
            flag = True
            count = 0
            for x in a:
                if x == i:
                    index_list.append(count)
                    break
                count += 1
            count = 0
            break

        if type(i) == dict:
            iteration(i,target)
        if type(a) == dict:
            if type(a[i]) == dict or type(a[i]) == list:
                iteration(a[i],target)
            elif type(a[i]) == str and a[i] == str(target):
                flag = True
                index_list.append(i)
                break
        if flag == True:
            if type(i) == str and type(a) != list:
                index_list.append(i)
                break
            if type(a) == list and type(i) == dict:
                count = 0
                for x in a:
                    if x == i:
                        index_list.append(count)
                        break
                    count += 1
                count = 0
        if flag == True:
            break
    # print(index_list)

def replace(main_dictionary,dictionary_name,replace_item):
    global index_list
    global flag
    # exec('{0} = {1}'.format(dictionary_name,main_dictionary))
    a = main_dictionary
    b = copy.deepcopy(main_dictionary)
    for i in replace_item:
        target = i
        value = replace_item[i]

    iteration(main_dictionary, target)
    index_result_key = copy.deepcopy(index_list)
    # print("?????")
    # print(index_result_key)
    # print(index_list)
    # print(target)
    # print(value)
    flag = False
    index_list = []
    iteration(main_dictionary, value)
    index_result_value = copy.deepcopy(index_list)
    # print("""value""")
    # print(index_result_value)

    if len(index_result_key) != 0 and len(index_result_value) == 0:
        """
        key 在dictionary里
        value不在dictionary里
        """
        tmp = dictionary_name
        # print("zzzzzzzzzzzzzzzzzzzz")
        # print(index_result_key)
        index_result_key.reverse()
        for i in range(len(index_result_key)):
            # print("//////")
            # print(b)
            if type(index_result_key[i]) == str:
                tmp = tmp + "[\"" + index_result_key[i] + "\"]"

            if type(index_result_key[i]) == int:
                tmp = tmp + "[" + str(index_result_key[i]) + "]"
            # tmp = tmp + "[\"" + index_result_key[::-1][i] + "\"]"

            b = b[index_result_key[i]]
            # print("........")
            # print(b)
            # print(main_dictionary)
        # print("sdsdad")
        # print(tmp)
        # print(b)

        if type(b) == str:
            if index_result_key[-1] == target:
                exec('{0} = [{0},"{1}"]'.format(tmp, replace_item[target]))
            else:
                xxx = {target:replace_item[target]}
                # print("xxxx")
                # print(xxx)
                # print(tmp)
                exec('{0} = {1}'.format(tmp, xxx))

        if type(b) == list:
            if index_result_key[-1] == target:
                exec('{0}.append("{1}")'.format(tmp, replace_item[target]))
            else:
                xxx = {target:replace_item[target]}
                # print("xxxx")
                # print(xxx)
                # print(tmp)
                exec('{0} = {1}'.format(tmp, xxx))

        if type(b) == dict:
            if index_result_key[-1] == target:
                exec('{0} = [{0},"{1}"]'.format(tmp, replace_item[target]))
            else:
                xxx = {target:replace_item[target]}
                # print("xxxx")
                # print(xxx)
                # print(tmp)
                exec('{0} = {1}'.format(tmp, xxx))
        # print(main_dictionary)

    if len(index_result_key) == 0 and len(index_result_value) == 0:
        """
        key和value都不在dictionary里
        """
        main_dictionary[target] = value
        # print(main_dictionary)

    if len(index_result_key) != 0 and len(index_result_value) != 0:
        """
        key和value都在dictionary里
        """
        t1 = main_dictionary[value]
        t2 = {value:t1}
        tmp_value = copy.deepcopy(t2)

        tmp = dictionary_name
        index_result_key.reverse()
        for i in range(len(index_result_key)):
            # print("index_result_key[i]index_result_key[i]index_result_key[i]")
            # print(index_result_key[i])
            if type(index_result_key[i]) == str:
                # print("str str str")
                tmp = tmp + "[\"" + index_result_key[i] + "\"]"
            if type(index_result_key[i]) == int:
                # print("int int int ")
                tmp = tmp + "[" + str(index_result_key[i]) + "]"
            # print("bbbbbbbb")
            # print(b)

            b = b[index_result_key[i]]
        if index_result_key[-1] == target:
            # print("jdasjdsadn")
            # print(b)
            # print(tmp_value)
            if type(b) == str:
                exec('{0} = ["{2}",{1}]'.format(tmp, tmp_value,b))
            if type(b) == list:
                exec('{0}.append({1})'.format(tmp, tmp_value))
            if type(b) == dict:
                exec('{0} = [{2},{1}]'.format(tmp, tmp_value,b))

        else:
            xxx = {target:tmp_value}
            # print("tttttttttttttttttttttttttttttttttttt")
            # print(tmp)
            # print(xxx)
            exec('{0} = {1}'.format(tmp, xxx))
        del main_dictionary[value]
        # print(main_dictionary)
    if len(index_result_key) == 0 and len(index_result_value) != 0:
        """
        key不在dictionary里
        value在dictionary里
        """
        tmp = copy.deepcopy(main_dictionary[value])
        del main_dictionary[value]

        xxx = {value:tmp}
        main_dictionary[target] = xxx
        # print(main_dictionary)

    flag = False
    index_list = []

# if __name__ == '__main__':
    # a = {"1": {"2": {"3": {"4": {"5": {"6": {"7": {"8": {"9": {"10": "11"}}}}}}}}}, "13": {"18": "12"}}
#     # print(a)
#     # list = [{"11":"13"},{"11":"14"},{"19":"20"},{"30":"1"}]
#     # # list = [{"30":"1"}]
#     # for i in list:
#     #     replace_item = i
#     #     replace(a,"a",replace_item)


# a = {'1': ['2', {'3': {'4': [{'11': ['14', {'10': '12'}]}, {'5': ['13', {'15': {'7': {'8': '24'}}}]}]}}], '31': '32', '33': '34'}
# # #
# # # iteration(a,"24")
# # # print(index_list)
# # # # index_list = []
# # # # iteration(a,"7")
# # # # print(index_list)
# # print(a)
# replace_item = {"5":"33"}
# replace(a, "a",replace_item)
# print(a)

# a = {'individual_id3': {'individual_id4': 'individual_id5'},
#      'individual_id22': ['individual_id23', {'individual_id24': ['individual_id25', {'individual_id28': 'individual_id29'}, {'individual_id26': 'individual_id27'}]}],
#      'individual_id60': 'individual_id61',
#      'individual_id89': {'individual_id90': ['individual_id91', 'individual_id92']},
#      'individual_id83': ['individual_id85', 'individual_id87', 'individual_id84'],
#      'individual_id49': {'individual_id51': ['individual_id55', 'individual_id52', 'individual_id53']},
#      'individual_id12': 'individual_id13'}
#
# # iteration(a,"individual_id26")
# # print(index_list)
# a = {'individual_id0': [{'individual_id88': 'individual_id89'},
#                         'individual_id1',
#                         {'individual_id12': {'individual_id30': {'individual_id31': ['individual_id32', {'individual_id33': ['individual_id34', 'individual_id35', 'individual_id37']}]}}},
#                         'individual_id2',
#                         {'individual_id3': {'individual_id4': {'individual_id5': 'individual_id6'}}}, 'individual_id39', 'individual_id79', 'individual_id63']}
#
#
# replace_item = {"individual_id6":"individual_id13"}
# replace(a, "a",replace_item)
# iteration(a,"individual_id12")
# print(index_list)
# print(a)