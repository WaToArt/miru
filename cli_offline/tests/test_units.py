from enum import auto
import pytest
from src.parse_info import download_anime_database_json

from pytest_socket import socket_disabled
repository_manami_project_json:str = "https://github.com/manami-project/anime-offline-database"

name_minified_anime_database:str = "anime-offline-database-minified.json"
name_regular_anime_database:str = "anime-offline-database.json"

def fail_intentionally_sadge():
    assert None == "failed intentionally"
class Tests_download_anime_database_json:

    def check_file_existence_local_json(self, ): # Have this run when Json is downloaded instead.
        p_a_db:download_anime_database_json = download_anime_database_json()
        
        assert p_a_db.existence_json == False, f"Should report false when first launch."

        output_message:str = p_a_db.verify_existence_local_json()
        assert p_a_db.existence_json == True, f"Method runs and checks that the json exists locally."
        
        assert './database_project_manami/' or '/database_project_manami/' in p_a_db.pathway_json  
        assert name_minified_anime_database or name_regular_anime_database in p_a_db.pathway_json


        assert 'was found. This will be used :3' in output_message


    
    def test_download_json_sucess(self):
        p_a_db:download_anime_database_json = download_anime_database_json()
        output_message = p_a_db.download_json()

        assert "Sucessfully downloaded one of the databases!" and "was downloaded" in output_message
        assert name_regular_anime_database or name_minified_anime_database in output_message

        self.check_file_existence_local_json(p_a_db)
        
    def test_download_json_failed(self): #force offline mode so no network connection is made
        
        p_a_db:download_anime_database_json = download_anime_database_json()
        output_message = p_a_db.download_json(True)
        
        assert output_message == "Failed to either Json options for anime offline databases :'["
    def test_verify_correct_repo_local_file_exists(self):
        p_a_db:download_anime_database_json = download_anime_database_json()

        assert p_a_db.correct_repo == False,'Start up should be immediately False'

        p_a_db.verify_correct_repo_of_json()
        assert p_a_db.correct_repo == True, ''
