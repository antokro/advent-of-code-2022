value_dictionary = {'a':1,
'b':2,
'c':3,
'd':4,
'e':5,
'f':6,
'g':7,
'h':8,
'i':9,
'j':10,
'k':11,
'l':12,
'm':13,
'n':14,
'o':15,
'p':16,
'q':17,
'r':18,
's':19,
't':20,
'u':21,
'v':22,
'w':23,
'x':24,
'y':25,
'z':26,
'A':27,
'B':28,
'C':29,
'D':30,
'E':31,
'F':32,
'G':33,
'H':34,
'I':35,
'J':36,
'K':37,
'L':38,
'M':39,
'N':40,
'O':41,
'P':42,
'Q':43,
'R':44,
'S':45,
'T':46,
'U':47,
'V':48,
'W':49,
'X':50,
'Y':51,
'Z':52}

def divide_chunks(l, n):
    for i in range(0, len(l), n):
         yield l[i:i + n]

def rucksack_reorganisation(rucksacks):
    sliced_rucksacks = []
    priorities = 0

    sliced_items = []

    # PART 1
    # slice rucksacks
    for rucksack in rucksacks:
        length = round(len(rucksack) / 2)
        sliced_rucksacks.append([rucksack[:length], rucksack[length:]]) 

    for sliced_rucksack in sliced_rucksacks:
        sliced_items.clear()

        for items in sliced_rucksack:
            splitted_items = [items[i:i+1] for i in range(0, len(items), 1)]
            sliced_items.append(splitted_items)

        for sliced_item in sliced_items[0]:
            if sliced_item in sliced_items[1]:
                priorities = priorities + value_dictionary[sliced_item]
                break

    # PART 2
    priorities_part_two = 0 
    grouped_rucksacks = list(divide_chunks(rucksacks, 3))


    for grouped_rucksack in grouped_rucksacks:
        grouped_splitted_rucksacks = []
        for rucksack in grouped_rucksack:
            splitted_rucksack = [rucksack[i:i+1] for i in range(0, len(rucksack), 1)]
            grouped_splitted_rucksacks.append(splitted_rucksack)
                
        for item in grouped_splitted_rucksacks[0]:
            if item in grouped_splitted_rucksacks[1]:
                if item in grouped_splitted_rucksacks[2]:
                    priorities_part_two = priorities_part_two + value_dictionary[item]
                    break

    return (priorities, priorities_part_two)







