#import gzip
#counter = 0
#my_list=[0]*200000000
#with gzip.open("/Akamai_scratch/enwiki-20080103.good.gz",'r') as file:
#        for line in file:
#                if counter <= 1:
#			revision = line.decode().split("\x1f")
#			print("after decode", revision)
#                        my_list[counter] = revision[0]
#                        counter +=1
#                else:
#                    break
#        my_list = my_list[0:counter]
#        my_list = list(set(my_list))
#        # file.write(my_list)
#        print (len(my_list))
#
#        newfile = gzip.open('unique_all_articleids.gz', 'wt')
#        newfile.writelines(my_list)
#        newfile.close()
#

#import gzip
#counter = 0
#my_list=[0]*200000000
#with gzip.open("/Akamai_scratch/enwiki-20080103.good.gz",'r') as file:
#        for line in file:
#                if counter <= 1:
#                    print("!!!!!before revision", line)
#                    revision = line.decode().split("\x1e")
#                    print("!!!!!after decode", revision)
#		    revision = revision.split(' ')
#		    print('!!!REVISION SPLIT BY SPACES')  
#		    my_list[counter] = revision[0]
#                    counter +=1
#                else:
#                    break
#        my_list = my_list[0:counter]
#        my_list = list(set(my_list))
#        # file.write(my_list)
#        print (len(my_list))
#
#        newfile = gzip.open('unique_all_articleids.gz', 'wt')
#        newfile.writelines(my_list)
#        newfile.close()


import gzip
counter = 0
my_list=[0]*200000000
with gzip.open("/Akamai_scratch/enwiki-20080103.good.gz",'r') as file:
        for line in file:
                if counter <= 1000000:
                    print("before revision", line)
                    revision = line.decode().split("\x1f")
                    print("after decode", revision)
                    #[words for segments in revision for words in segments.split()] 
                    #print("after list compr", revision)
                    revision = str(revision).split(' ')
                    print("after revision space split", revision)
                    my_list[counter] = revision[1]
                    print("what's the 0th indice of revision", my_list[counter]) 
                    counter +=1
                else:
                    break
        my_list = my_list[0:counter]
        my_list = list(set(my_list))
        # file.write(my_list)
        print(len(my_list))
        print(my_list)

        newfile = gzip.open('unique_all_articleids_3.gz', 'wt')
        items = map(lambda x: x + '\n', my_list)
        newfile.writelines(items)
        newfile.close()
