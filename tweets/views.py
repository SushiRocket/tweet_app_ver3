from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from.models import Tweet
from.forms import TweetForm

# Create your views here.
@login_required
def tweet_list(request):
    tweets = Tweet.objects.all().order_by('-created_at')

    if request.method == 'POST':
        form = TweetForm(request.POST)
        if form.is_valid():
            new_tweet = form.save(commit=False)
            new_tweet.user = request.user
            new_tweet.save()
            return redirect('tweets:tweet_list')
    else:
        form = TweetForm()
    
    context = {
        'form': form,
        'tweets': tweets,
    }
    return render('tweet_list.html', context)