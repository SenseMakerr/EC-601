import sys
import string
import twitter_sentiment_analysis


if __name__ == '__main__':
    keyword = 'Boston''house'
    num = 100
    twitter_sentiment_analysis.sentiment_analysis(keyword, num)