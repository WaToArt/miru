import pytest

from mypkg.info_db_media import db_info



def test_get__str___(args_db_info):
    foo_db_info_1 = db_info(args_db_info[0], args_db_info[1], args_db_info[2])
    output = str(foo_db_info_1)
    assert output == "48556 | Dropped"

def test_get_id_number(args_db_info):
    foo_db_info_2 = db_info(args_db_info[0], args_db_info[1], args_db_info[2])
    output_2 = foo_db_info_2.id_media
    assert output_2 == 48556, "Should return 48556 if arg was '48556'"
def test_get_status(args_db_info):
    foo_db_info_3 = db_info(args_db_info[0], args_db_info[1], args_db_info[2])
    output_3 = foo_db_info_3.my_status

    assert output_3 == "Dropped", "Should return status 'Dropped'"

def test_get_format_media(args_db_info):
    foo_db_info_4 = db_info(args_db_info[0], args_db_info[1], args_db_info[2])
    output = foo_db_info_4.format_media

    assert output == "anime"


