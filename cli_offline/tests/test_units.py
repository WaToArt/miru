from enum import auto
import pytest
from src.parse_info import parsed_anime_database
from src.ui import user_interface

repository_manami_project_json:str = "https://github.com/manami-project/anime-offline-database"

def fail_intentionally_sadge():
    assert None == "failed intentionally"
class Tests_parsed_anime_database:

    def test_check_existence_local_json(self):
        p_a_db:parsed_anime_database = parsed_anime_database()

        assert p_a_db.existence_json == False, f"Should report false when first launch."

        output_pathway_json:str = p_a_db.check_existence_local_json()
        assert p_a_db.existence_json == True, f"Method runs and checks that the json exists locally."
        
        assert output_pathway_json == './database_project_manami/anime-offline-database-minified.json'
    
    def test_verify_correct_repo_local_file_exists(self):
        p_a_db:parsed_anime_database = parsed_anime_database()

        assert p_a_db.correct_repo == False,'Start up should be immediately False'

        p_a_db.verify_correct_repo_of_json()
        assert p_a_db.correct_repo == True, ''