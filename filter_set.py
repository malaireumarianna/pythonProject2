import deeplake
import numpy as np

ds = deeplake.load("hub://activeloop/places205-train")


# Select the first 20 classes
classes_to_select = list(range(1, 11))  # Assuming classes are indexed from 1 to 205

# Filter dataset to include only data for the first 20 classes
filtered_ds = ds.filter(lambda x: x.labels.numpy() in classes_to_select, save_result = True, result_path = ".../filtered_places205.npz")





'''ds.labels.shape()

# Select the first 20 classes
classes_to_select = list(range(1, 21))  # Assuming classes are indexed from 1 to 205

# Filter dataset to include only data for the first 20 classes
filtered_ds = ds.filter(lambda x: x.labels.numpy() in classes_to_select)

images = []
labels = []
for sample in filtered_ds:
    images.append(sample["images"].numpy())
    labels.append(sample["labels"].numpy())

# Save the images and labels to a NumPy archive
np.savez("places_first20_classes.npz", images=images, labels=labels)
'''


# Filter dataset to include only data for the first 20 classes
'''filtered_samples = [sample for sample in ds if sample.labels.numpy() in classes_to_select]

# Extract images and labels from filtered dataset
images = np.array([sample.images.numpy() for sample in filtered_samples])
labels = np.array([sample.labels.numpy() for sample in filtered_samples])



np.savez('places_first20_classes.npz', images, labels)
'''

'''loaded_arrays = np.load('places_first20_classes.npz', allow_pickle = True)
loaded_arrays['images']
loaded_arrays['labels']'''