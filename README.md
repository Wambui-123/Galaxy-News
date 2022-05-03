# Galaxy-News
# Author
Yvonne Muthui

# Description
A flask application that has updated news for anyone to view and read at any given time. It has been created by the use of <a href="doc:introduction" target="_blank">Introduction</a>

# Link to live site




## User Story ( BDD ) 
The user would like to.... :
+  to see various news sources on the homepage of the application.
+ select a news source and see all news articles from the selected news source in the application.
+  see the image, description and the time a news article was created.
+ click on an article and read the full article on the source website.

## [Demo](https://news-galaxy.herokuapp.com/) click to view


## Installation / Setup instruction

#### The application requires the following installations to operate 
* python3
* flask v2 and above
* gunicorn
* bootstrap

#### Cloning

* Open Terminal {Ctrl+Alt+T}

* git clone ``https://github.com/Wambui-123/Galaxy-News.git``



* cd my_news_flask

* Vs code . or atom . based on the text editor you have.

### Running the Application
* To run the application, open the cloned file in terminal and run the following commands:
 * #### create flask environnent
        $  python3 -m venv pip virtual -- creates the virtual for runnning your app      
        $ source virtual/bin/env  -- activate  the virtual
        $ chmod +x launcher.py
        $ ./launcher.py
* #### Install Flask and other dependencies/Modules
        $ pip install flask
        $ pip install flask-Bootstrap ( optional)
* #### set up the API KEY
        + create account in [https://newsapi.org] and key will be issued
        + in root fold of your app create  a folder,config file in it and paste you API key and add it to .gitignore
        + alternatively have any python file in root folder and :
            export NEWS_API_KEY='<Your-Api-Key goes here>'
            python3 manage.py server
* #### Run app using vs terminal or main terminal
        $ chmod +x launch.sh
        $ ./launch.sh


## Technologies Used

* python3
* Flask Webframework


## Known Bugs
* There are no known bugs currently but pull requests are allowed incase you spot a bug
* also incase you run it a bug feel free to add or contact

## Contact Information 

If you have any question or contributions, please email me at [paulettenereah3@gmail.com](yvonnewambui28@gmail.com)




Portfolio- [Paullete](https://github.com/Wambui-123)
# Licence

Click to  [MIT License](Licence) view

 Copyright (c) 2022 | Yvonne Muthui