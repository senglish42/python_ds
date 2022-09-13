class Must_read:
    try:
        print(open("../data.csv", 'r').read())
    except IOError:
        print("../data.csv: No such file or directory")
        quit(2)


if __name__ == '__main__':
    Must_read()
