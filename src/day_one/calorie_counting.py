def calorie_counting(list:list):
    for x in range(len(list)):
        if list[x] == '':
            list[x] = '#'
        else: 
            list[x] = list[x]

    result = split_to_sublists(list,'#')

    for x in range(len(result)):
        total = 0
        for calorie in result[x]:
            total += calorie
        result[x] = total

    result.sort()
    result.reverse()

    top_elf = result[0]
    top_three_elf = result[0:1][0] + result[1:2][0] + result[2:3][0]

    return (top_elf,top_three_elf)

def split_to_sublists(list:list, delimiter:str):
    temp = []
    final = []
    for item in list:
        if item != delimiter:
            temp.append(int(item))
        else:
            final.append(temp)
            temp = []
    final.append(temp)
    return final 
