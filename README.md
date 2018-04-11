# Wikipedia-Edits-Distributed-Computing

# Authors  
Kevin, Lydia, Fanny, Xiaotai
 
# Data Set
[SNAP (Stanford)](https://snap.stanford.edu/data/wiki-meta.html) ~8GB zipped (~290GB unzipped) file with all of Wikipedia's revisions from its inception in 2001 to January 2008.  

# Questions of Interest
### The lifecycle of a page
* Can we cluster life cycles?
* What were the most revised articles of all time?

### Categories
* What attributes of article edit behavior can we glean from article categories? 
* How does edit behavior reflect major events in news, culture, tech, or history? 
   
# Randomly Sample 1000 Article IDs 
* Generate a list of unique article_ids  
    `/unique-articles`  
    
* Collect all article revisions associated with each unique article_id  
    `/random-subsample`
    
# Compare Revisions  
* Normalize revisions
    `/normalized-revision`  
* Look at creation timeline  
    `/creation-timeline`  

# Calculate Metadata for Entire Corpus  
* repeat steps above for entire dataset instead of sample  
    
# Analysis  
See this repo:  
https://github.com/Kevinisagirl/Wikipedia-Revisions-1000-articleid-sample

# Presentation  
See slides here:  
https://docs.google.com/presentation/d/1LYECSEUcr-U4f8_LEu3NOtIeOdiGqwZKGR-7UpIUO58/edit

# Development  

### Run   

Run `python3 unique_article.py`  
Otherwise the base python2.7 will scream at you.

### How to read head of gz file  
```
$ gzip -cd enwiki-20080103.good.gz | head -n 1
$ gzip -cd unique_all_articleids_3.gz | head -n 10
```

### File Tree  
```
.
├── README.md
├── creation-timeline
│   └── creation_timelines_toCSV.py
├── data
│   ├── all_revisions_1000_articles.txt
│   ├── all_revisions_1000_articles_caratseparated.txt
│   ├── all_revisions_1000_articles_commaseparated.txt
│   └── unique_all_articleids.gz
├── mrjob.conf
├── mrjob2.conf
├── normalized-revision
│   ├── create_normalized_revision_count_timeline.py
│   ├── create_normalized_revision_lengths_timeline.py
│   └── revision_count_timeline_2.py
├── random-subsample
│   ├── get_random_subsample.py
│   ├── get_random_subsample_toCSV.py
│   └── test_random_subsample.py
├── test
│   ├── blank_line_check.py
│   └── checking_format.py
└── unique-articles
    ├── unique-article
    ├── unique_article.py
    └── unique_article_ids.py

```
