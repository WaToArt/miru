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
    
    def check_local_json(self) -> bool:
        # Check if json exist locally in directory "databases"
        if anime_database_exists:
            self.existence_json = True
        else:
            self.existence_json = False

    def check_repo_of_json(self, json):
        pass

    def download_json(self):
        # TODO - Download minified json

            # TODO - If failed to download minified json, download regular json
        
        pass


class parsed_user_list:
    pass