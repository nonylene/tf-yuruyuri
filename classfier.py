import sys

import tensorflow as tf

import cifar10
from PIL import Image

FLAGS = tf.app.flags.FLAGS

tf.app.flags.DEFINE_string('checkpoint_dir', './train_old',
                           """Directory where to read model checkpoints.""")
FLAGS.batch_size = 1

if len(sys.argv) != 2:
    sys.stderr.write("usage: detect.py <filename>\n")
    sys.exit(-1)

# disable gpu
config = tf.ConfigProto(
        device_count = {'GPU': 0}
)

sess = tf.Session(config = config)

filename = sys.argv[1]

value = tf.read_file(filename)
images = tf.image.decode_png(value, channels = 3)

resized_images = tf.image.resize_images(images, 32, 32)
img = tf.image.per_image_whitening(resized_images)

logits = cifar10.inference(tf.expand_dims(img,0))

outputs = tf.nn.softmax(logits)
# Calculate predictions.
top_k_op = tf.nn.top_k(outputs, k=5)

# Restore the moving average version of the learned variables for eval.
saver = tf.train.Saver(tf.all_variables())

ckpt = tf.train.get_checkpoint_state(FLAGS.checkpoint_dir)
if ckpt and ckpt.model_checkpoint_path:
    # Restores from checkpoint
    saver.restore(sess, ckpt.model_checkpoint_path)
else:
    print('No checkpoint file found')
    finish()

values, indices = sess.run(top_k_op)

print(values.flatten().tolist())
print(indices.flatten().tolist())

sess.close()

