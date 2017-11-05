from flask import render_template
import feedparser
from flask import Flask
app=Flask(__name__)
RSS_FEEDS= {'bbc': 'http://feeds.bbci.co.uk/news/rss.xml',
'cnn': 'http://rss.cnn.com/rss/edition.rss',
'fox': 'http://feeds.foxnews.com/foxnews/latest',
'iol': 'http://www.iol.co.za/cmlink/1.640'}
@app.route("/")
@app.route("/<production>")
def get_news(production='bbc'):
    feed=feedparser.parse(RSS_FEEDS[production])
    # first_article=feed['entries'][0]
    # return render_template("home.html", article=first_article)
    return render_template("home.html",articles=feed["entries"])
# @app.route("/")
# @app.route("/bbc")
# def bbc():
#     return get_news('bbc')
# @app.route("/cnn")
# def cnn():
#     return get_news('cnn')
#
if __name__=="__main__":
    app.run(port=5000,debug=True)


