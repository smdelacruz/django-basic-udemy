Djando tutorial from [Udemy - Django for Beginners](https://www.udemy.com/course/introdjango/)

Commands

> `django-admin startproject leavesite` #Create a django project leavesite 
>
> `python manage.py startapp polls` Create an app inside the project called polls 
>
> `python manage.py runserver` Starting development server at http://127.0.0.1:8000/
>
> `python manage.py shell` Interactive console of django 

Add data to database

using `python manage.py shell`, execute the following command line by line

    >>>> import django
    >>>> django.setup()
    >>>> from django.utils import timezone
    >>>> q = Question(question_text="what's your name", pub_date=timezone.now())
    >>>> q.save()
    >>>> Question.objects.all()
    <QuerySet [<Question: what's your name>]>
    >>>> q = Question.objects.get(pk=1)
    >>>> q.choice_set.create(choice_text="bob", votes=0)
    >>>> q.choice_set.create(choice_text="betty", votes=0)
    >>>> q.choice_set.create(choice_text="frank", votes=0)
    >>>> q.save()
    >>>> exit()
    
> `python manage.py makemigrations`
> `python manage.py migrate`
> `python manage.py createsuperuser` Create a Super user; follow the prompt and fill out form
#http://127.0.0.1:8000/admin/ --> superuser