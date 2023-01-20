
from yield_test_main_2 import y_main
from yield_test import test
import time

""" main """
def main():
    test_list = list(range(0, 5))

    for a in y_main(test_list):
        time.sleep(1)
        pass


if __name__ == "__main__":

    """ main program """
    main()






