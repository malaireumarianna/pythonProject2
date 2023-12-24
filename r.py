labels_list = ['0', '8']  # Desired labels for filtering


@deeplake.compute
def filter_labels(sample_in, labels_list):
    return sample_in.labels.data()['text'][0] in labels_list


ds_view = ds.filter(filter_labels(labels_list), scheduler = 'threaded', num_workers = 0)

print(len(ds_view))



