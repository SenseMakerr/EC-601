# encoding: utf-8
from textblob import TextBlob
import tweepy
import sys

# request API
consumer_key = "XwK3IS0ldbT4FZ5fYLbZ3wDnU"
consumer_secret = "ytl8OhWaR1xGyO43JC0nfHkOD3e6SjghgKq7t5FVebYaee1zaM"
access_token = "1579831536119156741-4CF8Y5ehj9kmINXnLRcUlAnRTXsGAN"
access_token_secret = "lnLf5QuTKqZp7PktjzRHlpOqdYTdQsiRO9VVT4QZ80Vt6"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


def sentiment_analysis(keyword, num):
    # keyword = 'League of Legends', 'LoL'
    # retrieve tweets
    tweets = tweepy.Cursor(api.search_tweets, q='League of Legends', lang="en").items(num)

    # retrieve text in every tweet and remove repeat
    text_set = set()
    for tweet in tweets:
        text_set.add(tweet.text)
        # with open("example.txt", "a+") as f:
        #     f.write(str(tweet))

    # sentiment analysis with polarity and subjectivity
    polarity_score = []
    # subjectivity_score = []
    for text in text_set:
        analysis = TextBlob(text)
        # print(text)
        polarity_score.append(analysis.sentiment.polarity)
        # subjectivity_score.append(analysis.sentiment.subjectivity)

    # compute the sentiment score
    sum = 0
    length = len(polarity_score)
    count = 0
    for sentence in range(length):
        sum += polarity_score[sentence]
        if polarity_score[sentence] == 0:
            count = count + 1
        print(f"The polarity score of sentence {sentence} is {polarity_score[sentence]}")
    average = sum / (length - count)

    # output
    print(f"The total sentiment score of the {keyword}is {sum}")
    print(f"The average sentiment score of the {keyword}is {average}")

    # polarity judgement
    if average > 0:
        print("nice product!")
    else:
        print("not recommended product!")
    return





