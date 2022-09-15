import os


# Launching virtual environment using bash:
# virtualenv -p python3 senglish

# Launching virtual environment using bash:
# source senglish/bin/activate


def run():
    print("Your current virtual env is", os.getenv("VIRTUAL_ENV"))


if __name__ == '__main__':
    run()
