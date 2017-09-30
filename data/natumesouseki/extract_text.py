#!/usr/bin/python
# -*- coding: utf-8 -*-    

import sys
import re

# f = open(sys.argv[1], "r")

#line = f.readline()

line = sys.stdin.readline()
# ヘッダーの削除(最初のHL)
while line:
    # ヘッダーの削除
    if re.search('-'*10, line):
        break
    line = sys.stdin.readline()

line = sys.stdin.readline()
# ヘッダーの削除
while line:
    # ヘッダーの削除
    if re.search('-'*10, line):
        break
    line = sys.stdin.readline()

line = sys.stdin.readline()
while line:
    # 改行のみの行の削除
    line = re.sub('\n+', '', line)
    # フッターの削除
    if re.search('^底本', line):
        break
    print line
    line = sys.stdin.readline()
