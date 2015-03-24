from django.shortcuts import render
from app.models import User, UserProfile
from django.http import HttpResponse

def userProfile(request, user_name):
    context_dict = {}
    try:
        user = User.objects.get(username=user_name)
        context_dict['username'] = user          
    except:
         pass

    try:
        profile = UserProfile.objects.get(user=user)
        context_dict['profile'] = profile
    except:
        pass
    
    return render(request, 'app/profile.html', context_dict)
