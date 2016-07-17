def main():

	numer = 0

	input_var = raw_input("Enter the name of file: ") 
	read =  open(input_var , "rb")
	linea = read.readlines()

	print linea
	read.close()
	print ("you entered " + input_var)

	f = open(input_var,"r")
	for line in f.readlines():
		numlist = line.split()
  		numer += numlist
  		print numer
  		print [line]
	f.close()

	# liste = ["2","3",["1","4"]]

	# list_init = [int(e) for e in liste]
	# print list_init

main()