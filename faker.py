from code_reader import CodeReader as cr
from progress.bar import Bar
from fake_process import FakeSubprocess as fp
import random
import sys
import time


class Faker:
    def __init__(self):
        file_dir = "/src"
        self.faker_controller()

    def faker_controller(self):
        print(f'Faker Controller')
        #selection_list_selector = random.randint(1, 11)
        selection_list_selector = 1
        selection_list = {
            1: self.process_picker()
        }
        #self.progress_bar()
        #self.progress()
        #cr()
        selection_list.get(selection_list_selector)

    def progress(self):
        def bar(count, total, status=''):
            bar_len = 60
            filled_len = int(round(bar_len * count / float(total)))

            percents = round(100.0 * count / float(total), 1)
            progress_bar = '■' * filled_len + ' ' * (bar_len - filled_len)

            sys.stdout.write(f'[{progress_bar}] {percents}% ...{status}\r')

            sys.stdout.flush()

        rand_int = random.randint(1, 1)
        if rand_int == 1:
            bar_length = 100
            i = 0
            while i <= bar_length:
                bar(i, bar_length, status="Hashing file")
                time.sleep(0.005)
                i += 1

    def progress_bar(self):
        bar = Bar('Loading', fill='■', suffix='%(percent)d%%')
        for i in range(100):
            time.sleep(0.01)
            bar.next()
        bar.finish()

    def process_picker(self):
        #call_num = random.randint(1, 11)
        call_num = 3
        count = 0
        process_list = {
            1: "ping",
            2: "ls",
            3: "nbtstat",
            4: "netstat",
            5: "processes",
            6: "tasklist",
            7: "route",
            8: "system_info",
            9: "tracert",
            10: "nslookup",
            11: "ipconfig"
        }
        selectorama = fp()
        while count < call_num:
            rando_selecto = random.randint(1, 11)
            selectorama.selector(process_list.get(rando_selecto))
            count += 1
            print(count)
        #self.faker_controller()

if __name__ == '__main__':
    Faker()
