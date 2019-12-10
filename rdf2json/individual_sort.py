import copy

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
        if type(i) == str:
            pass
        else:
            if type(a[i]) == dict or type(a[i]) == list:
                iteration(a[i],target)
            elif type(a[i]) == str and a[i] == str(target):
                flag = True
                index_list.append(i)
                break
        if flag is True:
            index_list.append(i)
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
    print(index_result_key)
    print(index_list)

    flag = False
    index_list = []
    # print("index_list")
    # print(index_list)
    iteration(main_dictionary, value)
    index_result_value = copy.deepcopy(index_list)
    print("""value""")
    print(index_result_value)

    if len(index_result_key) != 0 and len(index_result_value) == 0:
        """
        key 在dictionary里
        value不在dictionary里
        """
        tmp = dictionary_name
        for i in range(len(index_result_key)):
            tmp = tmp + "[\"" + index_result_key[::-1][i] + "\"]"
            b = b[index_result_key[::-1][i]]
        print("sdsdad")
        print(tmp)

        if type(b) == str:
            if index_result_key[0] == target:
                exec('{0} = [{0},"{1}"]'.format(tmp, replace_item[target]))
            else:
                xxx = {target:replace_item[target]}
                print("xxxx")
                print(xxx)
                print(tmp)
                exec('{0} = {1}'.format(tmp, xxx))

        if type(b) == list:
            if index_result_key[0] == target:
                exec('{0}.append("{1}")'.format(tmp, replace_item[target]))
            else:
                xxx = {target:replace_item[target]}
                print("xxxx")
                print(xxx)
                print(tmp)
                exec('{0} = {1}'.format(tmp, xxx))
        print(main_dictionary)

    if len(index_result_key) == 0 and len(index_result_value) == 0:
        """
        key和value都不在dictionary里
        """
        main_dictionary[target] = value
        print(main_dictionary)

    if len(index_result_key) != 0 and len(index_result_value) != 0:
        """
        key和value都在dictionary里
        """
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
        print(main_dictionary)
    if len(index_result_key) == 0 and len(index_result_value) != 0:
        """
        key不在dictionary里
        value在dictionary里
        """
        tmp = copy.deepcopy(main_dictionary[value])
        del main_dictionary[value]

        xxx = {value:tmp}
        main_dictionary[target] = xxx
        print(main_dictionary)

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

a = {}
list1 = [{"11": "13"}, {"11": "15"},{"11": "14"}, {"19": "20"}, {"30": "11"}]
# list = [{"30":"1"}]
for i in list1:
    replace_item = i
    replace(a, "a", replace_item)
print(a)
