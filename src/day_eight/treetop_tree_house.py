# # 30373 0
# # 25512 1
# # 65332 2
# # 33549 3
# # 35390 4
# # 01234

def treetop_tree_house(trees: list):
    total = 0
    left_an_right_col = (len(trees) - 2) *2 # left and right column, substract beginning and end, because it's included in lenght of row
    lastRow = len(trees) -1
    first_and_last_row = 0
    scenic_score = []
    for x in range(len(trees)):
        if x == 0 or x == lastRow:
            first_and_last_row += len(trees[x])
        else:
            tree = trees[x][1:lastRow]
            for i,t in enumerate(tree):
                left = trees[x][0:i+1]
                right = trees[x][i+2:]

                top,bottom = get_top_and_bottom(trees, i+1, x)
                t_as_number = int(t)

                if isLarger(t_as_number,left) or isLarger(t_as_number,right) or isLarger(t_as_number,top) or isLarger(t_as_number,bottom):
                    total += 1

                scenic_score.append(find_scenic_score(trees, i+1, x, t_as_number, left, right ))

    total += first_and_last_row + left_an_right_col
    scenic_score.sort()
    scenic_score.reverse()

    return (total, scenic_score[0])

def isLarger(singleTree: int, trees: str):
    for t in trees:
        if int(t) < singleTree:
            continue
        else: return False
    return True

def get_top_and_bottom(trees: list, colPosition: int, rowPosition: int):
    top = []
    bottom = []
    col_length = len(trees)

    for x in range(0, rowPosition):
        top.append(trees[x][colPosition])

    for x in range(rowPosition+1,col_length):
        bottom.append(trees[x][colPosition])

    return (''.join(top),''.join(bottom))

def find_scenic_score(trees: list, colPosition: int, rowPosition: int, singleTree: int, left_trees: str, right_trees: str):
    up = 0
    down = 0 
    left = 0
    right = 0
    col_length = len(trees)

    # up
    temp_up = []
    for x in range(0, rowPosition):
        temp_up.append(int(trees[x][colPosition]))

    temp_up.reverse()
    for t in temp_up:
        if singleTree > t:
            up += 1
        elif singleTree <= t:
            up += 1
            break
        
     

    # down
    temp_down = []
    for x in range(rowPosition+1,col_length):
        temp_down.append(int(trees[x][colPosition]))
    for t in temp_down:
        if singleTree > t:
            down += 1
        elif singleTree <= t:
            down += 1
            break
        
    # left
    reverses_left_trees = left_trees[::-1]
    for l in reverses_left_trees:
        if singleTree > int(l):
            left += 1
        elif singleTree <= int(l):
            left += 1
            break
    # right
    for r in right_trees:
        if singleTree > int(r):
            right += 1
        elif singleTree <= int(r):
            right += 1
            break
    
    return up * down * left * right


