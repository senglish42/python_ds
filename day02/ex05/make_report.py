import sys
from analytics import Research
from config import num_of_steps


def run():
    if len(sys.argv) != 2:
        print("Input a file name as one argument.")
        quit(1)
    data = Research(sys.argv[1]).file_reader()
    analytics = Research.Analytics(data)
    new_data = analytics.predict_random(num_of_steps)
    new_analytics = Research.Analytics(new_data)
    analytics.save_file(new_analytics, "prognosis", "txt")


if __name__ == '__main__':
    run()
