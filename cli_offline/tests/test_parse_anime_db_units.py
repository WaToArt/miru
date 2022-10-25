from enum import auto
from types import NoneType
import pytest
from src.parse_info import download_anime_database_json, parsed_user_list_xml
from datetime import date

from pytest_socket import socket_disabled

manami_project_json_license_name:str = "GNU Affero General Public License v3.0"
manami_project_json_license_url:str = "https://github.com/manami-project/anime-offline-database/blob/master/LICENSE"
manami_project_json_repository:str = "https://github.com/manami-project/anime-offline-database"

name_minified_anime_database:str = "anime-offline-database-minified.json"
name_regular_anime_database:str = "anime-offline-database.json"

def fail_intentionally_sadge():
    assert None == "failed intentionally"


class Tests_UNITS_download_anime_database_json:

    def check_file_existence_local_json(self, ): # Have this run when Json is downloaded instead.
        download_p_a_db:download_anime_database_json = download_anime_database_json()
        
        assert download_p_a_db.existence_json == False, f"Should report false when first launch."

        download_p_a_db.verify_existence_local_json()
        assert download_p_a_db.existence_json == True, f"Method runs and checks that the json exists locally."
        assert './database_project_manami/' or '/database_project_manami/' in download_p_a_db.pathway_json  
        assert name_minified_anime_database or name_regular_anime_database in download_p_a_db.pathway_json


        # assert 'was found. This will be used :3' in output_message



    def test_verify_correct_repo_local_file_exists(self):
        download_p_a_db:download_anime_database_json = download_anime_database_json()

        assert download_p_a_db.correct_repo == False,'Upon start up, it should be immediately False'

        download_p_a_db.verify_correct_repo_of_json()
        assert download_p_a_db.correct_repo == True, 'After checking, the file should exist.'
    def test_compare_last_update(self):
        fail_intentionally_sadge()

    def test_move_old_json_to_backup_folder(self):
        fail_intentionally_sadge()

    def test_download_json_sucess(self):
        download_p_a_db:download_anime_database_json = download_anime_database_json()
        output_json:dict = download_p_a_db.download_json()
        response_message = download_p_a_db.debugging_status_code_from_downloading

        assert output_json != None, f"Download resulted in a NoneType. Error message: '{response_message}'"
        assert response_message == 200, f"Response status: {response_message}"

        output_string = output_json['license']['name']
        assert output_string == manami_project_json_license_name, f"Output:{output_string}"

        output_string = output_json['license']['url']
        assert output_json['license']['url'] == manami_project_json_license_url, f"Output:{output_string}"

        output_string = output_json['repository']
        assert output_string == manami_project_json_repository, f"Output:{output_string}"

        self.check_file_existence_local_json()

    def test_delete_local_json(self):
        fail_intentionally_sadge()
