from mrjob.job import MRJob
from mrjob.step import MRStep
# from mrjob.protocol import TextValueProtocol
import datetime as dt

class RevisionTimeline(MRJob):

    # OUTPUT_PROTOCOL = TextValueProtocol

    def mapperGroupRevisions(self, _, line):
        record = line.split('\x1e')
        article_info = record[0].split(' ')

        article_id = article_info[1]
        article_name = article_info[3]

        revision_datetime_str = article_info[4]
        user_name = article_info[5]
        user_id = article_info[6]
        revision_length = int(record[12].split(' ')[1])
        minor_flag = int(record[11].split(' ')[1])

        yield [article_id, article_name], [revision_datetime_str, revision_length, minor_flag, user_name, user_id]


    def reducerCreateTimeline(self, key, revisions):
        creation_datetime = dt.datetime.now()
        revisions = list(revisions)

        # find the date of creation, i.e. the date of oldest revision
        for r in revisions:
            revision_datetime = dt.datetime.strptime(r[0],'%Y-%m-%dT%H:%M:%SZ')
            if revision_datetime < creation_datetime:
                creation_datetime = revision_datetime


        # check if creation was before 01-01-03, so each article has at least a five year history

        if creation_datetime < dt.datetime.strptime('2003-01-01','%Y-%m-%d'):
            num_revisions = len(revisions)
            normalized_revision_timeline = [[] for i in range(num_revisions)]

            i = 0
            for r in revisions:
                revision_datetime = dt.datetime.strptime(r[0],'%Y-%m-%dT%H:%M:%SZ')
                time_since_creation = revision_datetime - creation_datetime
                normalized_revision_timeline[i] = [time_since_creation.days, time_since_creation.seconds, r[1], r[2],r[3],r[4]]
                i += 1


            yield key , [creation_datetime.strftime('%Y-%m-%d %H:%M:%S'), num_revisions, normalized_revision_timeline]

    def steps(self):
        return [
            MRStep(mapper=self.mapperGroupRevisions,
                   reducer=self.reducerCreateTimeline)
        ]

if __name__ == '__main__':
    RevisionTimeline.run()
