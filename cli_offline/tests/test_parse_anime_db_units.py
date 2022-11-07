from enum import auto
from types import NoneType
import pytest
from src.parse_anime_db import download_anime_database_json
from datetime import date
import requests

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

        download_p_a_db.verify_existence_local_json()

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

    def test_status_302_project_minami_json(self):
        # Test minified json
        response_status:int = requests.head('https://github.com/manami-project/anime-offline-database/blob/master/anime-offline-database-minified.json?raw=true').status_code
        assert response_status == 302, ''

        # Test regular json
        response_status = requests.head('https://github.com/manami-project/anime-offline-database/blob/master/anime-offline-database.json?raw=true').status_code # This results in response status '302'
        assert response_status == 302

    def test_download_json_response_status_200(self, download_json_minami_project):
        download_p_a_db:download_anime_database_json = download_anime_database_json()
        output_json:dict = download_p_a_db.download_json() # Test mainly for response
        response_message = download_p_a_db.debugging_status_code_from_downloading

        assert output_json != None, f"Download resulted in a NoneType. Error message: '{response_message}'"
        assert response_message == 200, f"Response status: {response_message}"
        self.check_file_existence_local_json()


    def test_download_json_verify_file(self, download_json_minami_project):
        output_json = download_json_minami_project

        output_string = output_json['license']['name']
        assert output_string == manami_project_json_license_name, f"Output:{output_string}"

        output_string = output_json['license']['url']
        assert output_json['license']['url'] == manami_project_json_license_url, f"Output:{output_string}"

        output_string = output_json['repository']
        assert output_string == manami_project_json_repository, f"Output:{output_string}"


    def test_delete_local_json(self):
        fail_intentionally_sadge()
