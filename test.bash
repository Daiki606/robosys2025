#!/usr/bin/env bash
# ==== 設定 ====
set -u
set -o pipefail

# NGを出す関数（エラー行を表示）
ng () {
  echo "NG at line: $1" 1>&2
  res=1
}

res=0

# ==== テスト開始 ====

# T1: 正常系 (1..5の合計=15)
out="$(seq 5 | ./plus)"
st="$?"
if [ "$st" -ne 0 ]; then ng "$LINENO"; fi
if [ "$out" != "15" ]; then ng "$LINENO"; fi

# T2: 異常系（非数値が混ざる）
out="$(printf '1\nあ\n3\n' | ./plus)"
st="$?"
if [ "$st" -eq 0 ]; then ng "$LINENO"; fi
if [ -n "$out" ]; then ng "$LINENO"; fi

# T3: 異常系（空入力）
out="$(printf '' | ./plus)"
st="$?"
if [ "$st" -eq 0 ]; then ng "$LINENO"; fi
if [ -n "$out" ]; then ng "$LINENO"; fi

# T4: 境界テスト（大きな数）
out="$(printf '1000000\n2000000\n' | ./plus)"
st="$?"
if [ "$st" -ne 0 ]; then ng "$LINENO"; fi
if [ "$out" != "3000000" ]; then ng "$LINENO"; fi

# ==== 結果 ====
if [ "$res" -eq 0 ]; then
  echo "OK"
fi

exit "$res"
