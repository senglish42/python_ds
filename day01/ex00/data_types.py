def data_types():
    var_list = [1, 'one', 1.1, True, ['o', 'n', 'e'], {'one': 1, 'two': 2}, (1, 2, 3), {1, 2, 3}]
    list = []
    for number in range(8):
        list.append(type(var_list[number]).__name__)
    print('[' + ', '.join(list) + ']')

if __name__=='__main__':
    data_types()
