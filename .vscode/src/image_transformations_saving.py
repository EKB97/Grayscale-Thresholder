import grayscale_thresholder
import copy

def main():
    print('testing image transformations and saving...')
    
    
    sample_image = grayscale_thresholder.ImageModel('Test Input Images/sample.jpeg')
    sample_image.save('Test Output Images/sample.jpeg')
    
    sample_image_norm1 = copy.copy(sample_image)
    sample_image_norm1.adjust_brigtness(1, 255)
    sample_image_norm1.save('Test Output Images/sample_norm1.jpeg')

    sample_image_thresh1 = copy.copy(sample_image)
    sample_image_thresh1.threshold(100)
    sample_image_thresh1.save('Test Output Images/sample_threshold1.jpeg')

if __name__ == '__main__':  
    main()
