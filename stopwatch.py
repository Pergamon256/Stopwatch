import time

x = int(input("Enter stopwatch minutes: "))
y = int(input("Enter stopwatch seconds: "))

print('Stopwatch started') #You can edit this to display whatever text you want, even include strings using {} and .format()
def stopwatch(m,s):
	i=m
	j=s
	k=0
	try:
		while True:
			if(j == 60):
				j = 0
				i += 1
			if((i > 9) and (j > 9)):
				print(str(i)+":"+str(j), end='\r') #Carriage return only works with python 3; end='\r' will not work with python 2.
			elif(i > 9):
				print(str(i)+":"+str(k)+str(j), end='\r')
			elif(j > 9):
				print(str(k)+str(i)+":"+str(j), end='\r')
			else:
				print(str(k)+str(i)+":"+str(k)+str(j), end='\r')
			time.sleep(1)
			j += 1
	except KeyboardInterrupt:
		pass
		print("", end='\r')

result = stopwatch(x,y)
stopwatch(result)