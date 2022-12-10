from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django import forms

from .models import User,Listing,Comments,Bids,Wishlist

class NewlistingForm(forms.Form):
    title = forms.CharField(label="title")
    category = forms.CharField(label="category")
    price=forms.IntegerField(label='price')
    image_url=forms.URLField()
    description= forms.CharField(widget=forms.Textarea(attrs={'style':'bottom:2rem'}))

class NewCommentForm(forms.Form):
    description= forms.CharField(widget=forms.Textarea(attrs={'style':'bottom:2rem'}))

class NewBidForm(forms.Form):
    price=forms.IntegerField(label='price')
    
def index(request):
    activelistings=Listing.objects.filter(is_active=True)
    return render(request, "auctions/index.html",{'activelistings':activelistings})


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


def addlisting(request):
    if request.method=="POST":
        form=NewlistingForm(request.POST)
        if form.is_valid():
            title=form.cleaned_data['title']
            category=form.cleaned_data['category']
            description=form.cleaned_data['description']
            price=form.cleaned_data['price']
            image_url=form.cleaned_data['image_url']
            
            user=User.objects.get(username=request.user)
            print(user)
            lisitng= Listing(posted_by=user,title=title, price=price, category=category,image_url=image_url,description=description,is_active=True)
            lisitng.save()
            return HttpResponseRedirect(reverse("index"))
    else:
        form =NewlistingForm()
        return render(request,'auctions/addlisting.html',{'form':form})


def listing(request,id):
    listing=Listing.objects.get(id=id)
    comments=Comments.objects.filter(listing_id=id)
    bids=Bids.objects.filter(listing_id=id)

    return render(request,'auctions/listing.html',{'listing':listing,'comments':comments,'bids':bids})


def addcomment(request,id):
    if request.method=="POST":
        form=NewCommentForm(request.POST)
        if form.is_valid():
            
            description=form.cleaned_data['description']
            user=User.objects.get(username=request.user)
            listingid=Listing.objects.get(id=id)
            comment= Comments(posted_by=user,description=description,listing_id=listingid)
            comment.save()
            return HttpResponseRedirect(reverse( "listing",kwargs={'id':id}))
        else:
            return HttpResponseRedirect(reverse( "listing",kwargs={'id':id}))
    else:
        
        return HttpResponseRedirect(reverse( "listing",kwargs={'id':id}))
    

def addbid(request,id):
    if request.method=="POST":
        form=NewBidForm(request.POST)
        if form.is_valid():
            
            price=form.cleaned_data['price']
            user=User.objects.get(username=request.user)
            listingid=Listing.objects.get(id=id)
            bid= Bids(posted_by=user,price=price,listing_id=listingid)
            bid.save()
            return HttpResponseRedirect(reverse( "listing",kwargs={'id':id}))
        else:
            return HttpResponseRedirect(reverse( "listing",kwargs={'id':id}))
    else:
        
        return HttpResponseRedirect(reverse( "listing",kwargs={'id':id}))


def viewwishlist(request):
    user=User.objects.get(username=request.user)
    wishlist=Wishlist.objects.filter(user_id=user)
    setdisplay=True
    if len(wishlist)==0:
        setdisplay=False
    return render(request,'auctions/wishlist.html',{'wishlist':wishlist,'setdisplay':setdisplay})


def addtowishlist(request,id):
    user=User.objects.get(username=request.user)
    listing_id=Listing.objects.get(id=id)
    print(user)
    wishlistobject=Wishlist(user_id=user,listing_id=listing_id)
    wishlistobject.save()
    
    return HttpResponseRedirect(reverse( "viewwishlist"))


