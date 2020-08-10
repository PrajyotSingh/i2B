from django.db import models

class Influencers(models.Model):
    FirstName=models.CharField(max_length=200,null=True)
    LastName=models.CharField(max_length=200,null=True)
    Email=models.EmailField(max_length=200,null=True)
    Mobile=models.IntegerField(null=True)
    Username=models.CharField(max_length=200,null=True)
    Followers=models.CharField(max_length=30,choices=[('1k-5k','1k-5k'),('5k-10k','5k-10k'),('10k-20k','10k-20k'),('20k-50k','20k-50k'),('>50k','>50k')],null=True)
    Category=models.CharField(max_length=30,choices=[('Lifestyle','Lifestyle'),('Food','Food'),('Fashion','Fashion'),('Artist','Artist'),('Makeup','Makeup'),('Mom','Mom'),('Blogger','Blogger'),('Travel','Travel'),('Others','Others')],default='Others', blank=True,null=True)
    Others=models.CharField(max_length=100,null=True)

    def __str__(self):
        return "{} {}".format(self.FirstName,self.LastName)

class Brands(models.Model):
    FirstName=models.CharField(max_length=200,null=True)
    LastName=models.CharField(max_length=200,null=True)
    Email=models.EmailField(max_length=200,null=True)
    Mobile=models.IntegerField(null=True)
    BrandName=models.CharField(max_length=200,null=True)

    def __str__(self):
        return "{}".format(self.BrandName)
