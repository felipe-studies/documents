from mongoengine import connect
connect(db="accounts", host="localhost", port=27017, username='felipe', password='123')

from mongoengine import Document, ListField, StringField, URLField

class Tutorial(Document):
    title = StringField(required=True, max_length=70)
    author = StringField(required=True, max_length=20)
    contributors = ListField(StringField(max_length=20))
    url = URLField(required=True)