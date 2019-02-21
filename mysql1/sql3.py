import re
str="helo hai? hai hello?"
x=re.findall(r"[a-z $?]+",str)
print(x)
