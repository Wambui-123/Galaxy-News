from flask import Flask, render_template
from newsapi import NewsApiClient
import datetime

app= Flask(__name__)
@app.route('/')
  
def home():
  # enter api key and client key for authorization
  newsapi= NewsApiClient(api_key="e9ac9316fc2c41eeab50e67e45e97a4b")
  
    # all articles
  all_articles = newsapi.get_everything(sources="bbc-news")
  # top highlights
  top_headlines = newsapi.get_top_headlines(sources="bbc-news")
  #Fetch all articles  
  a_articles = all_articles['articles']
  # Fetch all the top headlights
  t_articles = top_headlines['articles']
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
    
  contents = zip(news,author,desc,img,p_date,url,content)
  return render_template('home.html', contents=contents)



  # Create list for all articles
def news():
  all = zip(news_all,author_all,desc_all,img_all,p_date_all,url_all,content_all)
  newsapi= NewsApiClient(api_key="e9ac9316fc2c41eeab50e67e45e97a4b")
  all_articles = newsapi.get_everything(sources="bbc-news")
  a_articles = all_articles['articles']

   
  news_all = []
  author_all = []
  desc_all = []
  img_all = []
  p_date_all = []
  url_all = []
  content_all = []
  
  for j in range(len(a_articles)): 
    main_all_articles = a_articles[j]

#Append the articles into the list
    news_all.append(main_all_articles["title"])
    author_all.append(main_all_articles["author"])
    desc_all.append(main_all_articles["description"])
    img_all.append(main_all_articles["urlToImage"])
    p_date_all.append(main_all_articles["publishedAt"])
    url_all.append(main_all_articles["url"])
    content_all.append(main_all_articles["content"])  
    
  #merge them in a zip
  #pass it in rendered file
  # return render_template('home.html', contents=contents, all=all)
x = datetime.datetime.now()
time = x.strftime("%I:%M:%p")
print(time)

  

if __name__ == '__main__':
  app.run(debug=True)
