def main():

	input_var = raw_input("Enter the name of file: ") 
	print ("you entered " + input_var)

	lista = []

	f = open(input_var,"r")
	for line in f.readlines():
		lista.append(line.split())
	f.close()
	print lista

	list_init = [int(e) for e in lista]
	print list_init


main()