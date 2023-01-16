import re 
count=0
#pattern=re.compile("ab")
matcher=re.finditer("ab","abaababa")

for match in matcher:
    count+=1
    print(match.start(),"...",match.end(),"....",match.group())
print(count)

#0...2....ab
#3...5....ab
#5...7....ab