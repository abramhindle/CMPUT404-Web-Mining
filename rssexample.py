import feedparser
import difflib
import json
cbc = feedparser.parse("http://rss.cbc.ca/lineup/topstories.xml")
print(json.dumps(cbc))
print("\n\n################################################\n\n")
cnn = feedparser.parse("http://rss.cnn.com/rss/cnn_topstories.rss")
print(json.dumps(cnn))
print("\n\n################################################\n\n")
cbc_titles = [x['title'] for x in cbc.get('entries')]
cnn_titles = [x['title'] for x in cnn.get('entries')]
res = [(x,difflib.get_close_matches(x,cbc_titles,1,0.01)) for x in
            cnn_titles]
print(json.dumps(res))
