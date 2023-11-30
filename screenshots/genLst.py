#!/usr/bin/env python3

"""
$ cat <file>
<domain1>
<domain2>
<domain3>

$ ./genLst.py <file>
"['<domain1>', '<domain2>', '<domain3>']"
"""

import sys
import os

urls = []

if len(sys.argv) == 1:
    print("Missing file.")
    sys.exit(1)
elif os.path.isfile(sys.argv[1]):
    with open(sys.argv[1]) as f:
        for i in f.readlines():
            i = i.rstrip()  # removes \n
            urls.append(i)
    print(f"\"{urls}\"")
else:
    print("Are you using file?")
