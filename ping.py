from subprocess import Popen, PIPE
import argparse
import colorful
import math
import re


FAIL_FLAG = False
alive_count = 0
args = ''
avg = 0
avg_string = ''
color_palette = {
    'ip' : '#5888B8',
    'fail' : '#D33F3F',
    'semi' : '#FFA07A',    
    'success' : '#32CD32'
}
loss = 0
loss_string = ''
nonresponsive_count = 0
nonresponsive_list = {}
nonresponsive_server_count = 0
semi_responsive_count = 0
semi_responsive_list = {}
semi_responsive_server_count = 0

colorful.update_palette(color_palette)
parser = argparse.ArgumentParser(description='Ping an IPv4 address')
parser.add_argument('ip', metavar='IPv4 Address', type=str, nargs='+',
                   help='IPv4 address to ping')
args = parser.parse_args()

for x in range (4):
    ping = Popen(['ping', '-n', '1', args.ip[0]], stdout=PIPE)    
    loss_string = ''
    output = ping.communicate()[0]
    output = output.decode("utf-8")
    is_alive = ping.returncode

    if is_alive == 0:
        alive_count += 1
        avg_position_begin = output.find("Average = ")            
        avg_string = output[avg_position_begin:].strip().lower()
        avg += int(re.findall(r'\d+', avg_string)[0])
        ping = int(re.findall(r'\d+', avg_string)[0])
        print(f'{colorful.ip}{args.ip[0]}{colorful.reset} ping reponse: {colorful.success}average = {ping}ms{colorful.reset} with {colorful.success}{loss}% loss{colorful.reset}')
    else: 
        nonresponsive_count += 1
        loss_position_begin = output.find("Lost")
        loss_position_end = output.find("(")
        loss_string = output[loss_position_begin:loss_position_end]
        if "Ping request could not find host" in output:
            print(f'{colorful.fail}Ping request could not find host {colorful.ip}{args.ip[0]} {colorful.fail}Please check the name and try again{colorful.reset}')
            FAIL_FLAG = True
        elif "Request timed out" in output:
            print(f'{colorful.fail}Request timed out{colorful.reset}')
        else:
            loss += int(re.findall(r'\d+', loss_string)[0])

if alive_count == 0:
    nonresponsive_server_count += 1
    loss = 4

if alive_count != 4 and alive_count != 0:
    semi_responsive_server_count += 1

avg /= 4
loss = (loss / 4) * 100
avg = math.ceil(avg)
loss = math.ceil(loss)
print(f'\nPing Summary:')
if FAIL_FLAG == True:
    print(f'{colorful.fail}Ping request could not find host {colorful.ip}{args.ip[0]}{colorful.reset}')
elif loss == 100:
    print(f'{colorful.ip}{args.ip[0]}{colorful.reset} {colorful.fail}Ping request timed out. {loss}% loss{colorful.reset}')
elif loss < 100 and loss > 0:
    print(f'{colorful.ip}{args.ip[0]}{colorful.reset} ping reponse: {colorful.semi}average = {avg}ms{colorful.reset} with {colorful.semi}{loss}% loss{colorful.reset}')
else:
    print(f'{colorful.ip}{args.ip[0]}{colorful.reset} ping reponse: {colorful.success}average = {avg}ms{colorful.reset} with {colorful.success}{loss}% loss{colorful.reset}')
