import sys


def run():
    if len(sys.argv) != 2:
        print("You should input one name.")
        quit(1)
    try:
        with open('employees.tsv', 'r') as file:
            for n, line in enumerate(file, 0):
                line = line.rstrip('\n')
                if n > 0:
                    if line.split('\t')[2] == sys.argv[1]:
                        employee = line.split('\t')[0]
                        print(f"Dear {employee}, welcome to our team.\n"
                              f"We are sure that it will be a pleasure to work with you.\n"
                              f"That’s a precondition for the professionals that our company hires.")
                        quit(0)
    except IOError:
        print("employees.tsv : No such file or directory")
        quit(2)


if __name__ == '__main__':
    run()
