# Singular Value Decomposition technique
# 

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

pic = Image.open('Einstein_tongue.jpg')

plt.imshow(pic)
plt.show()

pic = np.array(pic)
plt.imshow(pic, cmap='gray')
plt.show()

# Apply SVD
U,S,V = np.linalg.svd(pic)

# Create spectrum
plt.plot(S, 's-')
plt.xlim([0,100])
plt.xlabel('Component number')
plt.ylabel('Singular value (\sigma)')
plt.show()

# Reconstruct image based on components
comps = np.arange(20,150)

# Reconstruct the low-rank version of the picture
reconPic = U[:,comps]@np.diag(S[comps])@V[comps,:]

# Show original and reconstructed for comparison
plt.figure(figsize=(5,10))
plt.subplot(1,2,1)
plt.imshow(pic,cmap='gray')
plt.title('Original')
plt.axis('off')

plt.subplot(1,2,2)
plt.imshow(reconPic,cmap='gray')
plt.title('Components %s-%s' %(comps[0], comps[1]))
plt.axis('off')
plt.show()