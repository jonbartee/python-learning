##grabs linkedin urls from raw html

import re

output = open('SubURLs.txt', 'w')

with open('./URLraw.txt', 'r', encoding='UTF8') as f:
    for line in f:
        if re.search("/in/", line):
            sep = '/'
            stripped = line.split(sep)
            output.write('https://www.linkedin.com/' + stripped[1] + '/' + stripped[2] + '/' + '\n')

f.close()