import os,sys
import jieba,codecs,math
import jieba.posseg as pseg

# names and counts
names = {}
# relation like {alice:{ben:1,june:2}}
relationships = {}
# lineName[i] = people'name appear in each line
lineNames = []

jieba.load_userdict("dict.txt")
with codecs.open("busan.txt","r","utf8") as f:
	for line in f.readlines():
		poss = pseg.cut(line)
		lineNames.append([])
		for w in poss:
			if w.flag == "nr" and len(w.word)>=2:
				lineNames[-1].append(w.word)
				if w.word not in names.keys():
					names[w.word] = 0
					relationships[w.word]={}
				names[w.word] += 1
for line in lineNames:
	for name1 in line:
		for name2 in line:
			if name1 != name2:
				if relationships[name1].get(name2) is None:
					relationships[name1][name2] = 1
				else:
					relationships[name1][name2] += 1

with codecs.open("busan_node.txt","w","gbk") as f:
	f.write("Name Label Weight\r\n")
	for name, times in names.items():
		f.write(name + " " + name + " " + str(times) + "\r\n")

with codecs.open("busan_edge.txt","w","gbk") as f:
	f.write("Source Target Weight\r\n")
	for name,edges in relationships.items():
		for v,w in edges.items():
			if w>3:
				f.write(name + " " + v + " " + str(w) + "\r\n")



