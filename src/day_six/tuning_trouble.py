def tuning_trouble_part_one(buffer):
    length = len(buffer)
    for x in range(length):
        end_marker = x + 4
        marker = buffer[x:end_marker]
        if len(set(marker)) == len(marker):
            return end_marker

def tuning_trouble_part_two(buffer):
    length = len(buffer)
    for x in range(length):
        end_marker = x + 14
        marker = buffer[x:end_marker]
        if len(set(marker)) == len(marker):
            return end_marker

