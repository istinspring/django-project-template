# django project template

I made it to reduce hours which is needed to bootstrap django project "as it should be".

Libs used:
* [Django](https://www.djangoproject.com/)
* [Fabric](http://docs.fabfile.org/en/1.8/)
* [Django Rest Framework](http://www.django-rest-framework.org/)
* [Django Suit](http://djangosuit.com/)

How to start (linux/osx):
* Clone project from github `git@github.com:istinspring/django-project-template.git`
* Rename project folder and 'cd' to it.
* Create virtualenv `virtualenv .env` and activate it `source .env/bin/activate`
* Install requirements `pip install -r requirements/dev.txt`
* Generate secret_key.py file `fab generate_secret_key_file`
* Create database `python manage.py syncdb`
* You'll need to [install bower](http://bower.io/#installing-bower) to manage front-end dependencies
* go to "static" folder and run `bower install`
* Finally run - `python manage.py runserver`

Future:
* Add more libs like south/sorl.thumbnail
* Configure Django-rest-framework
* Make a demo
* Deployment scripts for ec2/digitalocean/heroku
