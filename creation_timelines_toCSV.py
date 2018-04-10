import os
import re

progress = 0
outfile = open('./creation_timelines_5yrs.csv', 'w')
# write header
outfile.write('article_id,article_name,creation_datetime,num_revisions,all_revisions\n')

line_pattern = '\["([0-9]+?)", "(.+?)"\]\s*\["([0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2})", ([0-9]+?), \[(.+)\]\]'
with open('./creation_timelines_5yrs_new.txt','r') as infile:
    for line in infile:
        parts = list(re.findall(line_pattern, line)[0])
        # remove qutoes from the revision authour usernames
        parts[4] = re.sub('"','',parts[4])

        new_line = '{0},"{1}",{2},{3},"{4}"\n'.format(parts[0],parts[1],parts[2],parts[3],parts[4])
        outfile.write(new_line)

        progress += 1

        if progress%10000 == 0:
            print('{} lines processed so far'.format(progress))
outfile.close()
print('Done')
