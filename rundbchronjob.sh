#!/bin/bash
kill -9 1337
python36 createdbfile.py
cd quotafile
python -m SimpleHTTPServer 1337 &
cd ..
