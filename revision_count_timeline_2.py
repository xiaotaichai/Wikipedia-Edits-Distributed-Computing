from mrjob.job import MRJob
from mrjob.protocol import TextValueProtocol
import datetime as dt

class RevisionTimeline(MRJob):

    #OUTPUT_PROTOCOL = TextValueProtocol

    def mapper(self, _, line):
        data = line.split('<<sep>>')
        if len(data) == 18:
            article_id = data[0]
            article_name = data[2]
            revision_date = dt.datetime.strptime(data[3],'%Y-%m-%dT%H:%M:%SZ')

            revision_day = (revision_date - dt.datetime(2001,1,1)).days
            revision_time = (revision_date - dt.datetime(2001,1,1)).seconds
            revision_length = data[-1]

            yield (article_id, article_name), (revision_day,revision_time,revision_length)


    def reducer(self, key, revisions):
        creation_day = 1e6
        creation_time = 1e6
        num_revisions = 0
        revisions = list(revisions)
        for r in revisions:
            revision_day = r[0]
            revision_time = r[1]

            if revision_day < creation_day:
                creation_day = revision_day
                creation_time = revision_time

            elif revision_day == creation_day:
                if revision_time < creation_time:
                    creation_time = revision_time
            num_revisions += 1

        normalized_revision_timeline = [(r[0] - creation_day, r[1] - creation_time, r[2])for r in revisions]

        yield key, normalized_revision_timeline
if __name__ == '__main__':
    RevisionTimeline.run()