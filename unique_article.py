import gzip
counter = 0
list=[0]*200000000
with gzip.open("/Akamai_scratch/enwiki-20080103.good.gz",'r') as file:
	for line in file:
	    while counter < 100:	
                revision = line.decode().split("\x1f")
		list[counter] = revision[0]
		counter +=1
	list = list[0,counter]
	list = unique(list)
	list.write('unique_article\n')
	print (len(list))
