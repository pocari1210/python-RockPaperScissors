from random import randint
import time

hands = ["グー","チョキ","パー"]
rules = ["あいこ","負け","勝ち"]

win = 0
lose = 0
draw = 0

print("====じゃんけんスタート====")

while True:
  #Player
  print("0:グー 1:チョキ 2:パー")
  p = int(input("どれをだしますか?"))
  print("あなたは" + hands[p] + "をだす")

  # コンピューターの処理で0.9秒処理を遅らせる
  time.sleep(0.9)

  # コンピューターの処理
  m = randint(0,2)
  print("PCは" + hands[p] + "をだす")

  # 勝敗判定
  i = (p - m) % 3
  print(rules[i])

  # 配列の数値の差分で結果を決める
  if i == 0:
    draw = draw + 1
  elif i == 1:
    lose = lose + 1
  elif i == 2:
    win = win + 1
  time.sleep(0.9)

  # 結果を出力する
  print("{}勝/{}負{}引き分け".format(win, lose, draw))

  if win == 3:
    print("対戦結果:プレイヤーの勝ち")
    
    # while文から抜ける
    break

  elif lose == 3:
    print("対戦結果:コンピューターの勝ち")
    break


  
