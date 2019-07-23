from pygments import highlight
from pygments.style import Style
from pygments.token import Token
from pygments.lexers import JavaLexer
from pygments.formatters import Terminal256Formatter
import pygments
import random
import time


class CodeReader:
    def __init__(self):
        rando_selecto = random.randint(1, 1)
        self.read_code(rando_selecto)


    def read_code(self, rand_int):
        count = 0
        line_array = []
        file_list = {
            1: ".\\files\code_01.txt",
            2: ".\\files\code_02.txt"
        }

        with open(file_list.get(rand_int)) as file:
            for line in file:
                line_array.append(line.rstrip())

        line_array_length = len(line_array)

        while count < line_array_length:
            rando_lino = random.randint(1, 20)
            rando_sleepo = random.randint(1, 10)
            rando_sleepo /= 100

            for n in range(1, rando_lino):
                if count == line_array_length:
                    break
                line = line_array[count].rstrip()
                pygmatized_line = highlight(line, JavaLexer(), Terminal256Formatter())
                print(pygmatized_line)
                time.sleep(rando_sleepo)
                count += 1
                