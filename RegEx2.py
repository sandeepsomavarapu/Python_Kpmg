import re 
count =0
matcher=re.finditer("a{1,}","abaabaaab")
for match in matcher:
	print(match.start(),"...",match.group())

#1..7  
#3..@

#sandeep=[abc]