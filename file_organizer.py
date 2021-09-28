import os
import pathlib
import yaml

class OrganizeFolderFiles:

    def __init__(self, yaml_origin):
        self.configs = self._load_configs()
        self.root_path = self.configs.get("path")
        self.default_folders = self.configs.get("default_folders")
        self.destiny_root = self.configs.get("destiny_root")
        self.yaml_origin = yaml_origin

    def _load_configs(self):
        with open('configs.yml') as conf_file:
            configs = yaml.safe_load(conf_file)
        return  configs

    def execute(self):
        file_dict_list, file_types = self._get_files(os.listdir(path=self.root_path))
        self._to_correct_folder(file_dict_list, file_types)

    def _get_files(self, files):
        files = self._remove_folders(files)
        file_types = [file.split(".")[-1] if len(file.split(".")) > 1 else "script" for file in files]
        unique_types = self._get_single_file_types(file_types)

        return self._build_files_dict(files, file_types),  unique_types

    def _remove_folders(self, files):
        return [file for file in files if self._not_folder(file)]

    def _not_folder(self, file):
        return not os.path.isdir(os.path.join(self.root_path, file))

    def _build_files_dict(self, files, file_types):
        return [{file_type:file} for (file_type,file) in zip(file_types, files)]

    @staticmethod
    def _get_single_file_types(file_types):
        return list(set(file_types))

    def _to_correct_folder(self, file_dict_list, file_types):
        for file_type in file_types:
            self._move_file(file_type, file_dict_list)

    def _move_file(self, file_type, file_dict_list):
        for file_dict in file_dict_list:
            if file_dict.get(file_type):

                self._change_folder(file_type, file_dict[file_type])
                continue

    def _change_folder(self, folder_name, item_name):
        folder_name = self._define_right_path(folder_name)
        if not os.path.isdir(folder_name):
            os.mkdir(folder_name)

        current = os.path.join(self.root_path, item_name)
        destination = "/".join([folder_name, item_name])

        os.replace(current, destination)

    def _define_right_path(self, folder_name):
        for key in self.default_folders:

            if not self.default_folders[key]:
                continue

            path_name = self.default_folders[key].replace(" ","").split(",")
            
            if folder_name in path_name:
                return os.path.join(self.destiny_root, key, folder_name.capitalize())

        return os.path.join(self.root_path, folder_name.capitalize())

# yaml_origin = "/home/joaoh/repos_to_conribute/joaoh/FileOrganizer/configs.yml"

print(pathlib.Path(__file__).parent.resolve())

# OrganizeFolderFiles(yaml_origin).execute()