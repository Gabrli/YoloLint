import os
import yaml
from yololint.utils.compare_validate import compare_validate
from yololint.utils.add_file_to_list import add_file_to_list
from yololint.constants.folders import BASIC_FOLDERS, CHILD_FOLDERS

class StructureValidator:
    def __init__(self, dataset_path):
        self.dataset_path = dataset_path
        self.__errors = []

    def dataset_validation(self):
        full_dataset_path = os.path.join(os.path.dirname(__file__), self.dataset_path)
        if not os.path.exists(full_dataset_path):
            self.__errors.append("dataset path dosen't exists or is not correct !")
        basic_subfolders = []
        data_yaml = ''
        for basic_subfolder in os.listdir(full_dataset_path):
            if basic_subfolder.endswith('.yaml'):
                data_yaml = basic_subfolder
            else: basic_subfolders.append(basic_subfolder)
         
         
        basic_compare_valid = compare_validate(basic_subfolders, BASIC_FOLDERS)
        if basic_compare_valid:
            self.__errors.append(f"You don't have every need basic folders: {basic_compare_valid}")
  
        if data_yaml == '':
            self.__errors.append(f"You don't have data.yaml file !")
        
        with open(os.path.join(full_dataset_path, data_yaml), 'r') as f:
            data_config = yaml.safe_load(f)

            class_names = data_config.get('names')
            num_classes = data_config.get('nc')
            if not len(class_names) == num_classes:
                self.__errors.append("You don't have the same number of class_names and defined enum classes.")
        
        child_subfolders = []
 
        for folder in BASIC_FOLDERS:

            child_folder_path = os.path.join(full_dataset_path, folder)
           
            for child_folder in os.listdir(child_folder_path):
                child_subfolders.append(child_folder)

       
            child_compare_valid = compare_validate(child_subfolders, CHILD_FOLDERS)
            if  child_compare_valid:
                self.__errors.append(f"you don't every need child folders: {child_compare_valid} in {folder}")
            child_subfolders = []
  
      
        len_train_images = len(add_file_to_list(os.path.join(full_dataset_path, 'images/train')))
        len_test_images = len(add_file_to_list(os.path.join(full_dataset_path, 'images/val')))
        len_train_txt = len(add_file_to_list(os.path.join(full_dataset_path, 'labels/train')))
        len_test_txt = len(add_file_to_list(os.path.join(full_dataset_path, 'labels/val')))


        if (len_train_images != len_train_txt or len_train_images < 0 or len_train_txt < 0) or (len_test_images != len_test_txt or len_test_images < 0 or len_test_txt < 0):
            self.__errors.append(f"You don't have the same number of images and txt files in. "
                    f"Train Images: {len_train_images}, Test images: {len_test_images}, "
                    f"Train Txt: {len_train_txt}, Test Txt: {len_test_txt}")

        return f"Your Errors: {self.__errors}"
        