from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

# after creating a new model make migrations (python manage.py makemigrations)
#then migrate (python manage.py migrate)
#and if you want to add this model to admin then go to ..
# this app's admin.py and put this code [


#from .models import Blog
 #admin.site.register(Blog)

#]
