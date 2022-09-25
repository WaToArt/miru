import os
import json
from xml.etree import ElementTree

import requests
from requests import Response

from tqdm.auto import tqdm
from os import devnull
from docopt import docopt

class parsed_anime_database:
    """ Doc:
    Index:
        json = manami project's anime-offline-database
        
    """
    def __init__(self) -> None:
        self.existence_json:bool = False
        self.current_database:str = None
        self.pathway_json:str = None

        self.correct_repo:bool = False

    
    def verify_existence_local_json(self) -> str:
        """
        Check if json exist locally in directory "database_project_manami", and checks on several levels.
        """
        message_existence:str = "None of the required database were found."
        
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
                        self.current_database = file_name
                        self.pathway_json =  os.path.join(root, file_name)

                        message_existence = f"{file_name} was found. This will be used :3"
                        return message_existence

        # If json was not found in the directories.
        self.existence_json = False
        self.pathway_json = None
        return message_existence

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

    def progress_bar_downloading(self, response_json:Response, anime_db_json_name='test'):
        total_size_bytes = int(response_json.headers.get('content-length',0))
        block_size = 1024
        progress_bar = tqdm(total=total_size_bytes, unit='iB', unit_scale=True)
        with open(f'{anime_db_json_name}.json', 'wb') as file:
            for data in response_json.iter_content(block_size):
                progress_bar.update(len(data))
                file.write(data)
        progress_bar.close()





    def download_json(self, debug_force_fail_connection:bool = False) -> str:
        """ Credits for anime offline database
        Link: https://github.com/manami-project/anime-offline-database

        If the download was sucessful, it should return a message saying the "download was sucessfully". If it failed, it should return 
        
        """

        message_download:str = "Failed to either Json options for anime offline databases :'["

        if debug_force_fail_connection:
            return message_download

        url_json:dict = {
            'minified': 'https://github.com/manami-project/anime-offline-database/blob/master/anime-offline-database-minified.json?raw=true',
            'regular': 'https://github.com/manami-project/anime-offline-database/blob/master/anime-offline-database.json?raw=true',
        }
        #RFER 02 # TODO - Download minified json
        response_json:Response = requests.get(url_json['minified'], stream=True)

        self.progress_bar_downloading(response_json)

        anime_db_json_name:str = 'anime-offline-database-minified.json'

        if response_json.status_code != 200:
            # TODO - If failed to download minified json, download regular json
            print("Error #1: Failed to download minified ")
            response_json = requests.get(url_json['regular'],stream=True)
            anime_db_json_name:str = 'anime-offline-database.json'

            if response_json.status_code != 200:
                anime_db_json_name = None
                print("ERROR #2: Failed to download REGULAR anime offline database as well :[")
                
                # message_download = "Failed to either Json options for anime offline databases :'["

                return message_download
        
        

        # TODO - Implement verify repo before saving locally.
            # Maybe add it to each of the for loops when downloading from link.

        new_directory = r'./database_project_manami'
        if not os.path.exists(new_directory): # RFER 04
            os.makedirs(new_directory)

        new_relative_path:str = f'database_project_manami/{anime_db_json_name}'

        with open(new_relative_path, mode= 'w+') as file: # Unsure if pathway works.
            file.write(json.dumps(response_json.json(), indent=1))
            file.close()
        


        file_size:int = (os.stat(new_relative_path).st_size) / (10**6) # RFER 05 && RFER 06

        message_download = f'Sucessfully downloaded one of the databases! "{anime_db_json_name}" was downloaded ({file_size} mb) :D'
        
        return message_download



        


        


class parsed_user_list:
    pass
    
if __name__ == '__main__':
    padb = parsed_anime_database()
    pathway = padb.download_json()
    print(pathway)