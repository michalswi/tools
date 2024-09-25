![](https://img.shields.io/github/issues/michalswi/tool)
![](https://img.shields.io/github/forks/michalswi/tool)
![](https://img.shields.io/github/stars/michalswi/tool)
![](https://img.shields.io/github/last-commit/michalswi/tool)

### \# macaddr_checker.sh

[gist source](https://gist.github.com/michalswi/e4a4dec65c8c0e4a597f5e2cab8fc44b) (version from **25/09/2024**)  
[IEEE source](https://standards-oui.ieee.org/oui/oui.txt)  

```
$ ./macaddr_checker.sh 6c:c7:ec:92:48:61
6CC7EC SAMSUNG ELECTRO-MECHANICS(THAILAND)
```

### \# gsearch.sh

```
$ ./gsearch.sh <what>
$ ./gsearch.sh <what>+<more>
$ ./gsearch.sh <what>+<more>+<more>
```

### \# screenshots

Make [screenshots](./screenshots/) of domains

```
$ cd screenshots

$ cat <domains_list_file>
<domain1>
<domain2>
<domain3>

$ ./genLst.py <domains_list_file>
"['<domain1>', '<domain2>', '<domain3>']"

$ ./makeScreenshot.py "['<domain1>', '<domain2>', '<domain3>']"
```
