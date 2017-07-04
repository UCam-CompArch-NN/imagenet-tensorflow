import tensorflow as tf
import preprocess_utility as ult
from imagenet_data import ImagenetData

FLAGS = tf.app.flags.FLAGS
tf.app.flags.DEFINE_string('subset', 'train',
"""Either 'train' or 'validation'.""")

# def main():
#     dataset = ImagenetData(subset=FLAGS.subset)
#     data_files = dataset.data_files()
#     images, labels = ult.distorted_inputs(
#         dataset,
#         batch_size=FLAGS.batch_size,
#         num_preprocess_threads=FLAGS.num_preprocess_threads)
#
def traverse_train():
    dataset = ImagenetData(subset=FLAGS.subset)
    data_files = dataset.data_files()

    if data_files is None:
      raise ValueError('No data files found for this dataset')
    else:
      print("there are {} tfRecord files".format(len(data_files)))
    reader = dataset.reader()
    filename_queue = tf.train.string_input_producer(data_files,
                                                    shuffle=True,
                                                    capacity=16)
    key,value = reader.read(filename_queue)
    print(key)
    init = tf.global_variables_initializer()
    sess = tf.Session()
    sess.run(init)

    # Start the queue runners.
    for i in range(1024*10000):
      tf.train.start_queue_runners(sess=sess)
      key_value = sess.run([key])
      print(key_value)


#
#     # Create filename_queue
#     if train:
#         filename_queue = tf.train.string_input_producer(data_files,
#         shuffle=False,
#         capacity=16)
#     else:
#         filename_queue = tf.train.string_input_producer(data_files,
#         shuffle=False,
#         capacity=1)
#
#     if num_preprocess_threads is None:
#         num_preprocess_threads =  4
#         num_readers = 1
#
#     if num_readers > 1:
#         enqueue_ops = []
#         for _ in range(num_readers):
#             reader = dataset.reader()
#             _, value = reader.read(filename_queue)
#             enqueue_ops.append(examples_queue.enqueue([value]))
#
#             tf.train.queue_runner.add_queue_runner(
#             tf.train.queue_runner.QueueRunner(examples_queue, enqueue_ops))
#             example_serialized = examples_queue.dequeue()
#     else:
#         reader = dataset.reader()
#         key, example_serialized = reader.read(filename_queue)
#         print(key)
#
#     images_and_labels = []
#     for thread_id in range(num_preprocess_threads):
#         # Parse a serialized Example proto to extract the image and metadata.
#         image_buffer, label_index, bbox, _ = parse_example_proto(
#         example_serialized)
#         image = image_preprocessing(image_buffer, bbox, train, thread_id)
#         images_and_labels.append([image, label_index])
def main(argv=None):  # pylint: disable=unused-argument
  traverse_train()

if __name__ == '__main__':
  tf.app.run()
