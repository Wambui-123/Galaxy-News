from flask import Flask, render_template
from newsapi import NewsApiClient
from flask_navigation import Navigation
import datetime

app= Flask(__name__)
@app.route('/')
  
def home():
  # enter api key and client key for authorization
  newsapi= NewsApiClient(api_key="e9ac9316fc2c41eeab50e67e45e97a4b")
    # top highlights
  top_headlines = newsapi.get_top_headlines(sources="bbc-news")
    # all articles
  all_articles = newsapi.get_everything(sources="bbc-news")
    # Fetch all the top headlights
  t_articles = top_headlines['articles']
  #Fetch all articles  
  a_articles = all_articles['articles']

  #Things I want stored
  news = []
  author = []
  desc = []
  img = []
  p_date = []
  url = []
  content = []
  #fetch content from all articles using for loop
  for i in range(len(t_articles)):
    main_article = t_articles[i]
    # Append contents to list 
    news.append(main_article["title"])
    author.append(main_article["author"])
    desc.append(main_article["description"])
    img.append(main_article["urlToImage"])
    p_date.append(main_article["publishedAt"])
    url.append(main_article["url"])
    content.append(main_article["content"])
    
  # Create list for all articles
  news_all = []
  author_all = []
  desc_all = []
  img_all = []
  p_date_all = []
  url_all = []
  content_all = []
# For loop
  for j in range(len(a_articles)): 
    a_article = a_articles[j]
    
#Append the articles into the list
  news_all.append(a_article["title"])
  author_all.append(a_article["author"])
  desc_all.append(a_article["description"])
  img_all.append(a_article["urlToImage"])
  p_date_all.append(a_article["publishedAt"])
  url_all.append(a_article["url"])
  content_all.append(a_article["content"])     
  
  contents = zip(news,author,desc,img,p_date,url,content)
  all = zip(news_all,author_all,desc_all,img_all,p_date_all,url_all,content_all)
  return render_template('home.html', contents=contents, all=all) 
  
  
if __name__ == '__main__':
  app.run(debug=True)  
#     nav.Bar('top', [
#     nav.Item('home', 'news'),
#     ])
  
  # newsapi= NewsApiClient(api_key="e9ac9316fc2c41eeab50e67e45e97a4b")
  # all_articles = newsapi.get_everything(sources="bbc-news")
  # a_articles = all_articles['articles']




    
  #merge them in a zip
  #pass it in rendered file
# x = datetime.datetime.now()
# time = x.strftime("%I:%M:%p")
# print(time)


