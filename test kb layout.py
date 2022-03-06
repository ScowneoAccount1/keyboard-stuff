from os import WNOHANG


text = "Text where you will test how good your keyboard layout is."


# QWERTY----------------------------------------------------------
qwerty = [["q", "w", "e", "r", "t", "y", "u", "i", "o", "p"],
          ["a", "s", "d", "f", "g", "h", "j", "k", "l", ";", ],
          ["z", "x", "c", "v", "b", "n", "m", ",", ".", "'", ]]

qwertyUse = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],]

qwertyPerF = [0, 0, 0, 0, 0, 0, 0, 0]


# layout2----------------------------------------------------------
layout2 = [[" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", ],
          [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", ],
          [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", ]]

layout2Use = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],]

layout2PerF = [0, 0, 0, 0, 0, 0, 0, 0]


# layout3----------------------------------------------------------
layout3 = [[" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", ],
          [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", ],
          [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", ]]

layout3Use = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],]

layout3PerF = [0, 0, 0, 0, 0, 0, 0, 0]



# ============ FUCTIONS
def checktext(text_, layout_, layoutUse_):
  text_ = list(text_)

  for i in range(len(text_)):
    for x in range(3):
      try:
        numx = layout_[x].index(text_[i])
        # if numx:
        layoutUse_[x][numx] += 1
          # break
      except ValueError:
        pass

def countPerF(layoutUse_, PerF_):
  PerF_[0] = layoutUse_[0][0] + layoutUse_[1][0] + layoutUse_[2][0]
  PerF_[1] = layoutUse_[0][1] + layoutUse_[1][1] + layoutUse_[2][1]
  PerF_[2] = layoutUse_[0][2] + layoutUse_[1][2] + layoutUse_[2][2]
  PerF_[3] = layoutUse_[0][3] + layoutUse_[1][3] + layoutUse_[2][3] + layoutUse_[0][4] + layoutUse_[1][4] + layoutUse_[2][4]

  PerF_[4] = layoutUse_[0][5] + layoutUse_[1][5] + layoutUse_[2][5] + layoutUse_[0][6] + layoutUse_[1][6] + layoutUse_[2][6]
  PerF_[5] = layoutUse_[0][7] + layoutUse_[1][7] + layoutUse_[2][7]
  PerF_[6] = layoutUse_[0][8] + layoutUse_[1][8] + layoutUse_[2][8]
  PerF_[7] = layoutUse_[0][9] + layoutUse_[1][9] + layoutUse_[2][9]

  # return PerF_
  


# ============ EXECUTION
checktext(text, qwerty, qwertyUse)
countPerF(qwertyUse, qwertyPerF)

checktext(text, layout2, layout2Use)
countPerF(layout2Use, layout2PerF)

checktext(text, layout3, layout3Use)
countPerF(layout3Use, layout3PerF)



# ============ OUTPUT
print("\n\n--------------------QWERTY----------------------\nlayout")
#qwerty
for x in range(len(qwerty)): 
  for y in range(len(qwerty[x])):
    print(qwerty[x][y]+"  ", end='  ')
  print("")
print("\nheatmap")

#qwertyUse
for x in range(len(qwertyUse)): 
  for y in range(len(qwertyUse[x])):
    print(str(qwertyUse[x][y]).zfill(3), end='  ')
  print("")
print("\nper finger presses")

#qwertyPerF
for x in range(4):
  print(str(qwertyPerF[x]).zfill(3), end='  ')
for x in range(4, 5):
  print("          " + str(qwertyPerF[x]).zfill(3), end='  ')
for x in range(5, 8):
  print(str(qwertyPerF[x]).zfill(3), end='  ')
print("") 
print("\nhomerow use: " , str(sum(qwertyUse[1])))


print("\n\n--------------------layout2----------------------\nlayout")
#layout2
for x in range(len(layout2)): 
  for y in range(len(layout2[x])):
    print(layout2[x][y]+"  ", end='  ')
  print("")
print("\nheatmap")

#qwertyUse
for x in range(len(layout2Use)): 
  for y in range(len(layout2Use[x])):
    print(str(layout2Use[x][y]).zfill(3), end='  ')
  print("")
print("\nper finger presses")

#qwertyPerF
for x in range(4):
  print(str(layout2PerF[x]).zfill(3), end='  ')
for x in range(4, 5):
  print("          " + str(layout2PerF[x]).zfill(3), end='  ')
for x in range(5, 8):
  print(str(layout2PerF[x]).zfill(3), end='  ')
print("")
print("\nhomerow use: " , str(sum(layout2Use[1])))


print("\n\n--------------------layout3---------------------\nlayout")
#layout2
for x in range(len(layout3)): 
  for y in range(len(layout3[x])):
    print(layout3[x][y]+"  ", end='  ')
  print("")
print("\nheatmap")

#qwertyUse
for x in range(len(layout3Use)): 
  for y in range(len(layout3Use[x])):
    print(str(layout3Use[x][y]).zfill(3), end='  ')
  print("")
print("\nper finger presses")

#qwertyPerF
for x in range(4):
  print(str(layout3PerF[x]).zfill(3), end='  ')
for x in range(4, 5):
  print("          " + str(layout3PerF[x]).zfill(3), end='  ')
for x in range(5, 8):
  print(str(layout3PerF[x]).zfill(3), end='  ')
print("")
print("\nhomerow use: " , str(sum(layout3Use[1])))
