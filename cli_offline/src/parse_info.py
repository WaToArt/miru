import os
import json
from pickletools import int4
from xml.dom import ValidationErr
from xml.etree import ElementTree

import requests
from requests import Response
from requests import models

from tqdm.auto import tqdm
from os import devnull
from docopt import docopt

from jsonschema import validate, ValidationError

from datetime import datetime


class download_anime_database_json:
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

    def debug_only___psuedocode_for_ui_execute_downloading_json(self) -> None:
        """
        Psuedocode:
            - verify_existence_local_json
            - download_json
            - verify_correct_repo_of_json
            - compare_last_update
                - Ask user if they still want to download the new Json
                    - Default after timeout: Download
            - move old json (if it exists) into a separate folder that's old. # TODO - Need to create function
            - save_json
        """

        print(self.verify_existence_local_json())
        
        response_json:dict = self.download_json()
        
        print(self.verify_correct_repo_of_json(response_json))
        
        print(self.compare_last_update(online_json_date=response_json['lastUpdate']))

        self.move_old_json_to_backup_folder()

        self.save_json(response_json)


        
        pass
    
    def verify_existence_local_json(self) -> None:
        """
        Check if json exist locally in directory "database_project_manami/", and checks on several levels.
        """
        message_existence:str = "None of the required database were found."
        
        # Consists of two versions for the anime offline database, provided by Manami project.
        file_names: list[str] = [
            'anime-offline-database-minified.json',
            'anime-offline-database.json'
        ]

        # Look at two directories 
        directories: set[str] = [
            './database_project_manami',
            '../database_project_manami/'
        ]

        # Search for json in various directories
        for file_name in file_names: # Look for minified version first.
            for directory in directories:
                for root, dirs, files, in os.walk(directory):
                    if file_name in files:
                        self.existence_json = True
                        self.current_local_database = file_name
                        self.pathway_json =  os.path.join(root, file_name)

                        # Exit function if one of the versions are found
                        message_existence = f"{file_name} was found. This will be used :3"
                        print(message_existence)
                        return

        # If json was not found in the directories.
        self.existence_json = False
        self.pathway_json = None
        print(message_existence)

    def verify_correct_repo_of_json(self, json_file:dict= None) -> None:
        """
        Things to verify:
            - licence/
                - name
                - url
            - repository

        """

        if json_file == None:
            self.verify_existence_local_json()
            if not self.existence_json:
                return

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
            # If json's repo doesn't match, set the global variable "correct_repo" to False; if correct, set it to True. Display message to user about file being incorrect.
            validate(instance=json_file, schema=schema_anime_offline_database)
            self.correct_repo =  True
            output_message = "Sucess! Correct repo :3"
        except ValidationError as e:
            self.correct_repo = False
            output_message = f"Incorrect repo :'(. \n\nError message: {e}"
        
        print(output_message)


        
    def compare_last_update(self, online_json_date:str, local_json_date:str=None) -> str: # RFER 10
        """
        Check date of repo and determine whether to download newest json from repo

        entry in json: "lastUpdate"
        """
        try:
            with open(self.pathway_json) as file:
                local_json_file:dict = json.load(file)
                local_json_date:str = local_json_file['lastUpdate']
                file.close()
        except:
            print("Local json doesn't exist :'[")
            return
        date_parameters:str = '%Y-%m-%d'
        date_local_json:datetime = datetime.strptime(local_json_date, date_parameters)
        date_online_repo:datetime = datetime.strptime(online_json_date, date_parameters)

        if date_local_json >= date_online_repo:
            self.latest_json = True
            print("The local json is up-to-date :3")
        else:
            self.latest_json = False
            print("There's a newer json online :O")


    def move_old_json_to_backup_folder(self) -> None: # TODO
        """
        
        Idea: Before the new json is saved, move the old json into a separate folder as backup incase the download of the new json fails.

        """
        print("Currect action: moving existing json into backup folder.")

        conditions:list[bool] = [
            self.existence_json, 
            self.latest_json,
        ]

        # Exit immedately if 2 conditions aren't met
        match conditions:
            case [True, False]: # move existing file into new folder # self.existence_json == True and self.latest_json == False
                print("There is an existing json. Moving it into backup folder.")
                
                try: # Execute moving folder.
                    
                    print("Finished moving to backup folder.")
                except:
                    print("Action was interrupted. :'[")
                
            case [False, True]:
                print("It doesn't exist, so nothing was moved")
            case other:
                print("Something broke, but nothing was moved.")



    def progress_bar_download(self, response: Response= None) -> None:
        if response == None:
            return # Debug; end early

        # output_response = response.json()
        output_response = None
        
        total_size_bytes:int = int(response.headers.get('content-length', 0))
        block_size:int = 1024
        progress_bar = tqdm(
            total=total_size_bytes,
            unit='iB',
            unit_scale=True
        )

        for data in response.iter_content(block_size):
            progress_bar.update(len(data))
            output_response += data

        progress_bar.close()

        if total_size_bytes != 0 and progress_bar.n != total_size_bytes:
            print("Error: The download broke :'[")
        
        return output_response

    def download_json(self, debug_force_fail_connection:bool = False) -> dict:
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
        response:Response = requests.get(url, stream=True)
        anime_db_json_name:str = 'anime-offline-database-minified.json'

        # if response.status_code == 200:
        #     self.progress_bar_download(response=response)

        if response.status_code != 200:
            # TODO - If failed to download minified json, download regular json
            print("Error #1: Failed to download minified ")
            url = url_json["regular"]
            response = requests.get(url,stream=True)
            anime_db_json_name:str = 'anime-offline-database.json'

            # if response.status_code == 200:
            #     self.progress_bar_download(response=response)
            
            if response.status_code != 200:
                anime_db_json_name = None
                response = None

                print("ERROR #2: Failed to download REGULAR anime offline database as well :[")
        self.current_online_database = anime_db_json_name
        
        output_json = response.json()
        return output_json

    def save_json(self, response_json:dict): # TODO - Discard download bar for now. potentially, move the the download bar back to "download_json" function if I want to maintain progress bar. Biggest hurdle: separating saving the file from the progress bar.
        new_directory = r'./database_project_manami'
        if not os.path.exists(new_directory): # RFER 04
            os.makedirs(new_directory)

        # This saves the newly downloaded json to local storage.
        new_relative_path:str = f'database_project_manami/{self.current_online_database}'

        with open(new_relative_path, mode= 'w+') as file:
            
            file.write(json.dumps(response_json, indent=1))

        file_size:int = ((os.stat(new_relative_path).st_size) / (10**6)) # RFER 05 && RFER 06

        message_download = f'Sucessfully downloaded one of the databases! "{self.current_online_database}" was downloaded and saved locally with the size of ({file_size} mb) :D'
        
        # self.current_online_database = None # Reset to None

        print(message_download)


class parsed_anime_database:
    pass

class parsed_user_list:
    pass
    
if __name__ == '__main__':
    padb = parsed_anime_database()
    
    padb.debug_only___psuedocode_for_ui_execute_downloading_json()
    print("done!")