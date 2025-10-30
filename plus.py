#!/usr/bin/env python3
import sys

try:
    nums = []
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        # 数字でなければエラー終了
        if not line.isdigit() and not (line.startswith('-') and line[1:].isdigit()):
            sys.exit(1)
        nums.append(int(line))

    if len(nums) == 0:     # 入力なし→エラー
        sys.exit(1)

    print(sum(nums))
except:
    sys.exit(1)



