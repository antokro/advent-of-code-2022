def tuning_trouble(buffer: list, sequence: int):
    length = len(buffer)
    for x in range(length):
        end_marker = x + sequence
        marker = buffer[x:end_marker]
        if len(set(marker)) == len(marker):
            return end_marker

