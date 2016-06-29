from PIL import Image
import numpy as np

from face import Face

import characters
import os

faces = Face.select()

def export(ran, filename):
    os.remove(filename)
    with open(filename, "a") as f:
        for i in ran:
            print (i)
            face = faces[i]
            im = Image.open(face.face_path).resize((96,96))
            im = (np.array(im))
            r = im[:,:,0].flatten()
            g = im[:,:,1].flatten()
            b = im[:,:,2].flatten()
            character_id = characters.search_id(face.character)
            print(character_id)
            label = [character_id]
            out = list(label) + list(r) + list(g) + list(b)
            np.array(out, np.uint8).tofile(f)


face_count = Face.select().count()
face_count_6 = int(face_count / 6)
BASE_DIR = "data/"

export(range(0, face_count, 6), BASE_DIR + "data_batch_1.bin")
export(range(1, face_count, 6), BASE_DIR + "data_batch_2.bin")
export(range(2, face_count, 6), BASE_DIR + "data_batch_3.bin")
export(range(3, face_count, 6), BASE_DIR + "data_batch_4.bin")
export(range(4, face_count, 6), BASE_DIR + "data_batch_5.bin")
export(range(5, face_count, 6), BASE_DIR + "test_batch.bin")
