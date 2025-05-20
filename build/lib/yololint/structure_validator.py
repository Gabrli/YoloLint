import os
import yaml
from yololint.utils.compare_validate import compare_validate
from yololint.utils.add_file_to_list import add_file_to_list
from yololint.constants.folders import BASIC_FOLDERS, CHILD_FOLDERS

class StructureValidator:
    def __init__(self, dataset_path):
        self.dataset_path = dataset_path

    def dataset_validation(self):

        if not os.path.exists(self.dataset_path):
            return "🚫 Dataset path doesn't exist or is incorrect! 📁"
        basic_subfolders = []
        data_yaml = ''
        for basic_subfolder in os.listdir(self.dataset_path):
            if basic_subfolder.endswith('.yaml'):
                data_yaml = basic_subfolder
            else: basic_subfolders.append(basic_subfolder)
         
         
        basic_compare_valid = compare_validate(basic_subfolders, BASIC_FOLDERS)
        if basic_compare_valid:
            return "📂 Missing required base folders! Expected but not found: " + ", ".join(basic_compare_valid)
  
        if data_yaml == '':
            return f"❌ Missing required file: `data.yaml` 🧾"
        
        with open(os.path.join(self.dataset_path, data_yaml), 'r') as f:
            data_config = yaml.safe_load(f)
            if not data_config:
                return "⚠️ Your `data.yaml` file is empty or invalid! ❗"
            if not data_config.get('names'):
                return "🔍 Missing `names` field in your `data.yaml` file. Please define class names. 🧠"
            class_names = data_config.get('names')
            if not data_config.get('nc'):
                return "🔍 Missing `nc` field (number of classes) in your `data.yaml` file. 🧮"
            num_classes = data_config.get('nc')
            if not len(class_names) == num_classes:
                return "❌ The number of class names does not match `nc`. Check your `data.yaml`! 🔢"
        
        child_subfolders = []
 
        for folder in BASIC_FOLDERS:

            child_folder_path = os.path.join(self.dataset_path, folder)
           
            for child_folder in os.listdir(child_folder_path):
                child_subfolders.append(child_folder)

       
            child_compare_valid = compare_validate(child_subfolders, CHILD_FOLDERS)
            if  child_compare_valid:
                return f"📁 Missing child folders in `{folder}`. Expected: {', '.join(child_compare_valid)} 📂"
            child_subfolders = []
  
      
        len_train_images = len(add_file_to_list(os.path.join(self.dataset_path, 'images/train')))
        len_test_images = len(add_file_to_list(os.path.join(self.dataset_path, 'images/val')))
        len_train_txt = len(add_file_to_list(os.path.join(self.dataset_path, 'labels/train')))
        len_test_txt = len(add_file_to_list(os.path.join(self.dataset_path, 'labels/val')))


        if (len_train_images != len_train_txt or len_train_images < 0 or len_train_txt < 0) or (len_test_images != len_test_txt or len_test_images < 0 or len_test_txt < 0):
      
            return f"🖼️ Number of images and annotation files (.txt) doesn't match!\n Train Images: {len_train_images}, Train Labels: {len_train_txt}\n Val Images: {len_test_images}, Val Labels: {len_test_txt} ⚠️"

        return f"🧪 Validation complete.\n❗ Errors found:\n" + "\n".join(self.__errors) if self.__errors else "✅ All checks passed. Dataset structure looks good! 🧼"
        