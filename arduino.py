import serial
import time
serials = []
from datetime import datetime
file1 = open("output1.csv","a")
file2 = open("output2.csv","a")
file3 = open("output3.csv","a")
def uncode(text):
	try:
		text = text.decode()
		text = text.strip()
	except:
		return ""
	else:
		return text
def main(s):
	if not s:
		print("no arduinos connected")
		exit()
	time_prev1 = 0
	time_now1 = 0
	time_prev2 = 0
	time_now2 = 0
	time_prev3 = 0
	time_now3 = 0
	while True:
		for i in s:
			if i:
				data = i.readline()
				data = uncode(data)
				if not data == "":
					out = data
					now = datetime.now()
					dt = now.strftime("%d/%m/%Y;%H:%M:%S")
					out = dt + ";" + out + "\r\n"
					out = out.replace(".",",")
					file1.flush()
					file2.flush()
					file3.flush()
					try:
						if i.name == s[0].name:
							time_prev1 = time_now1
							time_now1 = time.time()
							file1.write(out)
							print("time",i.name,"took:",time_now1 - time_prev1)
						if i.name == s[1].name:
							time_prev2 = time_now2
							time_now2 = time.time()
							file2.write(out)
							print("time",i.name,"took:",time_now2 - time_prev2)
						if i.name == s[2].name:
							time_prev3 = time_now3
							time_now3 = time.time()
							file3.write(out)
							print("time",i.name,"took:",time_now3 - time_prev3)
					except:
						raise

for i in range(0,33):
	try:
		global a
		a = serial.Serial("/dev/ttyACM" + str(i),115200,timeout=0.01)
	except:
		pass
	else:
		print("found arduino at /dev/ttyACM" + str(i))
		serials.append(a)
for i in range(0,33):
	try:
		global b
		b = serial.Serial("/dev/ttyUSB" + str(i),115200,timeout=0.01)
	except:
		pass
	else:
		print("found arduino at /dev/ttyUSB" + str(i))
		serials.append(b)
try:
	main(serials)
except:
	file1.close()
	file2.close()
	file3.close()
	raise
