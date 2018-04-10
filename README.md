# Wikipedia-Edits-Distributed-Computing

 
# Questions of Interest
*  What are the most commonly edited Wikipedia articles?
* What trends & behaviours can we discern from article revision history?
* Do popular revisions coincide with current events, history, or pop culture?   

# Data Set
SNAP (Stanford) compressed zip file with all of Wikipedia's revisions from its inception in 2001 to January 2008.  

# Initial Sampling Worfklow  
* Generate a list of unique article_ids  
* Aggregate attributes associated with each article_id  

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
