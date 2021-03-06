from mrjob.job import MRJob
from mr3px.csvprotocol import CsvProtocol
import gzip
import random

# read in list of unique article id's
with gzip.open('unique_all_articleids.gz','rt') as infile:
    all_ids = infile.readlines()

# select n of those id's and strip the new lines
n = 10
selected_ids = random.sample(all_ids, n)
selected_ids = [id.rstrip('\n') for id in selected_ids]


class RandomSubsample(MRJob):

    OUTPUT_PROTOCOL = CsvProtocol

    def mapper(self, _, line):

        article_id = line.split('<<sep>>')[0]

        if article_id in selected_ids:
            yield 'key', line

    def reducer(self, key, record):
        yield record


if __name__ == '__main__':
    RandomSubsample.run()
