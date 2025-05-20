import os
from glob import glob
class AnnotationChecker:
    def __init__(self, labels_path, classes_count):
        self.labels_path = labels_path
        self.classes_count = int(classes_count)

    def annotation_checker(self):
        txt_files = glob(os.path.join(self.labels_path, '**', '*.txt'), recursive=True)

        if not txt_files:
            return "⚠️ No .txt annotation files found in the given path! 📂"
    
        for txt_file in txt_files:
            with open(txt_file, 'r') as f:
                if not f == None:
                    for i, line in enumerate(f, 1):
                        parts = line.strip().split()
                        if len(parts) != 5:
                            return f"🚫 [{txt_file}, line {i}] Expected 5 values (class_id, x_center, y_center, width, height), but got {len(parts)}."
                        try:
                            class_id = int(parts[0].replace(',', '').strip())
                        except ValueError:
                            return f"❌ [{txt_file}, line {i}] Invalid class ID: '{parts[0]}'. It must be an integer between 0 and {self.classes_count - 1}."
                        if not (0 <= class_id < self.classes_count):
                         return f"❌ [{txt_file}, line {i}] Invalid class ID: {parts[0]}. Must be between 0 and {self.classes_count - 1}. 📊"
                return f"⚠️ Empty .txt file!"
        return "✅ All annotation files look good! 🎉"
