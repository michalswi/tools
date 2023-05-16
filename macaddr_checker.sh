#!/usr/bin/env bash

# macaddr vendor list [gist] - version from 15/05/2023

# accepted format (M - adapter manufacturer, S - device)
# MM:MM:MM:SS:SS:SS
# MM-MM-MM-SS-SS-SS

fileName=macaddr-vendor-list.txt
gistURL=https://gist.githubusercontent.com/michalswi/73eb4920862891a53e7decc840f82554/raw/7937380355c4974901cc7f8ea8426d3517c843cd
string=$1

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
