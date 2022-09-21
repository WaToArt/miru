from email.generator import Generator
import pytest
from pytest import CaptureFixture
from src.ui import user_interface

messenge_purposely_failed:str = 'failed on purpose'
class Tests_user_cli:
    

    def test_executing_rolling_any_random_title_from_overall_anime_database(self, capsys:CaptureFixture):
        ui: user_interface = user_interface()


        # Mark opens the application for the first time, and is greeted with the options they can interact with. 
        ui.start()
        captured: CaptureFixture[str] = capsys.readouterr()
        assert "Welcome to Project miru 『見る』! Type in one of the options to continue :3" in captured._captured_out # TODO - Check if this fixture works as like "captured.out"

        # Mark decides that he wants to obtain a random anime to watch. However, the prompt asks whether or not 

        
        
        
        
        
        # Purposely fail
        assert None == messenge_purposely_failed
    
    def test_executing_grabbing_random_anime_from_user_list(self, capsys):

        assert None == messenge_purposely_failed