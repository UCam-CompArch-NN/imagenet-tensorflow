# TFRecord Checking

TFRecord checking script performs a simple traverse of all the data downloaded.

## Getting started

```shell
# location of ImageNet data in TFRecord format
DATA_DIR=$HOME/where-the-tfrecord-data-is

# run it with your tensorflow activated/stored
# by default, I assumed you have gpu support
python test_dataset.py --train_dir=$(DATA_DIR)
```
## Results

The script should run without raising any errors.
If errors such as "broken TFRecord" or "truncated TFRecord" is reported, this
means the downloaded files are corrupted.
