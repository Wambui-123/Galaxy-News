from flask import Flask, render_template
from newsapi import NewsApiClient
app= Flask(__name__)
@app.route('/')
def home():
  # enter api key and client key for authorization
  newsapi= NewsApiClient(api_key="e9ac9316fc2c41eeab50e67e45e97a4b")
  
  # top highlights
  top_headlines = newsapi.get_top_headlines(sources="bbc-news")
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
  #merge them in a zip
  contents = zip(news,author,desc,img,p_date,url,content)
  #pass it in rendered file
  return render_template('home.html', contents=contents)



if __name__ == '__main__':
  app.run(debug=True)
