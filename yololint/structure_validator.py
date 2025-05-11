import os
from yololint.utils.compare_validate import compare_validate
BASIC_FOLDERS = ['images', 'labels']
CHILD_FOLDERS = ['train', 'val']
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
            if basic_subfolder == "data.yaml":
                is_data_yaml = True
            else: basic_subfolders.append(basic_subfolder)
         
   
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
        
        #TODO: add check matching of image files in test and train in images folder to text files in train and val in labels folder

        return "Structure check complete !"
        

    def has_errors(self):
        pass
    def print_summary(self):pass