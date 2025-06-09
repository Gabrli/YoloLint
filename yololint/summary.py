import os
import glob
from yololint.utils.open_yaml_file import open_yaml_file
class Summary:
    def __init__(self, dataset_path):
        self.dataset_path = dataset_path
        self.labels_path = os.path.join(self.dataset_path, 'labels')

    def summary(self):
        len_train_images = len(os.listdir(os.path.join(self.dataset_path, 'images/train')))
        len_test_images = len(os.listdir(os.path.join(self.dataset_path, 'images/val')))
        nc = 0
        classes = []
        classes_id = []
        
        if "data.yaml" in os.listdir(self.dataset_path):
            data = open_yaml_file(self.dataset_path)
            nc = data.get("nc")
            classes = data.get("names")

        for txt_file in glob.glob(os.path.join(self.labels_path, '**', '*.txt'), recursive=True):
            with open(txt_file, 'r') as f:
                lines = f.readlines()
                if not lines:
                    print(f"⚠️ Empty .txt file: {txt_file}")
                else:
                    for line in lines:
                        parts = line.strip().split()
                        class_id = int(parts[0].replace(',', '').strip())
                        classes_id.append(class_id)

        print("----General Summary----")
        used_classes = []
        for class_id in classes_id:
            if class_id not in used_classes:
                used_classes.append(class_id)
                print(f"Number of used: {classes_id.count(class_id)} - {classes[class_id] if class_id < len(classes) else 'Unknown'}")
        print("-----------------------")
        print(f"Number of classes (nc): {nc}")
        print(f"Training images: {len_train_images}")
        print(f"Validation images: {len_test_images}")