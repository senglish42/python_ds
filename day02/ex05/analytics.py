from random import randint


class Research:
    def __init__(self, file):
        self.file = file
        self.valid = ('0', '1')

    @staticmethod
    def is_digit(string):
        if string.isdigit():
            return True
        else:
            try:
                float(string)
                return True
            except ValueError:
                return False

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
        if Research.is_digit(first) is True or Research.is_digit(second) is True:
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
        def __init__(self, database):
            self.data = database

        def counts(self):
            left, right = 0, 0
            for i in self.data:
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

    class Analytics(Calculations):
        @staticmethod
        def predict_random(num):
            lst = []
            for i in range(num):
                r1 = randint(0, 1)
                if r1 == 0:
                    r2 = 1
                else:
                    r2 = 0
                lst.append([r1, r2])
            return lst

        def predict_last(self):
            return self.data[len(self.data) - 1]

        def save_file(self, database, name, extension):
            with open(f"{name}.{extension}", 'w') as file:
                count = len(self.data)
                heads, tails = self.counts()
                p_heads, p_tails = self.fractions(heads, tails)
                new_heads, new_tails = database.counts()
                from config import template
                template = template.replace("%count%", f'{count}')
                template = template.replace("%tails%", f'{tails}')
                template = template.replace("%heads%", f'{heads}')
                template = template.replace("%p_heads%", f'{p_heads:.2f}')
                template = template.replace("%p_tails%", f'{p_tails:.2f}')
                template = template.replace("%new_heads%", f'{new_heads}')
                template = template.replace("%new_tails%", f'{new_tails}')
                file.write(template)
