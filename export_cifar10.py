from PIL import Image
import numpy as np

from face import Face

faces = Face.select()

def export(ran, filename):
    out = []
    for i in ran:
        print (i)
        face = faces[i]
        im = Image.open(face.face_path).resize((32,32))
        im = (np.array(im))
        r = im[:,:,0].flatten()
        g = im[:,:,1].flatten()
        b = im[:,:,2].flatten()
        label = [face.character_id]
        out = out + list(label) + list(r) + list(g) + list(b)
    np.array(out, np.uint8).tofile(filename)


face_count = Face.select().count()
face_count_6 = int(face_count / 6)
BASE_DIR = "data/"

export(range(0, face_count_6), BASE_DIR + "data_batch_1.bin")
export(range(face_count_6, face_count_6 * 2), BASE_DIR + "data_batch_2.bin")
export(range(face_count_6 * 2, face_count_6 * 3), BASE_DIR + "data_batch_3.bin")
export(range(face_count_6 * 3, face_count_6 * 4), BASE_DIR + "data_batch_4.bin")
export(range(face_count_6 * 4, face_count_6 * 5), BASE_DIR + "data_batch_5.bin")
export(range(face_count_6 * 5, face_count), BASE_DIR + "test_batch.bin")
