a= int(raw_input("enter the number"))
i = 2
while i<a:
	if a%i == 0:
		print "not prime", a
		break
	i = i+1
else:
	print"prime",a
