from enum import auto
import pytest
from src.parse_info import parsed_anime_database
from src.ui import user_interface

from pytest_socket import socket_disabled
repository_manami_project_json:str = "https://github.com/manami-project/anime-offline-database"

def fail_intentionally_sadge():
    assert None == "failed intentionally"
class Tests_parsed_anime_database:

    def check_existence_local_json(self): # Have this run when Json is downloaded instead.
        p_a_db:parsed_anime_database = parsed_anime_database()

        assert p_a_db.existence_json == False, f"Should report false when first launch."

        p_a_db.check_existence_local_json()
        assert p_a_db.existence_json == True, f"Method runs and checks that the json exists locally."
        assert p_a_db.pathway_json == './database_project_manami/anime-offline-database-minified.json'
    
    def test_download_json_sucess(self):
        p_a_db:parsed_anime_database = parsed_anime_database()
        output_message = p_a_db.download_json()

        assert "Sucessfully downloaded one of the databases!" and "was downloaded" in output_message
        assert 'anime-offline-database.json' or 'anime-offline-database-minified.json' in output_message

        self.check_existence_local_json()
        
    def test_download_json_failed(self): #force offline mode so no network connection is made
        
        p_a_db:parsed_anime_database = parsed_anime_database()
        output_message = p_a_db.download_json(True)
        
        assert output_message == "Failed to either Json options for anime offline databases :'["
    def test_verify_correct_repo_local_file_exists(self):
        p_a_db:parsed_anime_database = parsed_anime_database()

        assert p_a_db.correct_repo == False,'Start up should be immediately False'

        p_a_db.verify_correct_repo_of_json()
        assert p_a_db.correct_repo == True, ''
