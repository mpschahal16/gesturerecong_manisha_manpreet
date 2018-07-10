import numpy as np
gestures = np.load('gestures/composite_list.npy')
labels = np.load('gestures/composite_list_labels.npy')


print(gestures.shape)
print(labels)