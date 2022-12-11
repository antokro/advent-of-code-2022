def split_to_sublists(list:list, delimiter:str):
    for x in range(len(list)):
        if list[x] == '':
            list[x] = delimiter
        else: 
            list[x] = list[x]

    temp = []
    final = []
    for item in list:
        if item != delimiter:
            temp.append(item)
        else:
            final.append(temp)
            temp = []
    final.append(temp)
    return final