from itertools import count
from os import WNOHANG
from rich.console import Console
import math as m
import layouts as lay

cnsl = Console()

f = open("english_text.txt", "r")
style1 = "#ffffff b i"
style2 = "#000000 on #ffffff b i"
# layout_['style'] = "staggered"
# layout_['style'] = "ortho"

# list of all keyboard layouts could be found in layouts.py


#? ============ FUCTIONS ================================================
def calc_heatmap(text_, layout_):
	#? weird syntax instead of a generator, for clarity's sake
	layout_heatmap = [
		[0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,],
		[0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,],
		[0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,],
		[0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,],
	]

	for i in range(len(text_)):
		for x in range(4):
			try:
				numx = layout_[x].index(text_[i])
				layout_heatmap[x][numx] += 1
			except ValueError:
				pass

	return layout_heatmap




def calc_fing_stats(heatmap, layout_):
	hm = heatmap
	fing_stats = [0,    0,    0,    0,                0,    0,    0,    0]

	if layout_['style'] == 'staggered':
		fing_stats[0] = hm[0][0] + hm[1][0] + hm[2][0]
		fing_stats[1] = hm[0][1] + hm[1][1] + hm[2][1] + hm[3][0]
		fing_stats[2] = hm[0][2] + hm[1][2] + hm[2][2] + hm[3][1]
		fing_stats[3] = hm[0][3] + hm[1][3] + hm[2][3] + hm[3][2]\
				+ hm[0][4] + hm[1][4] + hm[2][4] + hm[3][3] + (hm[3][4] // 2)
		#*remap all after that
		fing_stats[4] = hm[0][5] + hm[1][5] + hm[2][5] + hm[3][5]\
				+ hm[0][6] + hm[1][6] + hm[2][6] + hm[3][0]
		fing_stats[5] = hm[0][7] + hm[1][7] + hm[2][7] + hm[3][7]
		fing_stats[6] = hm[0][8] + hm[1][8] + hm[2][8] + hm[3][8]
		fing_stats[7] = hm[0][9] + hm[1][9] + hm[2][9] + hm[3][9]\
				+ hm[0][10]+ hm[1][10]+ hm[1][10]+ hm[3][10]\
				+ hm[0][11]+ hm[1][11]+ hm[1][11]+ hm[3][11]\
	if layout_['style'] == 'ortho': # all done!
		fing_stats[0] = hm[0][0] + hm[1][0] + hm[2][0] + hm[3][0]
		fing_stats[1] = hm[0][1] + hm[1][1] + hm[2][1] + hm[3][1]
		fing_stats[2] = hm[0][2] + hm[1][2] + hm[2][2] + hm[3][2]
		fing_stats[3] = hm[0][3] + hm[1][3] + hm[2][3] + hm[3][3]\
				+ hm[0][4] + hm[1][4] + hm[2][4] + hm[3][4]

		fing_stats[4] = hm[0][5] + hm[1][5] + hm[2][5] + hm[3][5]\
				+ hm[0][6] + hm[1][6] + hm[2][6] + hm[3][0]
		fing_stats[5] = hm[0][7] + hm[1][7] + hm[2][7] + hm[3][7]
		fing_stats[6] = hm[0][8] + hm[1][8] + hm[2][8] + hm[3][8]
		fing_stats[7] = hm[0][9] + hm[1][9] + hm[2][9] + hm[3][9]\
				+ hm[0][10]+ hm[1][10]+ hm[1][10]+ hm[3][10]\
				+ hm[0][11]+ hm[1][11]+ hm[1][11]+ hm[3][11]\

	return fing_stats




def calc_avrg_per_finger(layout_, fing_stats, avrg_per_finger):
	deviation = [abs((fing_stats[i] - avrg_per_finger)) for i in range(8)]
	deviation = sum(deviation)//8
	return deviation




def compare_to_qwerty(layout_):
	qwerty_alike = 0

	for x in range(len(layout_["content"])): 
		for y in range(len(layout_["content"][x])):
			if layout_["content"][x][y] == lay.qwerty["content"][x][y]:
				qwerty_alike += 1

	persentage = int(qwerty_alike/48*100)

	return qwerty_alike, persentage




def calc_SFU(text_, layout_):
	which_finger = []
	same_finger = 0
	same_finger_matrix = [0, 0, 0, 0, 0, 0, 0, 0]


	for i in range(len(text_)):
		for x in range(4):
			if text_[i] in layout_[x][0]:
				which_finger.append("l_pinky")

			elif text_[i] in layout_[x][1]:
				which_finger.append("l_ring")

			elif text_[i] in layout_[x][2]:
				which_finger.append("l_mid")

			elif text_[i] in layout_[x][3] or text_[i] in layout_[x][4]:
				which_finger.append("l_point")


			elif text_[i] in layout_[x][5] or text_[i] in layout_[x][6]:
				which_finger.append("r_point")

			if text_[i] in layout_[x][7]:
				which_finger.append("r_mid")

			elif text_[i] in layout_[x][8]:
				which_finger.append("r_ring")

			elif text_[i] in layout_[x][9] or text_[i] in layout_[x][10] or text_[i] in layout_[x][6]:
				which_finger.append("r_pinky")


	for i in range(len(which_finger)-1):
		if which_finger[i] == which_finger[i+1]:
			same_finger += 1

			if which_finger[i]   == "l_pinky": same_finger_matrix[0] += 1
			elif which_finger[i] == "l_ring": same_finger_matrix[1] += 1
			elif which_finger[i] == "l_mid": same_finger_matrix[2] += 1
			elif which_finger[i] == "l_point": same_finger_matrix[3] += 1
			
			elif which_finger[i] == "r_point": same_finger_matrix[4] += 1
			elif which_finger[i] == "r_mid": same_finger_matrix[5] += 1
			elif which_finger[i] == "r_ring": same_finger_matrix[6] += 1
			elif which_finger[i] == "r_pinky": same_finger_matrix[7] += 1

	return same_finger, same_finger_matrix




def showResult(layout_):
	layout_heatmap = calc_heatmap(text, layout_["content"])
	fing_stats = calc_fing_stats(layout_heatmap, layout_)
	avrg_per_finger = int(sum(fing_stats) / 8)
	same_finger, same_finger_matrix = calc_SFU(text, layout_["content"])
	deviation = calc_avrg_per_finger(layout_, fing_stats, avrg_per_finger)

	homerow_use = sum(layout_heatmap[2][0:4]) + sum(layout_heatmap[2][6:10])
	#? leave this syntax intact. it's easier to demonstrate which keys it targets
	midcolumns_use = layout_heatmap[0][4] + layout_heatmap[0][5]\
	               + layout_heatmap[1][4] + layout_heatmap[1][5]\
	               + layout_heatmap[2][4] + layout_heatmap[2][5]\
	               + layout_heatmap[3][4] + layout_heatmap[3][5]


	qwerty_alike, qwerty_alike_percent = compare_to_qwerty(layout_)

	homerow_use_percent = int(homerow_use / len(text) * 100)

	# === === DISPLAYING
	cnsl.print(f" "*26 + layout_['name'].upper() + " "*(32-len(layout_['name'])), style=style2)
	cnsl.print("LAYOUT----------------------------------------------------", style=style1)
	cnsl.print(" " + "    ".join(layout_["content"][0]), style="#888888")

	cnsl.print(" " + "    ".join(layout_["content"][1]))

	if layout_['style']=="staggered": print(end=" ")
	cnsl.print(" " + "    ".join(layout_["content"][2][0:4]), style="#9999ff bold underline", end='    ')
	cnsl.print("    ".join(layout_["content"][2][4:6]), end='   ')
	cnsl.print(" " + "    ".join(layout_["content"][2][6:10]), style="#9999ff bold underline", end='    ')
	cnsl.print("    ".join(layout_["content"][2][10:12]))


	if layout_['style']=="staggered": print(end="    ")
	cnsl.print(" " + "    ".join(layout_["content"][3]))


	print(f"simmilar to qwerty {qwerty_alike}/48 (~{qwerty_alike_percent}%)")


	cnsl.print("\nHEATMAP---------------------------------------------------", style=style1)
	colorset = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"] #16
	max_heatmap_value = max([max(l) for l in layout_heatmap])

	for x in range(len(layout_heatmap)): 
		if x==2:
			if layout_['style']=="staggered": print(end=" ")
		if x==3:
			if layout_['style']=="staggered": print(end="    ")


		for y in range(len(layout_heatmap[x])):
			msg = str(layout_heatmap[x][y]).zfill(3)
			step_size = max_heatmap_value // 15
			color = "#" + colorset[int(msg)//step_size]*3 + "333"  #to invert, add 15- before int(msg)

			if x==2 and y in [0, 1, 2, 3, 6, 7, 8, 9]: #chcking if homerow
				cnsl.print(f"[{color} u o] {msg} [/]", end='') #optionally add an r, to reverse fg and bg
			else:
				cnsl.print(f"[{color} ] {msg} [/]", end='')
		print('')
		
	print(f"middle columns {midcolumns_use} (less = better)")
	print(f"homerow {homerow_use} ({homerow_use_percent}%)")
  

	cnsl.print("\nPER FINGER PRESSES----------------------------------------", style=style1)
	for i, elem in enumerate(fing_stats[0:4]):
		print(str(elem).zfill(3), end='  ')

	print("		", end="")

	for i, elem in enumerate(fing_stats[4:]):
		print(str(elem).zfill(3), end='  ')

	print(f"\navrg presses {avrg_per_finger} (avrg deviation {deviation})\n")

	cnsl.print("COMFORT LEVEL \\ SAME FINGER UTILISATION-------------------", style=style1)
	print(f"same finger utilisation {same_finger} (in total)")

	print("same finger utilisation per finger")
	for x in range(4): print(str(same_finger_matrix[x]).zfill(3), end='  ')
	print(end="		  ")
	for x in range(4, 8): print(str(same_finger_matrix[x]).zfill(3), end='  ')
	print("\n\n\n")






#? ============ OUTPUT ================================================
if __name__ == "__main__":
	text = list(str(f.readlines()))
	showResult(lay.qwerty)
	showResult(lay.colemak)
