import os
from glob import glob
class YoloAnnotationChecker:
    def __init__(self, labels_path, classes_count):
        self.labels_path = labels_path
        self.classes_count = classes_count
        self.___errors = []

    def annotation_checker(self):
        txt_files = glob(os.path.join(self.labels_path, '**', '*.txt'), recursive=True)
    
        for txt_file in txt_files:
            with open(txt_file, 'r') as f:
                for line in f :
                    parts = line.strip().split()
                    print(int(parts[0]))
                    if len(parts) != 5:
                        self.___errors.append(f"{txt_file} || You don't have all expected values")
                  
                    if not  (0 <= int(parts[0]) < self.classes_count):
                        self.___errors.append(f"{txt_file} || You don't have correct class id. Your class id: {parts[0]}")
            
        return f"Your Errors: {self.___errors}"

