
from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    # return HttpResponse('Hello')
    return render(request, 'home.html')     #, {'hithere': 'This is me'}

def eggs(request):
    return HttpResponse('<h1>Eggs are great!!</h1>')

def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()

    worddictionary = dict()

    for word in wordlist:
        if word in worddictionary:
            # Increase
            worddictionary[word] += 1
        else:
            # add to dictionary
            worddictionary[word] = 1

    sortedwords = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html', {'fulltext': fulltext, 'count': len(wordlist), 'worddictionary': worddictionary, 'sortedwords': sortedwords})

def about(request):
    # return HttpResponse('Hello')
    return render(request, 'about.html')