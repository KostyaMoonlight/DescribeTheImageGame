import cv2


class ImageProcessor:

    def __init__(self, path2image, proportions, size=None):
        self.image = cv2.imread(path2image)
        if size:
            self.image = cv2.resize(self.image, tuple(size))
        self.proportions = proportions
        self.size = self.image.shape[0], self.image.shape[1]

    def get_image_matrix(self):
        self.cut_image = []
        w, h = self.proportions
        self.w_size = self.size[0] // w
        self.h_size = self.size[1] // h

        for i in range(w):
            h_cut = []
            for j in range(h):
                h_cut.append(self.image[i*self.w_size: (i+1)*self.w_size,j*self.h_size: (j+1)*self.h_size,:])
            self.cut_image.append(h_cut)
        return self.cut_image
    