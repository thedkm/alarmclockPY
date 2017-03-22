import time,random ,webbrowser,datetime
from sys import argv  #Import argument from the command line from sys module. 
script, file_ = argv
# Check the playlist file
file = open(file_, 'r+')
list = file.readlines()
for item in list: pass
nlist = [] 
nlist += list
pick = random.randrange(len(nlist))
print(nlist[pick])
#Print the current time
print ("current time is:"+datetime.datetime.now().strftime("%H:%M:%S"))
print("\nEnter the time you want to wake up as HH:MM:SS")
alarm = input("Input time>")
clock = datetime.datetime.now().strftime("%H:%M:%S")
while clock != alarm:
	print ("Curent Time at present is: " + clock)
	clock = time.strftime("%H:%M:%S")
	time.sleep(1)	
if alarm == clock:
	webbrowser.open(nlist[pick])




