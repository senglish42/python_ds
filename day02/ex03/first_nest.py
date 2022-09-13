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
        return [int(first), int(second)]

    def file_reader(self, has_header=True):
        try:
            with open(self.file, 'r') as file:
                lines = file.readlines()
                lst = []
                for num, i in enumerate(lines, 1):
                    string = i.split(',')
                    self.check_length(len(string), num)
                    self.check_if_equal(string[0].strip(), string[1].strip(), num)
                    if num == 1 and has_header:
                        self.check_if_valid_header(string[0].strip(), string[1].strip())
                    else:
                        lst.append(self.check_if_valid_string(string[0].strip(), string[1].strip(), num))
                return lst
        except IOError:
            print(f"{self.file} : No such file or directory")
            quit(2)

    class Calculations:
        @staticmethod
        def counts(database):
            left, right = 0, 0
            for i in database:
                if i[0] != 0:
                    left += 1
                else:
                    right += 1
            return left, right

        @staticmethod
        def fractions(left, right):
            total = left + right
            p_left = left / total * 100
            p_right = right / total * 100
            return p_left, p_right


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Input a file name as one argument.")
        quit(1)
    data = Research(sys.argv[1]).file_reader()
    print(data)
    heads, tails = Research.Calculations.counts(data)
    print(f"{heads} {tails}")
    p_heads, p_tails = Research.Calculations.fractions(heads, tails)
    print(f"{p_heads} {p_tails}")
