#python

# 2桁の足し算の問題を出題するプログラムを作成してください。
# ユーザーの入力を求めて正解かどうか判定してください。
# 正解だった場合は「正解です」と表示し、
# 正解でない場合は「正解はxx」と表示してください。xxには正解の数字を入れてください。

# 例
# 1桁の足し算の問題を出題します。
# 5 + 3 = 8
# 正解です
# 1桁の足し算の問題を出題します。
# 5 + 3 = 9
# 正解は8です

# 2桁の足し算の問題を5回出題する
# 各問題の計算結果の合計と平均を求める
# 正解数、合計、平均、スコアをファイル（score.txt）に追記する
# ファイルが初めて作成される場合を考慮する
# スコアは正解数/合計 とする
import random
import time

def main():
    correct_answers = 0
    total_time = 0
    print("2桁の足し算の問題を出題します。")
    for i in range(5):
        a = random.randint(10,99)
        b = random.randint(10,99)
        print(a,"+",b,"=")
        start_time = time.time()
        c = int(input())
        end_time = time.time()
        elapsed_time = end_time - start_time
        total_time += elapsed_time
        if c == a + b:
            print("正解です")
            correct_answers += 1
        else:
            print("正解は", a+b, "です")

    # 合計と平均を計算
    average_time = total_time / 5

    # スコアを計算
    score = (correct_answers / total_time) * 100
    # 合計、平均、スコアを表示
    print(f"合計所要時間: {total_time} 平均所要時間: {average_time} スコア: {score}")
    # ファイルに結果を書き込む
    with open("score.txt", "a") as f:
        f.write(f"正解数: {correct_answers}\n")
        f.write(f"合計所要時間: {total_time}\n")
        f.write(f"平均所要時間: {average_time}\n")
        f.write(f"スコア: {score}\n")

if __name__ == "__main__":
    main()
