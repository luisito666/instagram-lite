from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):
    """ Modelo de los Post de los usuarios
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey('users.Profile', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='posts/photos')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s by %s' % ( self.title, self.user.username )
    
    def __repr__(self):
        return '<Post Title: (%s) and User: (%s) >' % (self.title, self.user.username)
