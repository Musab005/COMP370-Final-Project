# COMP370-Final-Project

Usage (from root directory \COMP370-Final-Project):
1) `python -m scripts.newsapi`           -> data\articles.json
2) `python -m scripts.extract_to_csv`    -> data\articles.csv

## project description
### A politician in the media
Your team has been hired by a media company that wants to understand how Elon Musk is being covered in the media. 
They have indicated that they are especially concerned with North American coverage and 

(1) whether coverage is positive or negative

(2) what topics the coverage focuses on.

You will conduct this analysis and submit a report discussing your findings.

### Analysis Details
Your analysis will draw on news articles drawn from the NewsAPI.org. To inform your analysis, you should 
collect at least 500 articles on this political figure from North American news outlets (ensure that you 
thoughtfully select these news sources).

To develop your topics, conduct an open coding on 200 articles (approach the exercise requiring each article
to belong to exactly one topic). For your open and later codings, just use the title and opening of the article 
(i.e., you don’t need to read the entire article). You should aim for between 3-8 topics in total.

Once your topics have been designed, manually annotate the rest of the articles in your dataset. While double 
annotation would usually be used, for this project (given time constraints), use single annotation.

Characterize your topics by computing the 10 words in each category with the highest tf-idf scores (to compute 
inverse document frequency, use all 500 articles that you originally collected.

Conduct a second coding of the posts by assessing whether they are positive, negative, or neutral about the 
politician. Bear in mind that you will need to develop a defensible way in which to interpret these categories.
