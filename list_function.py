def conca(list):
    final_list =""
    counter = 1
    for i in list:
        if counter < len(list):
            final_list = final_list + i + ","
        else:
            final_list = final_list + i
        counter += 1
    return final_list


list = ["a", "b", "c", "d", "e"]
print(conca(list))