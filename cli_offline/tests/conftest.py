import pytest
from src.ui import user_interface

@pytest.fixture(scope="class")
def setup_ui():
    return user_interface()