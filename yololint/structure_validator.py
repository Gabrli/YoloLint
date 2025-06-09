import os
from yololint.utils.compare_validate import compare_validate
from yololint.utils.add_file_to_list import add_file_to_list
from yololint.utils.open_yaml_file import open_yaml_file
from yololint.constants.folders import BASIC_FOLDERS, CHILD_FOLDERS
from yololint.auto_fix import AutoFix
from yololint.constants.commands import COMMANDS
from yololint.constants.errors import ERRORS

class StructureValidator:
    def __init__(self, dataset_path):
        self.dataset_path = dataset_path
        self.auto_fix = AutoFix(dataset_path)

    @classmethod
    def is_valid_number_of_data(len_train_images, len_train_txt, len_test_images, len_test_txt):
        return (len_train_images != len_train_txt or len_train_images < 0 or len_train_txt < 0) or (len_test_images != len_test_txt or len_test_images < 0 or len_test_txt < 0)

    @classmethod
    def auto_fix_handler(self, idx_of_error, idx_of_command, fun, new_element="", ):
         print(f"{ERRORS[idx_of_error] + ", ".join(new_element) if idx_of_error == 1 else ERRORS[idx_of_error]}")
         is_want_to_fix = input(f"Do you want to automatically {COMMANDS[idx_of_command]}").strip().lower()
         return fun(new_element) if is_want_to_fix == "yes" else ""

    def dataset_validation(self):

        if not os.path.exists(self.dataset_path):
            self.auto_fix_handler(0, 0, self.auto_fix.create_folder, "dataset",)
      
        basic_subfolders = []
        data_yaml = ''
        for basic_subfolder in os.listdir(self.dataset_path):
            if basic_subfolder.endswith('.yaml'):
                data_yaml = basic_subfolder
            else: basic_subfolders.append(basic_subfolder)
         
         
        basic_compare_valid = compare_validate(basic_subfolders, BASIC_FOLDERS)
        if basic_compare_valid:
            self.auto_fix_handler(1, 1, self.auto_fix.create_folder, basic_compare_valid)
  
        if data_yaml == '':
            self.auto_fix_handler(2, 2, self.auto_fix.create_yaml)
        
        data = open_yaml_file(self.dataset_path)    
        if not data:
            self.auto_fix_handler(3, 3, self.auto_fix.update_yaml, "all")
        if not data.get('names'):
            self.auto_fix_handler(4, 4, self.auto_fix.update_yaml,"names")
             
        class_names = data.get('names')
        if not data.get('nc'):
                self.auto_fix_handler(5,5, self.auto_fix.update_yaml, "nc")
        num_classes = data.get('nc')
        if not len(class_names) == num_classes:
            self.auto_fix_handler(6,6, self.auto_fix.update_yaml, "nc_maching")
        
        
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

        if self.is_valid_number_of_data(len_train_images, len_train_txt, len_test_images, len_test_txt):
         return f"🖼️ Number of images and annotation files (.txt) doesn't match!\n Train Images: {len_train_images}, Train Labels: {len_train_txt}\n Val Images: {len_test_images}, Val Labels: {len_test_txt} ⚠️"

        return f"🧪 Validation complete.\n ✅ All checks passed. Dataset structure looks good! 🧼"
        