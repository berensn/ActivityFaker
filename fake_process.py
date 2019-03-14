import subprocess
#import ping  


class FakeSubprocess:
    def ls(self):
        print("\n")
        print("ls")
        return subprocess.call('ls')

    def ping(self):
        print("ping")
        subprocess.call(['ping', "8.8.8.8"])

    def nbtstat(self):
        print("nbtstat")
        subprocess.call('nbtstat -c')

    def netstat(self):
        print("netstat")
        subprocess.call('netstat')

    def processes(self):
        print("processes")
        subprocess.call('ps -a')

    def tasklist(self):
        print("tasklist")
        subprocess.call('tasklist')

    def route(self):
        print("route")
        subprocess.call('route PRINT')

    def system_info(self):
        print("system info")
        subprocess.call('systeminfo')

    def tracert(self):
        print("tracert")
        subprocess.call('tracert 8.8.8.8')

    def nslookup(self):
        print("nslookup")
        subprocess.call('nslookup www.google.com')

    def ipconfig(self):
        print("ipconfig")
        subprocess.call('ipconfig')
