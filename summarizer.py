import tkinter as tk
import nltk
from textblob import TextBlob
from newspaper import Article
nltk.download('punkt')

def summarize():
    url = utext.get('1.0', "end").strip()
    article = Article(url)
    article.download()
    article.parse()
    article.nlp()

    title.config(state='normal')
    author.config(state='normal')
    publication.config(state='normal')
    utext.config(state='normal')
    summ.config(state='normal')
    sentiment.config(state='normal')

    title.delete('1.0', 'end')
    title.insert('1.0', article.title)

    author.delete('1.0', 'end')
    author.insert('1.0', article.authors)

    publication.delete('1.0', 'end')
    publication.insert('1.0', article.publish_date)

    summ.delete('1.0', 'end')
    summ.insert('1.0', article.summary)

    analysis = TextBlob(article.text)
    sentiment.delete('1.0','end')
    sentiment.insert('1.0',f'polarity:{analysis.polarity} sentiment:{"positive" if analysis.polarity>0 else "negative" if analysis.polarity<0 else "neutral"}')

    title.config(state='disabled')
    author.config(state='disabled')
    publication.config(state='disabled')
    utext.config(state='disabled')
    summ.config(state='disabled')
    sentiment.config(state='disabled')
root = tk.Tk()
root.title("Article Summary")
root.geometry('1200x600')

# title part
tlable = tk.Label(root, text='TITLE')
tlable.pack()
title = tk.Text(root, height=1, width=100)
title.config(state='disabled', bg='#dddddd')
title.pack()

# author part
alable = tk.Label(root, text='AUTHOR')
alable.pack()
author = tk.Text(root, height=1, width=150)
author.config(state='disabled', bg='#dddddd')
author.pack()

# publish date
plable = tk.Label(root, text='PUBLISHING DATE')
plable.pack()
publication = tk.Text(root, height=1, width=150)
publication.config(state='disabled', bg='#dddddd')
publication.pack()

# url part
ulable = tk.Label(root, text='URL')
ulable.pack()
utext= tk.Text(root, height=1, width=100)
utext.pack()

# summary part
slable = tk.Label(root, text='SUMMARY')
slable.pack()
summ= tk.Text(root, height=20, width=150)
summ.config(state='disabled', bg='#dddddd')
summ.pack()

# sentiment part
sentlable = tk.Label(root, text='SENTIMENT')
sentlable.pack()
sentiment = tk.Text(root, height=1, width=150)
sentiment.config(state='disabled', bg='#dddddd')
sentiment.pack()

# button part
btn = tk.Button(root, text='SUMMARIZE!!', command=summarize)
btn.pack()




root.mainloop()
