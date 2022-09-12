import sys


def check(file):
    lst = []
    found = False
    for line in file:
        lst.append(line[:len(line) - 1])
        found = False
        if '@' in line:
            found = True
    if not found:
        quit(3)
    return lst


def run():
    if len(sys.argv) != 2:
        print("You should input a file path as one argument.")
        quit(1)
    lst = []
    name = "Name"
    surname = "Surname"
    email = "E-mail"
    try:
        file = open(sys.argv[1])
    except IOError:
        print(sys.argv[1], ": No such file or directory")
        quit(2)
    else:
        lst = check(file)
    with open("employees.tsv", "w") as file:
        file.write(f"{name}\t{surname}\t{email}\n")
        for email in lst:
            email_split = email.split('.')
            name = email_split[0].title()
            surname = email_split[1].split('@')[0].title()
            file.write(f"{name}\t{surname}\t{email}\n")


if __name__ == '__main__':
    run()
