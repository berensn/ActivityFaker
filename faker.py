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
        #self.progress_bar()
        #self.progress()
        #self.process_picker(1)
        cr()

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

    def process_picker(self, call_num):
        count = 1
        while count <= call_num:
            rando_selecto = random.randint(1, 11)
            switch = {
                1: fp.ping(self),
                2: fp.ls(self),
                3: fp.nbtstat(self),
                4: fp.netstat(self),
                5: fp.processes(self),
                6: fp.tasklist(self),
                7: fp.route(self),
                8: fp.system_info(self),
                9: fp.tracert(self),
                10: fp.nslookup(self),
                11: fp.ipconfig(self)
            }
            switch.get(rando_selecto)
            #execution = switch.get(rando_selecto)
            #execution()
            count += 1

if __name__ == '__main__':
    Faker()
