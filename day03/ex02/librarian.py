import os


class UnconfiguredEnvironment(Exception):
    @staticmethod
    def err_msg():
        return "Virtual environment is not launched or name is not valid"


def run():
    try:
        if not os.getenv("VIRTUAL_ENV") or not os.getenv("VIRTUAL_ENV").endswith("ex02/senglish"):
            raise UnconfiguredEnvironment
        os.system("pip install pytest beautifulsoup4")
        os.system("pip freeze | tee requirements.txt")
        os.system("tar czf senglish.tar.gz senglish")
        os.system("rm -rf senglish")
    except UnconfiguredEnvironment as e:
        print(f"Error: {e.err_msg()}")


if __name__ == "__main__":
    run()
