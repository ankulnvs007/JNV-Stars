from django.db import models

# Create your models here.



class aluminies(models.Model):
    name = models.CharField(max_length=50, null=True)
    profession = models.CharField(max_length=70, null=True)
    batch = models.IntegerField( null=True)
    bio = models.TextField(max_length=1000, null=True)
    alumini_image = models.ImageField(upload_to="images", default='images/dpic.png' ,null=True, blank=True)
    education = models.CharField(max_length=100, null=True)
    college = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=500, null=True)
    phone = models.IntegerField(max_length=10, null=True)
    email = models.EmailField(max_length=100, null=True)
    twitter_link = models.URLField(blank=True, null=True)
    facebook_link = models.URLField(blank=True, null=True)
    insta_link = models.URLField(blank=True, null=True)
    linkdin_link = models.URLField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        ordering = ["-date_created"]

    def __str__(self):
        return self.name



class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, null=True)
    email = models.EmailField(max_length=100, null=True)
    message = models.TextField()
    time =models.DateTimeField(auto_now_add=True,blank=True)

    def __str__(self):
        return 'Message from ' + self.name