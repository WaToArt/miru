import pytest
from src.parse_anime_db import download_anime_database_json

@pytest.fixture(scope="session")
def download_json_minami_project():
    dadj: download_anime_database_json = download_anime_database_json()

    output_json = dadj.download_json()

    return output_json

