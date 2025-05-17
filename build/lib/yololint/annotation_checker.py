import os
from glob import glob
class AnnotationChecker:
    def __init__(self, labels_path, classes_count):
        self.labels_path = labels_path
        self.classes_count = classes_count
        self.___errors = []

    def annotation_checker(self):
        txt_files = glob(os.path.join(self.labels_path, '**', '*.txt'), recursive=True)

        if not txt_files:
            self.__errors.append("⚠️ No .txt annotation files found in the given path! 📂")
            return self.___errors
    
        for txt_file in txt_files:
            with open(txt_file, 'r') as f:
                for i, line in f :
                    parts = line.strip().split()
                    if len(parts) != 5:
                        self.___errors.append(f"🚫 [{txt_file}, line {i}] Expected 5 values (class_id, x_center, y_center, width, height), but got {len(parts)}.")
                        return self.___errors
                  
                    if not  (0 <= int(parts[0]) < self.classes_count):
                        self.___errors.append(f"   ❌ [{txt_file}, line {i}] Invalid class ID: {parts[0]}. "
                                f"Must be between 0 and {self.classes_count - 1}. 📊")
                        return self.___errors
            
        return   "✅ All annotation files look good! 🎉"
