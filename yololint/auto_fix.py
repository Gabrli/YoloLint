import os
import yaml
from yololint.utils.open_yaml_file import open_yaml_file
class AutoFix:
    def __init__(self, dataset_path):
        self.dataset_path = dataset_path

   
    def write_in_yaml(self, data):
       
        with open (os.path.join(self.dataset_path, 'data.yaml'), 'w') as f:
            yaml.dump(data, f, default_flow_style=False)
   
    def create_folder(self, new_element):
        is_list = type(new_element) is list
        if is_list:
            for element in new_element:
                folder_path = os.path.join(self.dataset_path, element)
                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)
        else: os.makedirs(new_element)
        return f"{"Folders" if is_list else "Folder"} created successfully. 📂"


    def create_yaml(self):
        self.write_in_yaml({"names":[],"nc":0})


    def update_yaml(self, element_to_update):
        data_yaml = open_yaml_file(self.dataset_path)

        if element_to_update == "nc_maching":
            self.write_in_yaml({"names": [data_yaml.get('names')], "nc": len(data_yaml.get('names'))})
            print("nc matching fix")
        if element_to_update == "names":
            print("names dosen't exist")
        if element_to_update == "nc":
            print("nc dosen't exist")

       
        # if new_element not in data_yaml['names']:
        #     data_yaml['names'].append(new_element)
        #     data_yaml['nc'] += 1
        #     with open(os.path.join(self.dataset_path, 'data.yaml'), 'w') as f:
        #         yaml.dump(data_yaml, f, default_flow_style=False)
        #     return f"Element '{new_element}' added to data.yaml successfully. 📄"
        # else:
        #     return f"Element '{new_element}' already exists in data.yaml. No changes made. ❌"
    #TODO: finish auto fixing the data.yaml file

