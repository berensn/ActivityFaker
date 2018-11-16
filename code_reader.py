import random
import time


class CodeReader:
    def __init__(self):
        rando_selecto = random.randint(1, 2)
        self.read_code(rando_selecto)


    def read_code(self, rand_int):
        file_list = {
            1: ".\\files\code_01.txt",
            2: ".\\files\code_02.txt"
        }

        with open(file_list.get(rand_int)) as file:
            for line in file:
                print(line)
                time.sleep(0.035)
