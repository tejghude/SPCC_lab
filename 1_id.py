import re
s = input("Enter a string")
pattern = r'^[a-zA-Z_]\w*$'
if(re.search(pattern,s)):
    print("\n Valid")
else:
    print("\n Invalid")
