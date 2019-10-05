import os
import time
h=int(raw_input("hrs=>"))
m=int(raw_input("min=>"))
s=int(raw_input("sec=>"))
t=h*3600+m*60+s
h=0
m=0
s=0
a=0
check=0
while a!=t:
	start=int(time.clock()-check)					#your time starts now		
	check=int(time.clock())
	while start!=1:
		start=int(time.clock()-check)
	s+=1
	if s>=60:
		s=s-60
		m+=1
	if m>=60:
		m=m-60
		h+=1
	os.system("clear")
	print "%s:%s:%s" %(h,m,s)
	check=time.clock()
	a+=1
os.system("say 'beep beep beep beep beep. Time is up.'")		#your time is up
# code ends
