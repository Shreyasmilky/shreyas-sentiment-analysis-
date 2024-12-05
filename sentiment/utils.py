from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def analyze_sentiment(text):
    analyzer = SentimentIntensityAnalyzer()
    score = analyzer.polarity_scores(text)

    if score['compound'] >= 0.05:
        return 'Positive'
    elif score['compound'] <= -0.05:
        return 'Negative'
    else:
        return 'Neutral'
from django.shortcuts import render
from .utils import analyze_sentiment

def sentiment_view(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        if text:
            sentiment = analyze_sentiment(text)
            return render(request, 'sentiment/result.html', {'sentiment': sentiment, 'text': text})
    return render(request, 'sentiment/index.html')
