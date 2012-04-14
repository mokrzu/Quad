##Quad (author: Lukasz Mokrzycki)
- - - 
Q & A example Django web application, that uses Mongo database.

> I used mongoengine to connect with mongo database, to achive that
> documents models should be placed in init file (application directory)
> not it the models.py, connection to database starts also in init (quad direvtory)

Dependencies:
+ working mongo instance (install mongodb and run mongod proccess)
+ mongoengine
+ django (i used django 1.4 version)

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
