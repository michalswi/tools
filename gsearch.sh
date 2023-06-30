#!/usr/bin/env bash
set -u
query=$1
open https://www.google.com/search?q=${1}
# open https://www.google.com/search\?q\=${1}
