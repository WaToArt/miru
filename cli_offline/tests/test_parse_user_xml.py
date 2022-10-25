from enum import auto
from types import NoneType
import pytest
from src.parse_user_xml import parsed_user_list_xml
from datetime import date

from pytest_socket import socket_disabled


def fail_intentionally_sadge():
    assert None == "failed intentionally"


class Tests_UNITS_parsed_user_list_xml:
    
    def test_set_website(self):
        foo_class:parsed_user_list_xml = parsed_user_list_xml()

        fail_intentionally_sadge()

    def test_search_xml_location(self):
        foo_class:parsed_user_list_xml = parsed_user_list_xml()

        fail_intentionally_sadge()

    def test_parse_xml(self):
        fail_intentionally_sadge()

    def test_grab_anime_info(self):
        """ Grab Wotakoi anime info, and focus on these info:
            
                <anime>
                <series_animedb_id>35968</series_animedb_id>
                <my_watched_episodes>11</my_watched_episodes>
                <my_start_date>2022-07-29</my_start_date>
                <my_finish_date>2022-07-29</my_finish_date>
                <my_status>Completed</my_status>
                <my_times_watched>0</my_times_watched>
            </anime>
            """
        expectations:dict = {
            "series_animedb_id": 35968,
            "my_watched_episodes": 11,
            "my_start_date": date(2022, 7, 29),
            "my_finish_date": date(2022, 7, 29),
            "my_status": "Completed",
            "my_times_watched": 0,
        }

        foo_class:parsed_user_list_xml = parsed_user_list_xml()



        


        output:dict = None
        assert output == expectations