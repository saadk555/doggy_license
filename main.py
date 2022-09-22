import re
from scrape import find


file = input(r'Please enter the path of the file with name: ')

with open(file,'r') as lines:
    for line in lines.readlines():
        rs = re.search(r"^(import|from) ([\w\-_]+)",line) 
        module = rs.group(2)
        find(module)
        
