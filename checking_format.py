from mrjob.job import MRJob
import gzip

class CheckFormat(MRJob):

    def mapper(self, _, line):

        record = line.split('\x1e')
        revision_info = record[0].split(' ')
        record_length = len(record)
        rev_info_length = len(revision_info)

        if rev_info_length != 7:
            if record_length != 13:
                yield 'record length and revision info length is bad', 1
            else:
                yield 'revision info length bad, record length good', 1
        else:
            if record_length != 13:
                yield 'record length bad, revision info length good', 1
            else:
                yield 'revision info length and record length good', 1


    def reducer(self, key, values):
        yield key, sum(values)


if __name__ == '__main__':
    CheckFormat.run()
