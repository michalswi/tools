#!/usr/bin/env bash

# macaddr vendor list [gist] - version from 25/09/2024

# accepted format (M - adapter manufacturer, S - device)
# MM:MM:MM:SS:SS:SS
# MM-MM-MM-SS-SS-SS

fileName=macaddr-vendor-list.txt
gistURL=https://gist.githubusercontent.com/michalswi/e4a4dec65c8c0e4a597f5e2cab8fc44b/raw/457a34368bbbd6920cd4028d40e0288854ec6447/
string=$1

if [ -z $1 ]; then
    echo "missing macaddr"
    exit 1
fi

if ! [ -f "/tmp/$fileName" ]; then
    wget -q \
    ${gistURL}/${fileName} \
    -P /tmp
fi

if [[ $string == *"-"* ]]; then
    base16=`echo $1 | awk -F- '{print $1$2$3}'`
    record=`grep -i $base16 /tmp/$fileName`
elif [[ $string == *":"* ]]; then
    base16=`echo $1 | awk -F: '{print $1$2$3}'`
    record=`grep -i $base16 /tmp/$fileName`
else
    echo "wrong macaddr format:" $1
    exit 1
fi

if [ ${#record} -ge 1 ]; then
    echo $record
else
    echo "no record found for:" $1
fi
