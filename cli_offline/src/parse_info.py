import os
import json
from xml.etree import ElementTree


class parsed_anime_database:
    """ Doc:
    Index:
        json = manami project's anime-offline-database
        
    """
    def __init__(self) -> None:
        self.existence_json:bool = False
        self.correct_repo:bool = False

        self.check_repo_of_json()
    
    def check_existence_local_json(self) -> str:
        # Check if json exist locally in directory "database_project_manami", and checks on several levels.
        
        # Consists of two versions for the anime offline database, provided by Manami project.
        file_names: list[str] = {
            'anime-offline-database-minified.json',
            'anime-offline-database.json'
        }

        directories: set[str] = {
            './database_project_manami',
            '../database_project_manami/'
        }

        pathway_json:str = None
        for file_name in file_names: # Look for minified version first.
            for directory in directories:
                for root, dirs, files, in os.walk(directory):
                    if file_name in files:
                        self.existence_json = True
                        pathway_json = os.path.join(root, file_name)
                        return pathway_json

        # If json was not found in the directories.
        self.existence_json = False
        return pathway_json

    def read_json():
        pass

    def check_repo_of_json(self):
        pass

    def download_json(self):
        # TODO - Download minified json

            # TODO - If failed to download minified json, download regular json
        
        pass


class parsed_user_list:
    pass
    
if __name__ == '__main__':
    padb = parsed_anime_database()
    pathway = padb.check_existence_local_json()
    print(pathway)