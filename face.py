import peewee

from os import path

db = peewee.SqliteDatabase(path.join(path.abspath(path.dirname(__file__)), 'main.db'))

class Face(peewee.Model):
    story = peewee.IntegerField(null = False)
    pic_path = peewee.TextField(null = False)
    x = peewee.IntegerField(null = False)
    y = peewee.IntegerField(null = False)
    w = peewee.IntegerField(null = False)
    h = peewee.IntegerField(null = False)
    character = peewee.TextField(null = True)
    face_path = peewee.TextField(null = False)
    original_id = peewee.IntegerField(null = False)
    thumb_path = peewee.TextField(null = True)

    class Meta:
        database = db
