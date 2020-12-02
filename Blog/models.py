from django.db import models

# Create your models here.
class BlogPost(models.Model):
    blog_id= models.AutoField(primary_key=True)
    blog_heading=models.CharField(max_length=200)
    blog_content=models.CharField(max_length=2000)
    blog_subheading=models.CharField(max_length=100)
    blog_subContent=models.CharField(max_length=1000)
    blog_addedBy=models.CharField(max_length=50)
    blog_pubDate=models.DateField(auto_now=True)
    blog_image=models.ImageField(upload_to='media',default="")
    def __str__(self):
        return str(self.blog_id)+"_"+self.blog_heading