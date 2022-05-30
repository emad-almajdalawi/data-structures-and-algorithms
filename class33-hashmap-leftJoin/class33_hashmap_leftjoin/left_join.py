
def left_join(left_table, right_table):
    """
    Left join two hashmaps
    Input: two hashmaps
    Output: a list of tuples
    """
    new_table = {}
    for key, value in left_table.items():
        if key in right_table:
            new_table[key] = value + ',' + right_table[key]
        else:
            new_table[key] = value + ',' + 'NULL'
    return new_table


def left_join_arr(left_table, right_table):
    """
    Left join two hashmaps
    Input: two hashmaps
    Output: a list of lists
    """
    if len(left_table) == 0:
        return []
    right_keys = []
    for row in right_table:
        right_keys.append(row[0])

    new_table = []
    for row in left_table:
        new_row = []
        new_value = ''
        if row[0] in right_keys:
            new_row.append(row[0])
            index = right_keys.index(row[0])
            new_value = row[1] + ',' + right_table[index][1]
            new_row.append(new_value)
            new_table.append(new_row)
        else:
            new_row.append(row[0])
            new_value = row[1] + ',' + 'NULL'
            new_row.append(new_value)
            new_table.append(new_row)
    return new_table



if __name__ == '__main__':
    left_table = {'a': '1', 'b': '2', 'c': '3'}
    right_table = {'a': '4', 'b': '5', 'd': '6'}

    left = [['a','1'],['b','2'],['c','3']]
    right = [['a','4'],['b','5'],['d','6']]

    print(left_join(left_table, right_table))
    print(left_join_arr(left, right))
