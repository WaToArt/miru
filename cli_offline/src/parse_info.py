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
        self.pathway_json:str = None

        self.correct_repo:bool = False

    
    def check_existence_local_json(self) -> str:
        # Check if json exist locally in directory "database_project_manami", and checks on several levels.
        
        # Consists of two versions for the anime offline database, provided by Manami project.
        file_names: list[str] = [
            'anime-offline-database-minified.json',
            'anime-offline-database.json'
        ]

        directories: set[str] = [
            './database_project_manami',
            '../database_project_manami/'
        ]

        for file_name in file_names: # Look for minified version first.
            for directory in directories:
                for root, dirs, files, in os.walk(directory):
                    if file_name in files:
                        self.existence_json = True
                        self.pathway_json = os.path.join(root, file_name)
                        return

        # If json was not found in the directories.
        self.existence_json = False
        self.pathway_json = None
        return

    def read_json(self):
        if self.pathway_json == None:
            return

        try:
            with open(self.pathway_json, 'r') as anime_offline_database:
                data_offline = json.load(anime_offline_database)
        except FileNotFoundError as e:
            print(f"Error: {e}")
            data_offline = None
        
        if data_offline == None:
            return
        

    def verify_correct_repo_of_json(self) -> None:
        
        # If json's repo doesn't match, set the file's existence and pathway to None. Display message to user about file being incorrect.
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