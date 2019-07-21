import subprocess
import random
import time


class FakeSubprocess(object):
    def selector(self, subprocess):
        func_name = subprocess
        func = getattr(self, func_name, lambda: 'Invalid')
        return func()

    def ls(self):
        print("\n")
        print("ls")
        return subprocess.run('ls')

    def ping(self):
        print("ping")
        subprocess.run(['ping', "8.8.8.8"])

    def nbtstat(self):
        print("nbtstat")
        result = subprocess.run('nbtstat -c', stdout=subprocess.PIPE).stdout.decode('utf-8')
        self.slow_output(result)

    def netstat(self):
        print("netstat")
        result = subprocess.run('netstat', stdout=subprocess.PIPE).stdout.decode('utf-8')
        self.slow_output(result)

    def processes(self):
        print("processes")
        subprocess.run('ps -a')

    def tasklist(self):
        print("tasklist")
        result = subprocess.run('tasklist', stdout=subprocess.PIPE).stdout.decode('utf-8')
        self.slow_output(result)

    def route(self):
        print("route")
        result = subprocess.run('route PRINT', stdout=subprocess.PIPE).stdout.decode('utf-8')
        self.slow_output(result)

    def system_info(self):
        print("system info")
        result = subprocess.run('systeminfo', stdout=subprocess.PIPE).stdout.decode('utf-8')
        self.slow_output(result)

    def tracert(self):
        print("tracert")
        subprocess.run('tracert 8.8.8.8')

    def nslookup(self):
        print("nslookup")
        subprocess.run('nslookup www.google.com')

    def ipconfig(self):
        print("ipconfig")
        result = subprocess.run('ipconfig', stdout=subprocess.PIPE).stdout.decode('utf-8')
        self.slow_output(result)

    def slow_output(self, result):
        data_line = []
        for i in result:
            data_line.append(i)
            if i == '\n':
                joined = ''.join(data_line)
                print(joined[:-2])
                data_line = []
                rando_sleepo = random.randint(1, 10)
                rando_sleepo /= 50
                time.sleep(rando_sleepo)