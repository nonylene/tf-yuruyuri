import sys

import tensorflow as tf

import cifar10
from PIL import Image

FLAGS = tf.app.flags.FLAGS
FLAGS.batch_size = 1

filename = tf.placeholder(tf.string)

value = tf.read_file(filename)

images = tf.image.decode_png(value, channels = 3)

resized_images = tf.image.resize_images(images, 96, 96)
img = tf.image.per_image_whitening(resized_images)

logits = cifar10.inference(tf.expand_dims(img, 0))

outputs = tf.nn.softmax(logits)
k_pl = tf.placeholder(tf.int32)
top_k_op = tf.nn.top_k(outputs, k = k_pl)

def classify(session, file_name, k = 1):
    values, indices = session.run(top_k_op, feed_dict = {
        filename: file_name,
        k_pl: k
        })
    return zip(indices.flatten().tolist(), values.flatten().tolist())

def session_with_checkpoint(checkpoint_dir = "./train_old", gpu_enabled = True):
    # disable gpu
    config = tf.ConfigProto(
        device_count = {'GPU': 1 if gpu_enabled else 0}
    )
    session = tf.Session(config = config)

    # Restore the moving average version of the learned variables for eval.
    saver = tf.train.Saver(tf.all_variables())

    ckpt = tf.train.get_checkpoint_state(checkpoint_dir)
    if ckpt and ckpt.model_checkpoint_path:
        # Restores from checkpoint
        saver.restore(session, ckpt.model_checkpoint_path)
    else:
        print('No checkpoint file found')
        finish()
    return session

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.stderr.write("usage: classifier.py <filename>\n")
        sys.exit(-1)
    with session_with_checkpoint() as session:
        result = classify(session, sys.argv[1], 5)

    print(dict(result))

