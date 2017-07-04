# TFRecord

To get the ImageNet dataset into the TFRecord format, we mostly follow the instructions [here](https://github.com/tensorflow/models/tree/master/inception). The instructions are reproduced below, with our additional steps appended.

## Getting started

Before you run the training script for the first time, you will need to download
and convert the ImageNet data to native TFRecord format. The TFRecord format
consists of a set of sharded files where each entry is a serialized `tf.Example`
proto. Each `tf.Example` proto contains the ImageNet image (JPEG encoded) as
well as metadata such as label and bounding box information. See
[`parse_example_proto`](https://github.com/tensorflow/models/tree/master/inception/inception/image_processing.py) for details.

We provide a single [script](https://github.com/tensorflow/models/tree/master/inception/inception/data/download_and_preprocess_imagenet.sh) for
downloading and converting ImageNet data to TFRecord format. Downloading and
preprocessing the data may take several hours (up to half a day) depending on
your network and computer speed. Please be patient.

To begin, you will need to sign up for an account with [ImageNet](http://image-net.org) to gain access to the data. Look for the sign up page,
create an account and request an access key to download the data.

After you have `USERNAME` and `PASSWORD`, you are ready to run our script. Make
sure that your hard disk has at least 500 GB of free space for downloading and
storing the data. Here we select `DATA_DIR=$HOME/imagenet-data` as such a
location but feel free to edit accordingly.

When you run the below script, please enter *USERNAME* and *PASSWORD* when
prompted. This will occur at the very beginning. Once these values are entered,
you will not need to interact with the script again.

```shell
# location of where to place the ImageNet data
DATA_DIR=$HOME/imagenet-data

# build the preprocessing script.
cd tensorflow-models/inception
bazel build //inception:download_and_preprocess_imagenet

# run it
bazel-bin/inception/download_and_preprocess_imagenet "${DATA_DIR}"
```

The final line of the output script should read:

```shell
2016-02-17 14:30:17.287989: Finished writing all 1281167 images in data set.
```

When the script finishes, you will find 1024 training files and 128 validation
files in the `DATA_DIR`. The files will match the patterns
`train-?????-of-01024` and `validation-?????-of-00128`, respectively.

## Additional steps

It seems that recent Bazel distributions work slightly differently from when the original instructions were written, and we got the following error when running the final command:

```
bazel-bin/inception/download_and_preprocess_imagenet.runfiles/inception/inception/data/download_imagenet.sh: line 105: bazel-bin/inception/download_and_preprocess_imagenet.runfiles/inception/inception/data/imagenet_lsvrc_2015_synsets.txt: No such file or directory
```

Following [this discussion](https://github.com/tensorflow/models/issues/682), we run the download script separately:

```shell
bazel-bin/inception/download_and_preprocess_imagenet.runfiles/inception/inception/data/download_imagenet.sh "${DATA_DIR}/raw-data/ /full/path/to/tensorflow/models/inception/inception/data/imagenet_lsvrc_2015_synsets.txt
```

In `download_and_preprocess_imagenet` we then comment out all long-running tasks up to and including the call to `download_imagenet.sh`, and re-run as originally suggested:

```shell
bazel-bin/inception/download_and_preprocess_imagenet "${DATA_DIR}"
```

## Checking the output

TODO
