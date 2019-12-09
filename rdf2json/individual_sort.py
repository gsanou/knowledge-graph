import copy

a = {"1":{"2":{"3":{"4":{"5":{"6":{"7":{"8":{"9":{"10":"11"}}}}}}}}},"13":{"18":"12"}}
b = {"1":"2","3":"4","5":"6"}
index_list = []
flag = False

def iteration(a,target):
    global index_list
    global flag
    for i in a:
        if i == str(target):
            # print("i")
            # print(index_result)
            flag = True
            index_list.append(i)
            break
        else:
            if type(a[i]) == dict or type(a[i]) == list:
                iteration(a[i],target)
            elif type(a[i]) == str and a[i] == str(target):
                flag = True
                index_list.append(i)
                break
        if flag == True:
            index_list.append(i)
            break
    # print(index_list)

# replace_item = {"11":"aaa"}
# for i in replace_item:
#     target = i
# print(target)
# iteration(a,target)
# index_result = index_list
# print(index_result)
#
# tmp = "a"
# for i in range(len(index_result)):
#     tmp = tmp + "[\"" + index_result[::-1][i] + "\"]"
#
# if index_result[0] == target:
#     exec('{0} = [{0},"{1}"]'.format(tmp,replace_item[target]))
# else:
#     exec('{0} = "{1}"'.format(tmp, replace_item[target]))
#
#
# print(a)

def replace(main_dictionary,dictionary_name,replace_item):
    global index_list
    global flag
    for i in replace_item:
        target = i
        value = replace_item[i]
        print("ssssss")
        print(target)
        print(value)

    iteration(main_dictionary, target)
    index_result_key = copy.deepcopy(index_list)
    print(index_result_key)
    print(index_list)

    flag = False
    index_list = []
    # print("index_list")
    # print(index_list)
    iteration(main_dictionary, value)
    index_result_value = copy.deepcopy(index_list)
    # print("""value""")
    # print(index_result_value)

    if len(index_result_key) != 0 and len(index_result_value) == 0:
        tmp = dictionary_name
        for i in range(len(index_result_key)):
            tmp = tmp + "[\"" + index_result_key[::-1][i] + "\"]"

        if index_result_key[0] == target:
            exec('{0} = [{0},"{1}"]'.format(tmp, replace_item[target]))
        else:
            xxx = {target:replace_item[target]}
            exec('{0} = {1}'.format(tmp, xxx))

        print(a)

    if len(index_result_key) == 0 and len(index_result_value) == 0:
        main_dictionary[target] = value
        print(a)

    if len(index_result_key) != 0 and len(index_result_value) != 0:
        t1 = main_dictionary[value]
        t2 = {value:t1}
        tmp_value = copy.deepcopy(t2)

        del main_dictionary[value]

        tmp = dictionary_name
        for i in range(len(index_result_key)):
            tmp = tmp + "[\"" + index_result_key[::-1][i] + "\"]"

        if index_result_key[0] == target:
            exec('{0} = [{0},"{1}"]'.format(tmp, tmp_value))
        else:
            xxx = {target:tmp_value}
            exec('{0} = {1}'.format(tmp, xxx))
        print(a)

if __name__ == '__main__':
    print(a)
    replace_item = {"11":"13"}
    replace(a,"a",replace_item)
    # a["1"]["2"]["3"]["4"]["5"]["6"]["7"]["8"]["9"]["10"] = {"11":"13"}
    # print(a)
