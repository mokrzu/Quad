##Quad (author: Lukasz Mokrzycki)
'Qestions & Answers' example Django web application, that uses Mongo database.

> I used mongoengine in order to connect with mongo database, to achive that
> documents models should be placed in init file (application directory)
> not it the models.py, connection to database starts also in init (quad directory).

Dependencies:

-   working mongo instance (install mongodb and run mongod proccess)
-   mongoengine
-   django (i used django 1.4 version)

Setup how-to:
    
    pip install mongoengine
    pip install django

    git clone git://github.com/mokrzu/Quad.git
    cd quad

    vim quad/settings.py
    # edit TEMPLATE_DIRS for your path

    python manage.py runserver

Now open browser at: http://127.0.0.1:8000/ 
- - -
Example interaction with database (from python shell in project dir):

# connect to mongo database
'''
    if you don't know database name, simply use mongo shell ("mongo" command),
    use "show dbs" to print all databases names, from here you could also test application
    for example: use "use quad_db" and next "db.author.find()" to print all Authors documents.
'''
>>> from mongoengine import *
>>> connect('quad_db')
Database(Connection('localhost', 27017), u'quad_db')

>>> from app import *

# print all question titles
>>> for question in Question.objects:
...     print question.title
... 
hello?
Who's there ?
How add mongo to django?
Awesome question?!

# add new question
>>> q = Question()
>>> q.title = "How to save that?"
>>> a = Author(name="me", email="me@example.com")
>>> a.save()
>>> q.content = "......."
>>> q.tags = ["short", "examples"]
>>> q.save
>>> q.save()
>>> Question.objects(title="How to save that?")[0].content
u'.......'

# delete question
>>> Question.objects(title="How to save that?")[0].delete()
>>> Question.objects(title="How to save that?")
[]

```
- - -
