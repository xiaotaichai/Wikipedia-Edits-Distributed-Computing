from mrjob.job import MRJob
import gzip

class CheckFormat(MRJob):

    def mapper(self, _, line):

        record = line.split('\x1e')
        revision_info = record[0].split(' ')

        if len(revision_info) != 7:
            yield 'revision info not good', 1
        else:
            yield 'revision info good', 1

    def reducer(self, key, values):
        yield key, sum(values)


if __name__ == '__main__':
    CheckFormat.run()
