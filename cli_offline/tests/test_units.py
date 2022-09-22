from enum import auto
import pytest
from src.parse_info import parsed_anime_database
from src.ui import user_interface

repository_manami_project_json:str = "https://github.com/manami-project/anime-offline-database"

def fail_intentionally_sadge():
    assert None == "failed intentionally"
class Tests_parsed_anime_database:


    def test_parsed_anime_database(self):
        p_a_db:parsed_anime_database = parsed_anime_database()

        assert p_a_db.verified_repo == True, f"The repo is not from {repository_manami_project_json}"
