import os
import re

path = "Z:\Pictures\Sony Camera\ReformatNew"
regex = "^(?P<day>[0-3]\d)-(?P<month>[0-1]\d)-(?P<year>[1,2]\d\d\d)$"
os.chdir(path)
file_list = os.listdir()
for x in file_list:
    print(x)
    res = re.search(regex, x)
    if res != None:
        day = res.group('day')
        month = res.group('month')
        year = res.group('year')
        new = year+'-'+month+'-'+day
        print("renaming",x,"to",new)
        os.rename(x,new)


