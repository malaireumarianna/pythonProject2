import matplotlib.pyplot as plt
import deeplake

# Load the dataset
ds = deeplake.load("hub://activeloop/places205")

# Select the first 20 classes
classes_to_select = list(range(1, 11))  # Assuming classes are indexed from 1 to 205

# Filter dataset to include only data for the first 20 classes
filtered_ds = ds.filter(lambda x: x.labels.numpy() in classes_to_select, save_result = True, result_path = .../"filtered_places205.npz")

# Save the filtered dataset
'''filtered_ds.save("filtered_places205")


# Load the saved dataset
filtered_ds = deeplake.load("filtered_places205")

'''
# Get one image from each class
# Get one image from each class
images = []
for sample in filtered_ds:
    label = sample.labels.numpy()
    image = sample.images.numpy()
    images.append((label, image))

    # Check if enough images have been gathered
    if len(images) == len(classes_to_select):
        break


print(len(images))

# Visualize one image from each class
'''fig, axs = plt.subplots(4, 5, figsize=(12, 10))  # 4 rows, 5 columns for 20 classes
for i, (label, image) in enumerate(images):
    row = i // 5
    col = i % 5
    axs[row, col].imshow(image)
    axs[row, col].set_title(f"Class {label}")
    axs[row, col].axis('off')

plt.tight_layout()
plt.show()'''
