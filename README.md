To install it, please do the following:

    Clone this repository on your local machine by opening a terminal and running: 
		git clone https://github.com/2087939a/group_project_django.git
		
    Create a new virtual enviroment and run:
		pip install -r requirements.txt
		
    Navigate to the root of the Django application and run the following commands in a terminal:
        python manage.py syncdb
        python manage.py migrate
        python populate.py

The application can now be run by typing python manage.py runserver inside a terminal. To explore it, please log in with one of the following test accounts:

    Username: test1 Password: pass
    Username: test2 Password: pass
    Username: test3 Password: pass
    Username: test4 Password: pass

Of course, you can always create a new account.

You should also create a superuser as it allows adding videos from the site itself.

This application is deployed to http://vidpop.pythonanywhere.com/vidpop/