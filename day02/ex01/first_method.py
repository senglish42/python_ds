class Research:
    @staticmethod
    def file_reader():
        try:
            return open("../data.csv", 'r').read()
        except IOError:
            print("../data.csv: No such file or directory")
            quit(2)


if __name__ == '__main__':
    print(Research().file_reader())
