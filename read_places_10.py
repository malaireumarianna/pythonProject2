import numpy as np

import deeplake
import numpy as np
from matplotlib import pyplot as plt

'''loaded_arrays = np.load('places_first20_classes.npz', allow_pickle = True)

images = loaded_arrays['images']
labels = loaded_arrays['labels']'''


filtered_ds = deeplake.load(".../filtered_places205.npz")


dataloader = filtered_ds.pytorch(num_workers = 2, shuffle = False, batch_size= 4)




classes_to_select = list(range(1, 11))

print(len(filtered_ds))


images = []

i=1
while i<11:
    for sample in filtered_ds:
        label = sample.labels.numpy()
        # Check if the class has been selected
        if label==i:
            print(label)
            image = sample.images.numpy()
            images.append((label, image))
            i += 1

labels_only = []
for label, _ in images:
    labels_only.append(label)

print(labels_only)


fig, axs = plt.subplots(2, 5, figsize=(12, 10))  # 4 rows, 5 columns for 20 classes
for i, (label, image) in enumerate(images):
    row = i // 5
    col = i % 5
    axs[row, col].imshow(image)
    axs[row, col].set_title(f"Class {label}")
    axs[row, col].axis('off')

plt.tight_layout()
plt.show()