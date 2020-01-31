import copy

index_list = []
flag = False

dtype = {}

def chgf(dict, inp, rep):
    for i in dict.keys():
        if i == inp:
            # rep.insert(0, dict[inp])
            rep = [rep, dict[i]]
            dict[i] = rep
            return
    for i in dict:
        if type(dict.get(i)) == type(dtype):
            chgf(dict.get(i), inp, rep)

def chgf_list1(dict, inp, rep):
    for i in dict.keys():
        if i == inp:
            tmp = dict[i]
            tmp.append(rep)
            dict[i] = tmp
            return
    for i in dict:
        if type(dict.get(i)) == type(dtype):
            chgf(dict.get(i), inp, rep)


def iteration(a,target):
    global index_list
    global flag
    for i in a:
        if i == str(target) and type(a).__name__ == "dict":
            # print("i")
            # print(index_result)
            flag = True
            index_list.append(i)
            break

        if i == str(target) and type(a).__name__ == "list":
            flag = True
            count = 0
            for x in a:
                if x == i:
                    index_list.append(count)
                    break
                count += 1
            count = 0
            break

        if type(i).__name__ == "dict":
            iteration(i,target)
        if type(a).__name__ == "dict":
            if type(a[i]).__name__ == "dict" or type(a[i]).__name__ == "list":
                iteration(a[i],target)
            elif type(a[i]).__name__ == "str" and a[i] == str(target):
                flag = True
                index_list.append(i)
                break
        if flag == True:
            if type(i).__name__ == "str" and type(a).__name__ != "list":
                index_list.append(i)
                break
            # if isinstance(a, list) == True and isinstance(i, dict) == True:
            if type(a).__name__ == "list" and type(i).__name__ == "dict":
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
    print("mainmainmain")
    print(main_dictionary)
    # a = main_dictionary
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
        # print("zzzzzzzzzzzzzzzzzzzz")
        # print(index_result_key)
        for i in range(len(index_result_key)):
            # print("//////")
            # print(b)
            if type(index_result_key[i]).__name__ == "str":
                tmp = tmp + "[\"" + index_result_key[i] + "\"]"

            if type(index_result_key[i]).__name__ == "int":
                tmp = tmp + "[" + str(index_result_key[i]) + "]"
            # tmp = tmp + "[\"" + index_result_key[::-1][i] + "\"]"

            b = b[index_result_key[i]]
            # print("........")
            # print(b)
            # print(main_dictionary)
        # print("sdsdad")
        # print(tmp)
        print(b)

        if type(b).__name__ == "str":
            if index_result_key[-1] == target:
                print("ttttttt")
                print(tmp)
                print(b)
                print(replace_item[target])

                chgf(main_dictionary, target, value)

                # exec('{0} = [{0},"{1}"]'.format(tmp, replace_item[target]))
                # tmp = [tmp,replace_item[target]]
                print("n1111111111111111111111111")
                print(main_dictionary)
                # exec('{0} = [{0},"{1}"]'.format(tmp, replace_item[target]))
            else:
                print("else")
                xxx = {target:replace_item[target]}
                # print("xxxx")
                # print(xxx)
                # print(tmp)
                exec('{0} = {1}'.format(tmp, xxx))

        if type(b).__name__ == "list":
            if index_result_key[-1] == target:
                # exec('{0}.append("{1}")'.format(tmp, replace_item[target]))
                chgf_list1(main_dictionary,target,value)
            else:
                xxx = {target:replace_item[target]}
                # print("xxxx")
                # print(xxx)
                # print(tmp)
                exec('{0} = {1}'.format(tmp, xxx))

        if type(b).__name__ == "dict":
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
            if type(index_result_key[i]).__name__ == "str":
                # print("str str str")
                tmp = tmp + "[\"" + index_result_key[i] + "\"]"
            if type(index_result_key[i]).__name__ == "int":
                # print("int int int ")
                tmp = tmp + "[" + str(index_result_key[i]) + "]"
            # print("bbbbbbbb")
            # print(b)

            b = b[index_result_key[i]]
        if index_result_key[-1] == target:
            # print("jdasjdsadn")
            # print(b)
            # print(tmp_value)
            if type(b).__name__ == "str":
                # chgf(main_dictionary,target,value)
                exec('{0} = ["{2}",{1}]'.format(tmp, tmp_value,b))
            if type(b).__name__ == "list":
                # chgf_list1(main_dictionary,target,value)
                exec('{0}.append({1})'.format(tmp, tmp_value))
            if type(b).__name__ == "dict":
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
#     a = {"1": {"2": {"3": {"4": {"5": {"6": {"7": {"8": {"9": {"10": "11"}}}}}}}}}, "13": {"18": "12"}}
#     a = {'19': '20','30': {'1': {'2': {'3': {'4': {'5': {'6': {'7': {'8': {'9': {'10': {'11': [{'13': {'18': '12'}}, '14']}}}}}}}}}}}}
#     a = {'11': [{'13': {'18': '12'}}, '14']}
#
#     # print(a)
#     # list = [{"11":"13"},{"11":"14"},{"19":"20"},{"30":"1"},{"18":"22"}]
#     # iteration(a, "11")
#     # print(index_list)
#     # iteration(a, "13")
#     # print(index_list)
#     list = [{"12": "220"}]
#     for i in list:
#         replace_item = i
#         print(replace_item)
#         replace(a,"a",replace_item)
#         print(a)
#         # iteration(a,"18")
#         # print(index_list)

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