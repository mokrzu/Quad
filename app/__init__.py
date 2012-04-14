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
    author = ReferenceField(Author)

'''
    Question document have embedded: Author and Answer fields.
'''
class Question(Document):
    title = StringField(max_length=120)
    content = StringField()
    author = ReferenceField(Author)
    tags = ListField(StringField(max_length=20))
    answers = ListField(EmbeddedDocumentField(Answer))
