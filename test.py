import os
from proxysetup.pattern_mathing import beacon_check
import glob
import time


pwd = os.getcwd()

print pwd
get_time = time.localtime(time.time())
time_now = "{0}_{1}_{2}_{3}_{4}_{5}".format(get_time.tm_mday,get_time.tm_mon,
                                                    get_time.tm_year,get_time.tm_hour,get_time.tm_min,get_time.tm_sec)

file_name = "test_sdk700_motog_{0}.log"
project_path= os.getcwd()
list_of_files = glob.glob('/Users/rmqa/Desktop/git/automation/proxysetup/logs/*')  # * means all if need specific format then *.csv
latest_file = max(list_of_files, key=os.path.getctime)
print 'lastestfile'
print latest_file

print 'project_path'
print project_path

filepath = project_path +'/proxysetup/logs/'+ latest_file

test = beacon_check(latest_file)
if len(test) == 0:
    print("No match found")
    # allure.attach('ClickURL-NotTracked', 'match not found', type=AttachmentType.TEXT)
else:
    print("Match found")
    for match in test:
        print(match + '\n')