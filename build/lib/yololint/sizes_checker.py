import os
import glob
import cv2 as cv

class SizesChecker:
    def __init__(self, sizeX, sizeY):
        self.sizeX = sizeX
        self.sizeY = sizeY

    def check_sizes(self, path_to_dataset):
        """
        Check if all images in the dataset have the specified size.
        """
        img_files = []
        for ext in ('*.jpg', '*.jpeg', '*.png'):
            img_files.extend(glob.glob(os.path.join(path_to_dataset, '**', ext), recursive=True))
        for img_file in img_files:
            img = cv.imread(img_file)
            if img is None:
                print(f"❌ Image '{img_file}' could not be read. Please check the file path. 📂")
                continue
            sizeY, sizeX = img.shape[:2]  
            if sizeX != self.sizeX or sizeY != self.sizeY:
                print(f"❌ Image '{img_file}' has size {sizeX}x{sizeY}, expected {self.sizeX}x{self.sizeY}. 📏")
                user_confirmed = input("Do you want to rescale this Image? (yes/no): ").strip().lower()
                if user_confirmed == 'yes':
                    print(self.rescale_image(img_file))
                continue
            else:
                return f"✅ All images are of size {self.sizeX}x{self.sizeY}. 🎉"
        
    def rescale_image(self, image_path):
        """
        Rescale the image to the specified size.
        """
        img = cv.imread(image_path)
        if img is None:
            return f"❌ Image '{image_path}' could not be read. Please check the file path. 📂"
        resized_img = cv.resize(img, (self.sizeX, self.sizeY))  
        cv.imwrite(image_path, resized_img)
        return f"✅ Image '{image_path}' has been resized to {self.sizeX}x{self.sizeY}. 📏"

