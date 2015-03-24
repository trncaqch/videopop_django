from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import logout, authenticate, login, logout
from app.forms import UserForm, UserProfileForm
from django.contrib.auth.decorators import login_required
from models import Score
from gameViews import *

def index(request):
    restart()
    if request.user.is_authenticated():
        user = request.user
        top_scores = Score.objects.filter(user=user).order_by('-score')[:5]
        last_scores = Score.objects.filter(user=user).order_by('-date')[:5]
        context_dict = {"top_scores": top_scores,
                        "last_scores": last_scores}
    else:
        top_scores = Score.objects.order_by('-score')[:10]
        context_dict = {"top_scores": top_scores}
    return render(request, 'app/index.html', context_dict)

def register(request):
    # A boolean value for telling the template whether the registration was successful.
    registered = False

    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            registered = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print user_form.errors, profile_form.errors

    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    # Render the template depending on the context.
    return render(request,
            'app/register.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered} )



def user_login(request): 
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/vidpop/')
            else:

                return HttpResponse("Your account is disabled.")
        else:
            # Bad login details were provided.
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render(request, 'app/login.html', {})



@login_required
def user_logout(request):

    logout(request)
    return HttpResponseRedirect('/vidpop/')
