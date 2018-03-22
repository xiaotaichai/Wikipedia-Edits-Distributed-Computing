from mrjob.job import MRJob
from mrjob.protocol import TextValueProtocol
import gzip
import random

all_ids = [""]*2953425
id_counter = 0
# read in list of unique article id's
with gzip.open('/Akamai_scratch/fanny_kevin_lydia_xiaotai/Wikipedia-Edits-Distributed-Computing/unique_all_articleids.gz','rt') as infile:
    for line in infile:
        if line != "\n":
            all_ids[id_counter] = line
            id_counter += 1

# select n of those id's and strip the new lines
n = 1000
selected_ids = random.sample(all_ids, n)
selected_ids = [id.rstrip('\n') for id in selected_ids]

class RandomSubsample(MRJob):

    OUTPUT_PROTOCOL = TextValueProtocol

    def mapper(self, _, line):

        article_id = line.split('<<sep>>')[0]
        # print("article id is: ", article_id)

        if article_id in selected_ids:
            yield 'key', line

    def reducer(self, key, records):
        for record in records:
            
            yield key, record


if __name__ == '__main__':
    RandomSubsample.run()
