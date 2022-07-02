from distutils.command.upload import upload
from xml.dom.domreg import registered
from django.db import models
from django.contrib.auth.models import User

from dajngo_day_4.basic_app.forms import UserProFileInfoForm



def register(request):
    registered = False

    if request.method =="POST"
        user_form = UserForm(data=request.POST)
        profile_form = UserProFileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

                user = user_form.save()
                user.set_password(user.password)
                user.save()

                profile = profile_form.save(commit=False)
                profile.user = user

class UserProFileInfo(models.Model):

    user = models.OneToOneField(User)


    portfolio_site = models.URLField(blank=True)

    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)

    


    def __str__(self):
        return self.user.username