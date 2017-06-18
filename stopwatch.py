import os
import time
h=int(raw_input("hrs=>"))
m=int(raw_input("min=>"))
s=int(raw_input("sec=>"))
t=h*3600+m*60+s
a=1
check=0
while a!=t+1:
	start=int(time.clock()-check)			
	check=int(time.clock())
	while start!=1:
		start=int(time.clock()-check)
	os.system("clear")
	print "%s:%s:%s" %(a/3600,(a%3600)/60,a-a/3600-(a%3600)/60)
	check=time.clock()
	a+=1
os.system("say 'beep beep beep beep beep. Time is up.'")
