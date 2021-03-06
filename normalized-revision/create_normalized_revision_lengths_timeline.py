from mrjob.job import MRJob
from mrjob.protocol import TextValueProtocol

class RandomSubsample(MRJob):

    #OUTPUT_PROTOCOL = TextValueProtocol

    def mapper(self, _, line):

        #
        # article_id = line.split('<<sep>>')[0]
        # article_name = line.split('<<sep>>')[2]
        # revision_date = line.split('<<sep>>')[3]
        # revision_length = line.split('<<sep>>')[-1]
        line = line.strip()
        if line:
            parts = line.split('<<sep>>')
            article_id = parts[0]
            article_name = parts[2]
            revision_date = parts[3]
            revision_length = parts[-1]

            yield [article_id, article_name], [revision_date, revision_length]

    def reducer(self, key, records):
        monthly_revision_count = [0]*96
        for record in records:
            year, month = record[0].split('-')[0], record[0].split('-')[1]
            index = (int(year) - 2001)*12 + int(month) - 1
            monthly_revision_count[index] += int(record[1])

        normalized = [float(i)/sum(monthly_revision_count) for i in monthly_revision_count]
        yield key, normalized

if __name__ == '__main__':
    RandomSubsample.run()
