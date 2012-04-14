# Models for quad application
from mongoengine import *

# Author of question/answer
class Author(EmbeddedDocument):
    email = StringField(required=True)
    name = StringField(max_length=50)

    def show(self):
        return (self.name + " (" + self.email + ")")

class Answer(EmbeddedDocument):
    content = StringField()
    datetime = DateTimeField()
    author = ReferenceField(Author)

class Question(Document):
    title = StringField(max_length=120, required=True)
    author = ReferenceField(Author, required=True)
    tags = ListField(StringField(max_length=20))
    answers = ListField(EmbeddedDocumentField(Anser))

