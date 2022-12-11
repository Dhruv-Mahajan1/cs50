from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    id=models.AutoField(primary_key=True)



class Listing(models.Model):
    id=models.AutoField(primary_key=True)
    posted_by=models.ForeignKey(User ,on_delete=models.CASCADE)
    dateCreated=models.DateField(auto_now_add=True)
    title=models.CharField(max_length=50)
    description=models.CharField(max_length=200)
    price=models.IntegerField()
    image_url = models.URLField(max_length=500,default="https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.istockphoto.com%2Fphotos%2Fno-image-available&psig=AOvVaw35LvTbizKSyZNRhAnjDL-h&ust=1670775821403000&source=images&cd=vfe&ved=0CA8QjRxqFwoTCMjx7Iy77_sCFQAAAAAdAAAAABAE")
    category=models.CharField(max_length=80)
    is_active=models.BooleanField(default=True)
    
    

class Bids(models.Model):
    id=models.AutoField(primary_key=True)
    posted_by=models.ForeignKey(User ,on_delete=models.CASCADE)
    listing_id=models.ForeignKey(Listing,on_delete=models.CASCADE)
    dateCreated=models.DateField(auto_now_add=True)
    price=models.IntegerField()

class Comments(models.Model):
    id=models.AutoField(primary_key=True)
    posted_by=models.ForeignKey(User ,on_delete=models.CASCADE)
    listing_id=models.ForeignKey(Listing,on_delete=models.CASCADE)
    dateCreated=models.DateField(auto_now_add=True)
    description=models.CharField(max_length=200)


class Wishlist(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    listing_id=models.ForeignKey(Listing,on_delete=models.CASCADE)


class Winner(models.Model):
    listingid = models.ForeignKey(Listing,on_delete=models.CASCADE)
    bougthby_id = models.ForeignKey(User ,on_delete=models.CASCADE)
    winprice = models.IntegerField()