from django.shortcuts import render
from .utils import analyze_sentiment

def sentiment_view(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        if text:
            sentiment = analyze_sentiment(text)
            return render(request, 'sentiment/result.html', {'sentiment': sentiment, 'text': text})
    return render(request, 'sentiment/index.html')
