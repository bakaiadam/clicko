import fileinput


first_line = True
actual_map = list()
actual_ink_map = list()
island_sets = list()


def flow_ink(i, k, color_index, color_name):
    if i < 0 or i >= len(actual_map):
        return
    if k < 0 or k >=len(actual_map[0]):
        return
    if actual_map[i][k] != color_name:
        return
    drop_ink(i, k, color_index)

def drop_ink(i, k, color_index):
    if actual_ink_map[i][k] != 0:
        return 0
    actual_ink_map[i][k] = color_index
    if len(island_sets) == color_index - 1:
        island_sets.append(set())
    island_sets[color_index - 1].add((i, k))
    flow_ink(i + 1, k, color_index, actual_map[i][k])
    flow_ink(i - 1, k, color_index, actual_map[i][k])
    flow_ink(i, k + 1, color_index, actual_map[i][k])
    flow_ink(i, k - 1, color_index, actual_map[i][k])

    return 1

temp_row_i = 0
for line in fileinput.input():
    if first_line:
        col_num = int(line.split()[1])
        row_num = int(line.split()[0])
        color_num = int(line.split()[2])

        #print(col_num)
        #print(row_num)
        #print(color_num)

        first_line = False
        actual_map = [[0 for x in range(col_num)] for x in range(row_num)]
        actual_ink_map = [[0 for x in range(col_num)] for x in range(row_num)]
        continue
    for k in range(col_num):
        actual_map[temp_row_i][k] = line[k]
    temp_row_i = temp_row_i + 1

color_index = 1
for i in range(len(actual_map)):
    for k in range(len(actual_map[i])):
        color_index = color_index + drop_ink(i,k, color_index)
        #print(actual_ink_map[i][k], end="")
    #print("")

max_len = 0
click_to = (0,0)
for x in island_sets:
    if max_len <= len(x) and actual_map[list(x)[0][0]][list(x)[0][1]] != "-":
        max_len = len(x)
        click_to = list(x)[0]
    #print(x)

print(str(click_to[0]) + " " + str(click_to[1]))