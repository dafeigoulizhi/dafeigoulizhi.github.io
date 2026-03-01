#!/bin/bash

set -e

git add .
git commit -m "update"
git push origin main

make html

scp -r build/html/* wufeim@masters12.cs.jhu.edu:~/public_html/knowledge/

ssh wufeim@masters12.cs.jhu.edu "chmod -R 755 ~/public_html/knowledge/"
