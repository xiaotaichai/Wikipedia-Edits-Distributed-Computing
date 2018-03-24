from mrjob.job import MRJob
from mrjob.protocol import TextValueProtocol
import datetime as dt

class RevCountTimeline(MRJob):

    #OUTPUT_PROTOCOL = TextValueProtocol

    def mapper(self, _, line):
        data = line.split('<<sep>>')
        if len(data) == 18:
            article_id = data[0]
            article_name = data[2]
            revision_date = dt.datetime.strptime(data[3],'%Y-%m-%dT%H:%M:%SZ')
            revision_day = (revision_date - dt.datetime(2001,1,1)).days
            revision_time = (revision_date - dt.datetime(2001,1,1)).seconds

            yield (article_id, article_name), (revision_day,revision_time)


    def reducer(self, key, revisions):
        monthly_revision_count = [0]*97
        creation_day = 1e6
        creation_time = 1e6
        for r in revisions:
            revision_date = r[0]
            revision_time = r[1]

            if revision_day < creation_day:
                creation_day = revision_day
                creation_time = revision_time

            elif revision_day == creation_day:
                if revision_time < creation_time:
                    creation_time = revision_time

        normalized_revision_times = [(r[0] - creation_day, r[1] - creation_time) for r in revisions]
        yield key, normalized_revision_times

if __name__ == '__main__':
    RevCountTimeline.run()
