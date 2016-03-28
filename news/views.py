from django.shortcuts import render
from .models import Article, Feed
from .forms import FeedForm
from django.shortcuts import redirect

import feedparser
import datetime

def articles(request):
    articles = Article.objects.all() 
    
    rows = [articles[x:x+1] for x in range(0, len(articles), 1)]
    
    return render(request, 'news/articles.html', {'rows': rows})

def feeds(request):
    feeds = Feed.objects.all()
    return render(request, 'news/feeds.html', {'feeds': feeds})
    
def newFeed(request):
    if request.method == 'POST':
        form = FeedForm(request.POST)
        if form.is_valid():
            feed = form.save(commit=False)
            
            existingFeed = Feed.objects.filter(url = feed.url)
            
            if len(existingFeed) == 0:
                feedData = feedparser.parse(feed.url)
                
                feed.title = feedData.feed.title
                feed.save()
                
                for entry in feedData.entries:
                    article = Article()
                    article.title = entry.title
                    article.url = entry.link
                    article.description = entry.description
                    
                    d = datetime.datetime(*(entry.published_parsed[0:6]))
                    dateString = d.strftime('%Y-%m-%d %H:%M:%S')
                    
                    article.publicationDate = dateString
                    article.feed = feed
                    article.save()
                    
            return redirect('news.views.feeds') 
    else :
        form = FeedForm()
    return render(request, 'news/newFeed.html', {'form': form})