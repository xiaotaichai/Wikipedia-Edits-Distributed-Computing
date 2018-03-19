import gzip
counter = 0
my_list=[0]*200000000
with gzip.open("/Akamai_scratch/enwiki-20080103.good.gz",'r') as file:
	for line in file:
	    while counter < 100:	
                revision = line.decode().split("\x1f")
		my_list[counter] = revision[0]
		counter +=1
        my_list = my_list[0:counter]
	my_list = list(set(my_list))
	file.write(my_list)
	print (len(my_list))
