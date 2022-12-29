import matplotlib.pyplot as plt
from wordcloud import WordCloud ,STOPWORDS
import sys,os
text=open('abcd1.txt',mode='r',encoding='utf-8').read()
stopwords=STOPWORDS
wc=WordCloud(
    background_color='white',
    stopwords=stopwords,
    height=600,
    width=400
    )
wc.generate(text)

wc.to_file('sample_output.png')
