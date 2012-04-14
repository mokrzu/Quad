# Models for quad application
from mongoengine import *

# Author of question/answer
class Author(Document):
    email = StringField(required=True)
    name = StringField(max_length=50)

    def show(self):
        return (self.name + " (" + self.email + ")")

# Answet for Question
class Answer(EmbeddedDocument):
    content = StringField()
    #datetime = DateTimeField()
    author = ReferenceField(Author, required=True)

    def __init__(self, content, author_name, author_email):
        self.content = content
        self.author = Author(name=author_name, email=author_email)

'''
    Question document have embedded: Author and Answer fields.
'''
class Question(Document):
    title = StringField(max_length=120, required=True)
    content = StringField()
    author = ReferenceField(Author, required=True)
    tags = ListField(StringField(max_length=20))
    answers = ListField(EmbeddedDocumentField(Answer))

    def __init__(self, title, content, author_name, author_email, tags):
        self.title = title
        self.content = content
        self.author = Author(name=author_name, email=author_email)
        self.tags = tags
