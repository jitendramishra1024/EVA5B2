import math 
import matplotlib.pyplot as plt
import numpy as np

def plot_n_image(number,trainloader,classes,format):
    # get some random training images
    dataiter = iter(trainloader)
    images, labels = dataiter.next()
    nrows = math.floor(math.sqrt(number))
    ncols = math.ceil(math.sqrt(number))

    fig, ax = plt.subplots(nrows, ncols, figsize=(10, 15))

    for i in range(nrows):
        for j in range(ncols):
            index = i * ncols + j
            ax[i, j].axis("off")
            ax[i, j].set_title(classes[labels[index]])
            #FIRST UNNORMALIZE THEN SHOW 
            if format=='raw':
              ax[i, j].imshow(np.transpose(images[index].cpu().numpy()/ 2 + 0.5, (1, 2, 0)), cmap="gray_r")
            elif format=='normalized':
              ax[i, j].imshow(np.transpose(images[index].cpu().numpy(), (1, 2, 0)), cmap="gray_r")
    