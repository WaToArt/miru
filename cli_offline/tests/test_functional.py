import pytest
from pytest import CaptureFixture
from src.ui import user_interface
from src.parse_anime_db import download_anime_database_json

def fail_intentionally_sadge():
    assert None == "failed intentionally"

message_purposely_failed:str = 'failed on purpose'

welcome_message:str = "Welcome to Project miru 『見る』! Type in one of the options to continue :3\n"

option_all_random_anime:str = "Give me any anime that exists!\n"
option_select_from_user_list:str = "Give me a random anime of my list!\n"
option_list_all_my_lists:str = "List all of my anime!\n"
option_download_database:str = "Download the database!\n"


class Tests_user_cli:
    

    def test_executing_rolling_any_random_title_from_overall_anime_database(self, capsys:CaptureFixture):
        ui: user_interface = user_interface()


        # Mark opens the application for the first time, and is greeted with the options they can interact with. 
        ui.start_program()
        captured = capsys.readouterr()
        assert welcome_message in captured.out # TODO - Check if this fixture works as like "captured.out"

        # Mark decides that he wants to obtain a random anime to watch. However, the app (application) detects that this is Mark's first time launching the program. The program asks if they want to download the json of the anime database.


        # Mark accidentally said no. The application displayed a message saying that to either manually download the anime database (with link to GitHub) or let the program download the Json. Then, the application returns back to the menu.

            
        # Mark decided to say yes to download the file. The program will download the json if Mark types yes OR Mark timed out after 5 seconds.
            ## The program will download the json if Mark types yes OR Mark timed out after 5 seconds.
            ## If download failed, pop a 5 second failed-message and only return back to the options list.
        
        # Purposely fail
        fail_intentionally_sadge()    
    def test_executing_grabbing_random_anime_from_user_list(self, capsys):

        # Mark decides that he wants to obtain a random anime to watch. However, the application (app) detects that this is Mark's first time launching the program. The program asks if they want to download the json of the anime database. The program will download the json if Mark types yes OR Mark timed out after 5 seconds.
            
            ## If Mark said no, the application will default to linking the anime's raw ID and MAL (MyAnimeList) link from Mark's list.

            ## If download failed, pop a 5 second message and only return the raw ID and MAL link.

        # Purposely fail
        fail_intentionally_sadge()

class Tests_FUNCTIONAL_download_anime_database_json:

    def test_download_and_saving_json():

        fail_intentionally_sadge()