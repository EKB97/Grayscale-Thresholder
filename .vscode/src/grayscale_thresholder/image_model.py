from PIL import Image, ImageEnhance
import numpy as np

class ImageModel:

    def __init__(self, image_file):
        self.load(image_file)

    def load(self, image_file):
        self.image = Image.open(image_file)
        self.pixel_data = np.array(self.image)
        self.height = self.pixel_data.shape[0]
        self.width = self.pixel_data.shape[1]
        self.shape = (self.height, self.width)

    def save(self, file_location):
        self.image.save(file_location)
    
    def adjust_brigtness(self, current, target):
        factor = current / target
        enhancer = ImageEnhance.Brightness(self.image)
        self.image = enhancer.enhance(factor)
        
    def threshold(self, threshold):
        self.image = self.image.point(lambda p: p > threshold and 255)
        