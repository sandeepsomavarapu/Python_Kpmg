import re
matcher=re.finditer("\D","a7@ b9a zW")#sabdeep@gmail.com
for match in matcher:
    print(match.start(),"...",match.group())

#0  a
#3  b
