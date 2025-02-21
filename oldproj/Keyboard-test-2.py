from itertools import count
from os import WNOHANG
from rich.console import Console
import math as m
from layouts import *

cnsl = Console()

f = open("text.txt", "r")
text = str(f.readlines())

style1 = "#ffffff b i"
style2 = "#000000 on #ffffff b i"


# list of all keyboard layouts could be found in layouts.py


# ============ FUCTIONS ================================================
def checktext(text_, layout_, layout_use_):
    text_ = list(text_)

    for i in range(len(text_)):
        for x in range(4):
            try:
                numx = layout_[x].index(text_[i])
                layout_use_[x][numx] += 1
            except ValueError:
                pass




def countper_finger(layout_use_, per_finger_):
    per_finger_[0] = layout_use_[0][0] + layout_use_[1][0] + layout_use_[2][0] + layout_use_[3][0]
    per_finger_[1] = layout_use_[0][1] + layout_use_[1][1] + layout_use_[2][1] + layout_use_[3][1]
    per_finger_[2] = layout_use_[0][2] + layout_use_[1][2] + layout_use_[2][2] + layout_use_[3][2]
    per_finger_[3] = layout_use_[0][3] + layout_use_[1][3] + layout_use_[2][3] + layout_use_[3][3]\
                   + layout_use_[0][4] + layout_use_[1][4] + layout_use_[2][4] + layout_use_[3][4]

    per_finger_[4] = layout_use_[0][5] + layout_use_[1][5] + layout_use_[2][5] + layout_use_[3][5]\
                   + layout_use_[0][6] + layout_use_[1][6] + layout_use_[2][6] + layout_use_[3][0]
    per_finger_[5] = layout_use_[0][7] + layout_use_[1][7] + layout_use_[2][7] + layout_use_[3][7]
    per_finger_[6] = layout_use_[0][8] + layout_use_[1][8] + layout_use_[2][8] + layout_use_[3][8]
    per_finger_[7] = layout_use_[0][9] + layout_use_[1][9] + layout_use_[2][9] + layout_use_[3][9]\
                   + layout_use_[0][10]+ layout_use_[1][10]+ layout_use_[1][10]+ layout_use_[3][10]\
                   + layout_use_[0][11]+ layout_use_[1][11]+ layout_use_[1][11]+ layout_use_[3][11]\




def count_avrg_per_finger(layout_):
    avrg_per_finger = int(sum(layout_[2]) / 8)
    deviation = 0

    for i in range(8):
        deviation += abs((layout_[2][i] - avrg_per_finger))

    deviation = int(deviation/8)

    return avrg_per_finger, deviation




def compare_to_qwerty(layout_):
    simmilar_keys = 0

    for x in range(len(layout_[0])): 
        for y in range(len(layout_[0][x])):
            if layout_[0][x][y] == qwerty[0][x][y]:
                simmilar_keys += 1

    persentage = int(simmilar_keys/48*100)

    return simmilar_keys, persentage




def count_comfort(text_, layout_):
    # text_ = list(text_)
    # print(text_)
    which_finger = []
    same_finger = 0
    same_finger_matrix = [0, 0, 0, 0, 0, 0, 0, 0]


    for i in range(len(text_)):
        for x in range(4):
            if text_[i] in layout_[x][0]:
                which_finger.append("ltPy")

            elif text_[i] in layout_[x][1]:
                which_finger.append("ltRg")

            elif text_[i] in layout_[x][2]:
                which_finger.append("ltMl")

            elif text_[i] in layout_[x][3] or text_[i] in layout_[x][4]:
                which_finger.append("ltPr")


            elif text_[i] in layout_[x][5] or text_[i] in layout_[x][6]:
                which_finger.append("rtPr")

            if text_[i] in layout_[x][7]:
                which_finger.append("rtMl")

            elif text_[i] in layout_[x][8]:
                which_finger.append("rtRg")

            elif text_[i] in layout_[x][9] or text_[i] in layout_[x][10] or text_[i] in layout_[x][6]:
                which_finger.append("rtPy")


    for i in range(len(which_finger)-1):
        if which_finger[i] == which_finger[i+1]:
            same_finger += 1

            if which_finger[i]   == "ltPy": same_finger_matrix[0] += 1
            elif which_finger[i] == "ltRg": same_finger_matrix[1] += 1
            elif which_finger[i] == "ltMl": same_finger_matrix[2] += 1
            elif which_finger[i] == "ltPr": same_finger_matrix[3] += 1
            
            elif which_finger[i] == "rtPr": same_finger_matrix[4] += 1
            elif which_finger[i] == "rtMl": same_finger_matrix[5] += 1
            elif which_finger[i] == "rtRg": same_finger_matrix[6] += 1
            elif which_finger[i] == "rtPy": same_finger_matrix[7] += 1

    return same_finger, same_finger_matrix




