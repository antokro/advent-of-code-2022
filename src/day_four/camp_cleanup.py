def camp_cleanup(sections):
    counter_part_1 = 0
    counter_part_2 = 0

    for x in range(len(sections)):
        item = sections[x]
        team_one = item.split(',')[0]
        team_two = item.split(',')[1]

        team_one_from = int(team_one.split('-')[0])
        team_one_to = int(team_one.split('-')[1])

        team_two_from = int(team_two.split('-')[0])
        team_two_to = int(team_two.split('-')[1])

        range_team_one = range(team_one_from,team_one_to+1)
        range_team_two = range(team_two_from,team_two_to+1)

    #PART 1
        if set(range_team_one).issubset(range_team_two) or set(range_team_two).issubset(range_team_one):
            counter_part_1 = counter_part_1 +1 
        
    #PART 2
        if team_one_from <= team_two_to and team_two_from <= team_one_to:
            counter_part_2 = counter_part_2 +1
            


    print("Sections fully contained by the other: ",counter_part_1)
    print("Sections that overlap: ", counter_part_2)

    return (counter_part_1, counter_part_2)