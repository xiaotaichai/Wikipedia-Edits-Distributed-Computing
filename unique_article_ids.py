import gzip


counter = 0
article_ids = [0]*200000000

with gzip.open("/Akamai_scratch/enwiki-20080103.good.gz",'r') as infile:
    for line in infile:

        record = line.decode().split("\x1e")
        revision = str(record[0]).split(' ')
        article_ids[counter] = revision[1]
        counter += 1
        if counter%1000000 == 0:
            print('{0} records processed so far...'.format(counter))


article_ids = article_ids[0:counter]
unique_article_ids = list(set(article_ids))
print('Number of unique article_ids: {0}'.format(len(unique_article_ids)))


outfile = gzip.open('unique_all_articleids.gz', 'wt')
items = map(lambda x: x + '\n', unique_article_ids)
outfile.writelines(items)
outfile.close()
