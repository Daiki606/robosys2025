# robosys2025

![test](https://github.com/Daiki606/robosys2025/actions/workflows/test.yml/badge.svg)

このリポジトリは千葉工業大学 先進工学部 ミライロボティクス学科の授業  
「ロボットシステム学（Robosys2025）」のために作成したものである。  
自作コマンドの作成および GitHub Actions を利用した自動テストを実装している。

---

## 🧭 コマンド概要（uniqcount）

`uniqcount` は標準入力から読み込んだ文字列をソートし、  
同じ行をまとめて出現回数を出力するコマンドである。  
引数が指定された場合はエラーを返し、終了ステータスは 0 以外となる。

### 使用例

```bash
echo -e "a\na\nb" | ./uniqcount

## 🏷️ ライセンス（License）

This software package is distributed under the terms of the **3-Clause BSD License**.  
© 2025 Daiki Yamashita
