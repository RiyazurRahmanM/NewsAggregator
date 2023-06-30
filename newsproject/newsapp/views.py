from django.shortcuts import render
import requests
# Create your views here.
def index(request):
    r = requests.get('http://api.mediastack.com/v1/news?access_key=e7be5ca97ec06854fa1bfd24cc19a835&keywords=tennis&countries=us')
    res = r.json()
    data = res['data']
    title = []
    description = []
    url = []
    image = []

    for i in data:
        title.append(i['title'])
        description.append(i['description'])
        url.append(i['url'])
        image.append(i['image'])

    news = zip(title,image,description,url)

    return render(request,'newsapp/index.html',{'news':news})