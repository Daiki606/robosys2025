#!/usr/bin/env python3
import sys

try:
    nums = []
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        # チェック: 数字でなければ例外を出す
        if not line.isdigit() and not (line.startswith('-') and line[1:].isdigit()):
            sys.exit(1)
        nums.append(int(line))

    # 入力がなかった場合もエラー
    if len(nums) == 0:
        sys.exit(1)

    print(sum(nums))
except:
    sys.exit(1)


