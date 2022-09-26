import os
import json
from xml.dom import ValidationErr
from xml.etree import ElementTree

import requests
from requests import Response

from tqdm.auto import tqdm
from os import devnull
from docopt import docopt

from jsonschema import validate, ValidationError

from datetime import datetime


class parsed_anime_database:
    """ Doc:
    Index:
        json = manami project's anime-offline-database
        
    """
    def __init__(self) -> None:
        self.existence_json:bool = False
        self.pathway_json:str = None
        self.latest_json:bool = False
        self.correct_repo:bool = False

        self.current_local_database:str = None
        self.current_online_database:str = None

    
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
                        self.current_local_database = file_name
                        self.pathway_json =  os.path.join(root, file_name)

                        message_existence = f"{file_name} was found. This will be used :3"
                        return message_existence

        # If json was not found in the directories.
        self.existence_json = False
        self.pathway_json = None
        return message_existence

    def read_json(self): # This might not be needed
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
        

    def verify_correct_repo_of_json(self, json_file:json= None) -> str:
        """
        Things to verify:
            - licence/
                - name
                - url
            - repository

        """

        if json_file == None:
            self.verify_existence_local_json()
            with open(self.pathway_json) as file:
                json_file = json.load(file)
                file.close()

        license_name:str = "GNU Affero General Public License v3.0"
        license_url:str = "https://github.com/manami-project/anime-offline-database/blob/master/LICENSE"
        repository_url:str = "https://github.com/manami-project/anime-offline-database"
        # repository_url:str = "fail on purpose; keep it up on this difficult self-taught coding journey! you got this :3" # DEBUG - dummy to fail on purpose :3 

        schema_anime_offline_database = {
            "type": "object",
            "properties": {
                "license": {
                    "name": { "type": "string",
                        "enum": [license_name],
                    },
                    "url": {
                        "type": "string",
                        "enum": [license_url],
                    }
                },
                "repository": {
                    "type": "string",
                    "enum": [repository_url],
                },
            },
        }

        output_message:str = None
        try:
            validate(instance=json_file, schema=schema_anime_offline_database)
            self.correct_repo =  True
            output_message = "Sucess! Correct repo :3"
        except ValidationError as e:
            self.correct_repo = False
            output_message = f"Incorrect repo :'(. \n\nError message: {e}"
        
        return output_message


        # If json's repo doesn't match, set the global variable "correct_repo" to False; if correct, set it to True. Display message to user about file being incorrect.
        

    def move_old_json_to_backup_folder(self):
        """
        
        Idea: Before the new json is saved, move the old json into a separate folder as backup incase the download of the new json fails.

        """
        
        pass

    def compare_last_update(self, online_json_date:str=None, local_json_date:str=None) -> str: # RFER 10
        """
        Check date of repo and determine whether to download newest json from repo

        entry in json: "lastUpdate"
        """

        with open(self.pathway_json) as file:
            local_json_file:dict = json.load(file)
            local_json_date:str = local_json_file['lastUpdate']
            file.close()
        date_parameters:str = '%Y-%m-%d'
        date_local_json:datetime = datetime.strptime(local_json_date, date_parameters)
        date_online_repo:datetime = datetime.strptime(online_json_date, date_parameters)

        if date_local_json >= date_online_repo:
            self.latest_json = True
            return "The local json is up-to-date :3"
        else:
            self.latest_json = False
            return "There's a newer json online :O"



        

    def download_json(self, debug_force_fail_connection:bool = False) -> json:
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
        url = url_json['minified']
        response_json:Response = requests.get(url, stream=True)
        anime_db_json_name:str = 'anime-offline-database-minified.json'

        if response_json.status_code != 200 or self.correct_repo == False:
            # TODO - If failed to download minified json, download regular json
            print("Error #1: Failed to download minified ")
            url = url_json["regular"]
            response_json = requests.get(url,stream=True)
            anime_db_json_name:str = 'anime-offline-database.json'

            if response_json.status_code != 200 or self.correct_repo == False:
                anime_db_json_name = None
                response_json = None

                print("ERROR #2: Failed to download REGULAR anime offline database as well :[")
        self.current_online_database = anime_db_json_name
        return response_json.json()

    def save_json(self, response_json:json): # TODO - Discard download bar for now. potentially, move the the download bar back to "download_json" function if I want to maintain progress bar. Biggest hurdle: separating saving the file from the progress bar.
        new_directory = r'./database_project_manami'
        if not os.path.exists(new_directory): # RFER 04
            os.makedirs(new_directory)

        # This saves the newly downloaded json to local storage.
        new_relative_path:str = f'database_project_manami/{self.current_online_database}'
        with open(new_relative_path, mode= 'w+') as file, tqdm(
            desc=self.current_online_database,
            total= int(response_json.headers['content-length']),
            unit='iB',
            unit_scale=True,
            unit_divisor=1000,
        ) as p_bar: # RFER 07
            
            size = file.write(json.dumps(response_json.json(), indent=1))
            p_bar.update(size)

        file_size:int = ((os.stat(new_relative_path).st_size) / (10**6)) # RFER 05 && RFER 06

        message_download = f'Sucessfully downloaded one of the databases! "{self.current_online_database}" was downloaded and saved locally with the size of ({file_size} mb) :D'
        
        self.current_online_database = None # Reset to None

        print(message_download)


        


        


class parsed_user_list:
    pass
    
if __name__ == '__main__':
    padb = parsed_anime_database()
    padb.download_json()
    padb.verify_existence_local_json()
    output:bool = padb.verify_correct_repo_of_json()

    print(output)
    print()
    print(padb.correct_repo)


    # Testing to see how response.headers works... This isn't useful.
    response:Response = requests.get('https://github.com/manami-project/anime-offline-database/blob/master/anime-offline-database-minified.json?raw=true')

    loaded_str = json.loads(response.text)

    print(loaded_str['lastUpdate'])

    loaded_json = response.json()
    print(loaded_json['lastUpdate'])

    # bar = json.load(response.json())
    # print(bar['lastUpdate'])