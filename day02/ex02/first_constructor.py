import sys


def is_digit(string):
    if string.isdigit():
        return True
    else:
        try:
            float(string)
            return True
        except ValueError:
            return False


class Research:
    def __init__(self, file):
        self.file = file
        self.valid = ('0', '1')

    def check_length(self, num, string_num):
        if num != 2:
            raise ValueError(f"\tString #{string_num} content is not valid.\n"
                             f"Reminder:\tEach string of {self.file} file should contain two values"
                             " delimited by comma.")

    def check_if_equal(self, first, second, string_num):
        if first == second:
            raise ValueError(f"\tString #{string_num} values are the same.\n"
                             f"Reminder:\tEach string of {self.file} file should contain not the same values.")

    def check_if_valid_header(self, first, second):
        if is_digit(first) is True or is_digit(second) is True:
            raise ValueError(f"Error: File {self.file} header should not contain a number.")

    def check_if_valid_string(self, first, second, string_num):
        if first not in self.valid or second not in self.valid:
            raise ValueError(f"\tAt least one value of #{string_num} string is not valid.\n"
                             f"Reminder:\tString #{string_num} of {self.file} file should only contain values: "
                             f"{self.valid[0]} and {self.valid[1]}.")

    def file_reader(self):
        try:
            with open(self.file, 'r') as file:
                lines = file.readlines()
                for num, i in enumerate(lines, 1):
                    string = i.split(',')
                    self.check_length(len(string), num)
                    self.check_if_equal(string[0].strip(), string[1].strip(), num)
                    if num == 1:
                        self.check_if_valid_header(string[0].strip(), string[1].strip())
                    else:
                        self.check_if_valid_string(string[0].strip(), string[1].strip(), num)
                file.seek(0)
                return file.read()
        except IOError:
            print(self.file, ": No such file or directory")
            quit(2)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Input a file name as one argument.")
        quit(1)
    print(Research(sys.argv[1]).file_reader())
