from mrjob.job import MRJob


class BlankLineCheck(MRJob):

    def mapper(self, _, line):

        line = line.strip()

        if line:
            yield 'Not blank', 1
        else:
            yield 'Blank', 1

    def reducer(self, key, values):
        yield key, sum(values)


if __name__ == '__main__':
    BlankLineCheck.run()
