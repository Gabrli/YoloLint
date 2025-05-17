import os
from glob import glob
class AnnotationChecker:
    def __init__(self, labels_path, classes_count):
        self.labels_path = labels_path
        self.classes_count = int(classes_count)
        self.__errors = []

    def annotation_checker(self):
        txt_files = glob(os.path.join(self.labels_path, '**', '*.txt'), recursive=True)

        if not txt_files:
            self.__errors.append("⚠️ No .txt annotation files found in the given path! 📂")
            return self.__errors
    
        for txt_file in txt_files:
            with open(txt_file, 'r') as f:
                for i, line in enumerate(f, 1):
                    parts = line.strip().split()
                    if len(parts) != 5:
                        self.__errors.append(
                            f"🚫 [{txt_file}, line {i}] Expected 5 values (class_id, x_center, y_center, width, height), but got {len(parts)}."
                        )
                        return self.__errors
                    try:
                        class_id = int(parts[0].replace(',', '').strip())
                    except ValueError:
                        self.__errors.append(
                            f"❌ [{txt_file}, line {i}] Invalid class ID: '{parts[0]}'. It must be an integer between 0 and {self.classes_count - 1}."
                        )
                        return self.__errors
                    if not (0 <= class_id < self.classes_count):
                        self.__errors.append(
                            f"❌ [{txt_file}, line {i}] Invalid class ID: {parts[0]}. Must be between 0 and {self.classes_count - 1}. 📊"
                        )
                        return self.__errors
            
        return "✅ All annotation files look good! 🎉"