def showResult(layout_):
    checktext(text, layout_[0], layout_[1])
    countper_finger(layout_[1], layout_[2])
    same_finger, same_finger_matrix = count_comfort(text, layout_[0])

    homerow_use = layout_[1][2][0] + layout_[1][2][1] + layout_[1][2][2] + layout_[1][2][3] \
                + layout_[1][2][6] + layout_[1][2][7] + layout_[1][2][8] + layout_[1][2][9]

    midcolumns_use = layout_[1][0][4] + layout_[1][0][5]\
                   + layout_[1][1][4] + layout_[1][1][5]\
                   + layout_[1][2][4] + layout_[1][2][5]\
                   + layout_[1][3][4] + layout_[1][3][5]

    avrg_per_finger, deviation = count_avrg_per_finger(layout_)

    simmilar_keys, si_ke_persent = compare_to_qwerty(layout_)

    homerow_use_percent = int(homerow_use / len(text) * 100)
   

    cnsl.print("LAYOUT----------------------------------------------------", style=style1)
    cnsl.print("    ".join(layout_[0][0]), style="#777777")
    cnsl.print("    ".join(layout_[0][1]))
    cnsl.print("    ".join(layout_[0][2][0:4]), style="#9999ff bold", end='    ')
    cnsl.print("    ".join(layout_[0][2][4:6]), end='    ')
    cnsl.print("    ".join(layout_[0][2][6:10]), style="#9999ff bold", end='    ')
    cnsl.print("    ".join(layout_[0][2][10:12]))
    cnsl.print("    ".join(layout_[0][3]))


    print(f"simmilar to qwerty {simmilar_keys}/48 (~{si_ke_persent}%)")


    cnsl.print("\nHEATMAP---------------------------------------------------", style=style1)
    for x in range(len(layout_[1])): 
        for y in range(len(layout_[1][x])):
            print(str(layout_[1][x][y]).zfill(3), end='  ')
        print("")
        
    print(f"middle columns {midcolumns_use} (less = better)")
    print(f"homerow {homerow_use} ({homerow_use_percent}%)")
  

    cnsl.print("\nPER FINGER PRESSES----------------------------------------", style=style1)
    for x in range(4):
        print(str(layout_[2][x]).zfill(3), end='  ')
    print(end="          ")

    for x in range(4, 8):
        print(str(layout_[2][x]).zfill(3), end='  ')
    print("")
    print(f"avrg presses {avrg_per_finger} (avrg deviation {deviation})\n")

    cnsl.print("COMFORT LEVEL \\ SAME FINGER UTILISATION-------------------", style=style1)
    print(f"same finger utilisation {same_finger} (in total)")

    print("same finger utilisation per finger")
    for x in range(4): print(str(same_finger_matrix[x]).zfill(3), end='  ')
    print(end="          ")
    for x in range(4, 8): print(str(same_finger_matrix[x]).zfill(3), end='  ')
    print("\n")






# ============ OUTPUT ================================================
if __name__ == "__main__":
    cnsl.print("                          QWERTY                          ", style=style2)
    showResult(qwerty)
    print("\n\n\n")

    cnsl.print("                          QWIRFY                          ", style=style2)
    showResult(qwirfy)  #ie ft uj ke ln
    print("\n\n\n")

    cnsl.print("                          QWSDFY                          ", style=style2)
    showResult(qwsdfy)  #ie ft uj ke ln
    print("\n\n\n")

    cnsl.print("                          COLEMAK                         ", style=style2)
    showResult(colemak)
    print("\n\n\n")

    # cnsl.print("                          DVORAK                          ", style=style2)
    # showResult(dvorak)
    # print("\n\n\n")

    # cnsl.print("                          WORKMAN                         ", style=style2)
    # showResult(workman)
    # print("\n\n\n")
