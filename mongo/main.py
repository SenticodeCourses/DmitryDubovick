import mongo1 as mgc


def main():
    while True:
        command = input()
        if command in ['q', 'break', 'close', 'exit']:
            break

        elif len(command.split()) == 2:
            func, value = command.split()
            if func == 'name':
                mgc.update_name(value)
            elif func == 'age':
                mgc.update_age(value)
            elif func == 'number':
                mgc.update_phone(value)
            else:
                print('Wrong command!')

        else:
            print('Wrong command!')


if __name__ == '__main__':
    main()