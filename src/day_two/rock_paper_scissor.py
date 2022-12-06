# /*
#  * (1 for Rock, 2 for Paper, and 3 for Scissors)
#  * plus the score for the outcome of the round
#  *(0 if you lost, 3 if the round was a draw, and 6 if you won).

#  *
#  * Opponent: A for Rock, B for Paper, and C for Scissors
#  * Me: X for Rock, Y for Paper, and Z for Scissors.
#  */

points = { 'A': 1, 'B': 2, 'C': 3, 'X': 1, 'Y': 2, 'Z': 3  }

def rock_paper_scissor_part_one(list:list):

    total = 0
    for x in range(len(list)):
        list[x] = list[x].split(' ')

    for r in list:
        if (r[0] == 'A' and r[1] == 'X') or (r[0] == 'B' and r[1] == 'Y') or (r[0] == 'C' and r[1] == 'Z'):
            total += 3 + points[r[1]]
        elif (r[0] == 'A' and r[1] == 'Z') or (r[0] == 'B' and r[1] == 'X') or (r[0] == 'C' and r[1] == 'Y'):
            total += points[r[1]]
        else:
            total += 6 + points[r[1]]

    return (total)


# /**
#  * X means you need to lose,
#  * Y means you need to end the round in a draw, and Z means you need to win
#  *
#  * Opponent: A for Rock, B for Paper, and C for Scissors.
#  */

def rock_paper_scissor_part_two(list:list):
    total = 0
    for x in range(len(list)):
        list[x] = list[x].split(' ')

    for r in list:
        if r[1] == 'X':
            if r[0] == 'A':
                my_choice = 'Z'
            elif r[0] == 'B':
                my_choice = 'X'
            else: 
                my_choice = 'Y'
            total += points[my_choice]
        elif r[1] == 'Y':
            if r[0] == 'A':
                my_choice = 'X'
            elif r[0] == 'B':
                my_choice = 'Y'
            else: 
                my_choice = 'Z'
            total += 3 + points[my_choice]
        else:
            if r[0] == 'A':
                my_choice = 'Y'
            elif r[0] == 'B':
                my_choice = 'Z'
            else: 
                my_choice = 'X'
            total += 6 + points[my_choice]

    return (total)
