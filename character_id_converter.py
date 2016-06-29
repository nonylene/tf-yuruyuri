import peewee

from os import path

from face import Face


Face.create_table(True)
Face.delete().execute()

import old_face

# 36000
faces = old_face.Face.select()

for face in faces:
    print(face.id)
    if face.character == "akari":
        c_id = 0
    elif face.character == "kyoko":
        c_id = 1
    elif face.character == "tinatsu":
        c_id = 2
    elif face.character == "yui":
        c_id = 2
    elif face.character == "titose":
        c_id = 3
    elif face.character == "ayano":
        c_id = 4
    elif face.character == "sakurako":
        c_id = 5
    elif face.character == "himawari":
        c_id = 6
    elif face.character == "other_yuri":
        c_id = 7
    elif face.character == "other_face":
        c_id = 7
    elif face.character == "other_other":
        c_id = 7


    Face.create(
            story = face.story,
            pic_path = face.pic_path,
            x = face.x,
            y = face.y,
            w = face.w,
            h = face.h,
            face_path = face.face_path,
            original_id = face.id,
            character = face.character,
            character_id = c_id
    )
