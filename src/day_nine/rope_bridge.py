# R = right
# U = up
# L = left
# D = down

# from https://github.com/juanplopes/advent-of-code-2022/blob/main/day09.py
def rope_bridge(moves, knots):
    formatted_moves = []
    for x in range(len(moves)):
        splitted = moves[x].split()
        formatted_moves.append((splitted[0],int(splitted[1])))
    
    print(formatted_moves)
    X = [[0, 0] for _ in range(knots)]
    visited = set()
    for a, b in formatted_moves:
        for _ in range(int(b)):
            X[0][0] += {'R': 1, 'L': -1}.get(a, 0)
            X[0][1] += {'D': 1, 'U': -1}.get(a, 0)
            for j in range(1, knots):
                if (X[j-1][0]-X[j][0])**2 + (X[j-1][1]-X[j][1])**2 > 2:
                    X[j][0] += max(-1, min(1, X[j-1][0] - X[j][0]))
                    X[j][1] += max(-1, min(1, X[j-1][1] - X[j][1]))
            visited.add(tuple(X[-1]))
    return len(visited)

# def rope_bridge(rope:list):
    visited = set()
    visited.add((0,0))
    for x in range(len(rope)):
        splitted = rope[x].split()
        rope[x] = (splitted[0],int(splitted[1]))

    # (row, column)
    last_position = (0,0)
    for x in rope:
        (direction, length) = x
        if direction == 'R':
            for l in range(1,length):
                visited.add((last_position[0],last_position[1] + l))

            last_position = (last_position[0],last_position[1] + length)
        if direction == 'L':
            for l in range(length):
                visited.add((last_position[0],last_position[1] - l+1))

            last_position = (last_position[0],last_position[1] - length)
        if direction == 'U':
            for l in range(length):
                visited.add((last_position[0] + l,last_position[1]))
            
            last_position = (last_position[0] + length,last_position[1])
        if direction == 'D':
            for l in range(length):
                visited.add((last_position[0] - l,last_position[1]))
            
            last_position = (last_position[0] - length,last_position[1])
    #     print(x)
    #     print('last position', last_position)
        
    # print(visited)
    # print(len(visited))
    return (len(visited))

