#!/bin/bash
while true
do
 kill -9 1337
 sleep 30
 python36 createdbfile.py
 cd quotafile
 python -m SimpleHTTPServer 1337 &
 cd ..
done
