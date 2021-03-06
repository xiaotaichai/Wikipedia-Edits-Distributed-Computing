from mrjob.job import MRJob
from mrjob.protocol import TextValueProtocol

class RevisionCountTimeline(MRJob):

    #OUTPUT_PROTOCOL = TextValueProtocol

    def mapper(self, _, line):

        record = line.split('\x1e')
        article_info = record[0].split(' ')

        article_id = article_info[1]
        article_name = article_info[3]
        revision_date = article_info[4]

        yield [article_id, article_name], revision_date

    def reducer(self, key, records):
        monthly_revision_count = [0]*96
        for record in records:
            year, month = record.split('-')[0], record.split('-')[1]
            index = (int(year) - 2001)*12 + int(month) - 1
            monthly_revision_count[index] += 1

        normalized = [float(i)/sum(monthly_revision_count) for i in monthly_revision_count]
        yield key, normalized

if __name__ == '__main__':
    RevisionCountTimeline.run()
