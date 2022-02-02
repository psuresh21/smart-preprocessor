import time  
import datetime

print("---------------------------------------------------------")
mydt = datetime.datetime.now()
print("welcome to smart preprocessor (.smart)")
print("it's will make your fingers less pain due to smart preprocessor \n it's take you next level of css")
print("Copyright (c) " + mydt.strftime("%Y") + " Suresh Pandiyan \n")

k = str(input("file path: \n"))

while(True):
	c = []
	with open(k) as load:
		for enter in load:
			#print(enter)
			m = enter.rstrip()
			c.append(m)
	m = k.replace(".smart",".css")
	with open(m,"w+") as kk:
		mt = range(len(c))
		for x in mt:
			s = c[x].replace("[","{").replace("]","}").replace("'''","/*").replace("''","*/").replace("!imp","!important").replace(".. ",": ").replace("hash","#").replace("'#'","#").replace("global","*")
			print(s, file=kk)
	iop = m.replace(".css",".txt")
	with open(m, "r") as kf:
		for kk in kf:
			with open(iop, "w+") as kkm:
				print(" PATH: "+ m +"\n","Ln:" + str(int(x) + 1), file=kkm)
	time.sleep(1)



