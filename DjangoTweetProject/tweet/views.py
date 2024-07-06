from django.shortcuts import render
from .models import *
from .forms import *
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
def index(request):
    return render(request, 'tweet/index.html')

def display_tweet(request):
    tweets = Tweet.objects.all()
    return render(request, 'tweet/display_tweet.html',{'tweets':tweets})
@login_required
def create_tweet(request):
    if request.method=='POST':
        form = TweetForm(request.POST,request.FILES)
        if form.is_valid():
            tweet=form.save(commit=False)
            tweet.user=request.user
            tweet.save()
            return redirect('display_tweet')
    else:
        form = TweetForm()

    return render(request,'tweet/tweet_form.html',{'form':form})
@login_required
def update_tweet(request,id):
    tweet=get_object_or_404(Tweet,pk=id,user=request.user)
    if request.method=='POST':
        form = TweetForm(request.POST,request.FILES,instance=tweet)
        if form.is_valid():
            tweet=form.save(commit=False)
            tweet.user=request.user
            tweet.save()
            return redirect('display_tweet')
    else:
        form = TweetForm(instance=tweet)

    return render(request,'tweet/tweet_form.html',{'form':form})

@login_required
def delete_tweet(request, id):
    tweet=get_object_or_404(Tweet,pk=id,user=request.user)
    if request.method=='POST':
        tweet.delete()
        return redirect('display_tweet')

    return render(request,'tweet/tweet_delete.html',{'tweet':tweet})

def register(request):
    if request.method=='POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request,user)
            return redirect('display_tweet')
            
    else:
        form = UserRegistrationForm()
    return render(request,'registration/register.html',{'form':form})
    