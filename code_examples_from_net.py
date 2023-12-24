import deeplake

labels_list = ['0', '8']  # Desired labels for filtering


'''@deeplake.compute
def filter_labels(sample_in, labels_list):
    return sample_in.labels.data()['text'][0] in labels_list


ds_view = ds.filter(filter_labels(labels_list), scheduler = 'threaded', num_workers = 0)

print(len(ds_view))


'''
import deeplake
import numpy as np

ds = deeplake.load("hub://activeloop/places205")

# Load the test set
test_ds = ds.test_split()
