def write_into_file(data):
    my_file = open('money.txt', 'a')
    my_file.write('%s : %s\n' % (data['name'], data['value']))
    my_file.close()

