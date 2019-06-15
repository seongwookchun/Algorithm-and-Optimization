# 묵찌빠 게임

import random

d_rps = {0:'Rock', 1:'Paper', 2:'Scissors'}
d_players = {-1:'Player', 1:'Computer', 0:'None'}
d_gameType = {1:'RPS', 2:'묵찌빠'}
def sign(x):
  if x > 0:
    return 1
  elif x < 0:
    return -1
  #elif x == 0:
  return 0

flag_winner = 0    # initializing flag_winner as -1
# flag_rpsUser = 0
flag_gameType = 1    # 1: normal, 2: 묵찌빠
while True:
  # Rock Paper Scissors
  # 0    1     2
  rps_com = random.randint(0, 2)     # computer picks rps
  # print('*********** Rock Paper Scissors **********')

  while True:#flag_rpsUser < 1:
    print(' 0    1     2')
    rps_user = int(input('>>>'))
    print('gameType      :', d_gameType[flag_gameType])
    print('offense player:', d_players[sign(flag_winner)])
    print('computer rps  :', d_rps[rps_com])
    print('users rps     :', d_rps[rps_user])
    if (not (rps_user == 0) and not(rps_user == 1) and not(rps_user == 2)):
      print('Your input:', type(rps_user), rps_user)
      print('Input correct value')
    else:
      break

  
  dist = rps_com - rps_user
  if flag_gameType == 1:
    print('*********** RPS ***********')
    if dist != 0:
      flag_winner = dist 
      flag_gameType = 2
      print('Winner of RPS is player', d_players[sign(flag_winner)])

  elif flag_gameType == 2:
    print('*********** 묵찌빠 ***********')
    if dist == 0:
      print('Winner of 묵찌빠 is player', d_players[sign(flag_winner)])
      break
    

  print('again...')
