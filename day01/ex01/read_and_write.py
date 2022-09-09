def multiple_replace(old_data, replace_values):
    for i, j in replace_values.items():
        old_data = old_data.replace(i, j)
    return old_data

def read_and_write():
    with open('ds.csv', 'r') as f:
        old_data = f.read()

    replace_values = {'",': '"\t', ',"': '\t"', ',false': '\tfalse', 'false,': 'false\t', ',true': '\ttrue',
                      'true,': 'true\t'}

    new_data = multiple_replace(old_data, replace_values)
    with open('ds.tsv', 'w') as f:
        f.write(new_data)

if __name__=='__main__':
    read_and_write()
