import os
from yololint.utils.compare_validate import compare_validate
from yololint.utils.add_file_to_list import add_file_to_list
from yololint.constants.folders import BASIC_FOLDERS, CHILD_FOLDERS

class StructureValidator:
    def __init__(self, dataset_path):
        self.dataset_path = dataset_path

    def dataset_validation(self):
        full_dataset_path = os.path.join(os.path.dirname(__file__), self.dataset_path)
        if not os.path.exists(full_dataset_path):
            return "dataset path dosen't exists or is not correct !"
        basic_subfolders = []
        is_data_yaml = False
        for basic_subfolder in os.listdir(full_dataset_path):
            is_data_yaml = basic_subfolder == "data.yaml"
            basic_subfolders.append(basic_subfolder) if not is_data_yaml else is_data_yaml
         
   
        basic_compare_valid = compare_validate(basic_subfolders, BASIC_FOLDERS)
        if basic_compare_valid:
            return f"You don't have every need basic folders: {basic_compare_valid}"
  
        if not is_data_yaml:
            return f"You don't have data.yaml file !"
        
        child_subfolders = []
 
        for folder in BASIC_FOLDERS:

            child_folder_path = os.path.join(full_dataset_path, folder)
           
            for child_folder in os.listdir(child_folder_path):
                child_subfolders.append(child_folder)

       
            child_compare_valid = compare_validate(child_subfolders, CHILD_FOLDERS)
            if  child_compare_valid:
                return f"you don't every need child folders: {child_compare_valid} in {folder}"
            child_subfolders = []
  
      
        len_train_images = len(add_file_to_list(os.path.join(full_dataset_path, 'images/train')))
        len_test_images = len(add_file_to_list(os.path.join(full_dataset_path, 'images/val')))
        len_train_txt = len(add_file_to_list(os.path.join(full_dataset_path, 'labels/train')))
        len_test_txt = len(add_file_to_list(os.path.join(full_dataset_path, 'labels/val')))


        if (len_train_images != len_train_txt or len_train_images < 0 or len_train_txt < 0) or (len_test_images != len_test_txt or len_test_images < 0 or len_test_txt < 0):
            return (f"You don't have the same number of images and txt files in. "
                    f"Train Images: {len_train_images}, Test images: {len_test_images}, "
                    f"Train Txt: {len_train_txt}, Test Txt: {len_test_txt}")

        return "Structure check complete !"
        

    def has_errors(self):
        pass
    def print_summary(self):pass