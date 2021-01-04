from PIL import Image

class image_model():

    def __init__(self, image_file):
        self.load_raw(image_file)

    def load_raw(self, image_file):
        self.image = Image.open(image_file)

