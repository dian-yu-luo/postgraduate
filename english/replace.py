import re
import sys

f = ""
with open(sys.argv[1], encoding="utf-8") as file:
    f = file.read()

f = re.sub('(?<!\s)]]',"| ]]",f)
print(f)

file = open(sys.argv[1],mode="w", encoding="utf-8")
file.write(f)
