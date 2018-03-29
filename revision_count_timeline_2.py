from mrjob.job import MRJob
from mrjob.step import MRStep
from mrjob.protocol import TextValueProtocol
import datetime as dt

class RevisionTimeline(MRJob):

    # OUTPUT_PROTOCOL = TextValueProtocol

    def mapperGroupRevisions(self, _, line):
        record = line.split('\x1e')
        article_info = record[0].split(' ')

        article_id = article_info[1]
        article_name = article_info[3]

        revision_datetime_str = article_info[4]
        # revision_datetime = dt.datetime.strptime(article_info[4],'%Y-%m-%dT%H:%M:%SZ')
        # revision_day = (revision_date - dt.datetime(2001,1,1)).days
        # revision_time = (revision_date - dt.datetime(2001,1,1)).seconds

        revision_length = int(record[12].split(' ')[1])
        minor_flag = int(record[11].split(' ')[1])
        # yield (article_id, article_name), (revision_day,revision_time,revision_length)
        yield (article_id, article_name), (revision_datetime_str, revision_length, minor_flag)


    def reducerFindCreation(self, key, revisions):
        # creation_day = 1e6
        # creation_time = 1e6
        creation_datetime = dt.datetime.now()
        revisions = list(revisions)
        for r in revisions:
            revision_datetime = dt.datetime.strptime(r[0],'%Y-%m-%dT%H:%M:%SZ')
            if revision_datetime < creation_datetime:
                creation_datetime = revision_datetime

        creation_datetime_str = creation_datetime.strftime('%Y-%m-%dT%H:%M:%SZ')
        num_revisions = len(revisions)
        yield key , [revisions, creation_datetime_str, num_revisions]

    def reducerCreateTimeline(self, key, values):

        # normalized_revision_timeline = [(r[0] - creation_day, r[1] - creation_time, r[2])for r in revisions]
        # normalized_revision_timeline = [((dt.datetime.strptime(r[0],'%Y-%m-%dT%H:%M:%SZ') - creation_datetime).days, (dt.datetime.strptime(r[0],'%Y-%m-%dT%H:%M:%SZ') - creation_datetime).seconds ,r[1], r[2]) for r in revisions]
        num_revisions = values[2]
        normalized_revision_timeline = []*num_revisions
        
        creation_datetime = dt.datetime.strptime(values[1],'%Y-%m-%dT%H:%M:%SZ')
        revisions = values[0]
        i = 0
        for r in revisions:
            revision_datetime = dt.datetime.strptime(r[0],'%Y-%m-%dT%H:%M:%SZ')
            time_since_creation = revision_datetime - creation_datetime
            normalized_revision_timeline[i] = [time_since_creation.days, time_since_creation.seconds, r[1], r[2]]
            i += 1
        yield key + (creation_datetime.strftime('%Y-%m-%d %H:%M:%S', num_revisions), normalized_revision_timeline

    def steps(self):
        return [
            MRStep(mapper=self.mapperGroupRevisions,
                   reducer=self.reducerFindCreation),
            MRStep(reducer=self.reducerCreateTimeline)
        ]

if __name__ == '__main__':
    RevisionTimeline.run()
