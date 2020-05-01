import re

#Return a list containing every occurrence of "wo":

txt = "The wolf found another wolf"
x = re.findall("wo", txt)
print(x)
