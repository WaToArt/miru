from doctest import OutputChecker
import pytest

from scans.scan_xml import scan_xml

def test_root_tag_and_attri(xml_kitsu_anime_location, kitsu):
    foo_scan_xml = scan_xml(xml_kitsu_anime_location, kitsu, 'anime')
    output = f"{foo_scan_xml.root.tag} + {foo_scan_xml.root.attrib}"

    assert output == "myanimelist + {}"

def test_text_at_element_0_and_1(xml_kitsu_anime_location, kitsu):
    foo_scan_xml = scan_xml(xml_kitsu_anime_location, kitsu, 'anime')
    
    # Full info:
    ## <user_export_type>1</user_export_type>
    output = f"{foo_scan_xml.root[0][0].text}"
    assert output == "1"

def test_root_iter_no_arg(xml_kitsu_anime_location, kitsu):
    foo_scan_xml = scan_xml(xml_kitsu_anime_location, kitsu, 'anime')

    output:list = foo_scan_xml.check_ids_all_status()
    assert output == [48556, 40417, 50265, 35968, 46095] # DO NOT SORT LIST

def test_root_iter_with_arg(xml_kitsu_anime_location, kitsu):
    foo_scan_xml = scan_xml(xml_kitsu_anime_location, kitsu, 'anime')
    output:list = foo_scan_xml.check_ids_all_status('series_animedb_id')
    assert output == [48556, 40417, 50265, 35968, 46095] # DO NOT SORT LIST

def test_check_len_root_list(xml_kitsu_anime_location, kitsu):
    foo_scan_xml = scan_xml(xml_kitsu_anime_location, kitsu, 'anime')
    anime_ids:list = foo_scan_xml.check_ids_all_status('series_animedb_id')
    output = len(anime_ids)

    assert output == 5

def test_check_animeid_MAL(xml_kitsu_anime_location, kitsu, args_db_info):
    foo_scan_xml = scan_xml(xml_kitsu_anime_location, kitsu, 'anime')
    list_objects_info_db = foo_scan_xml.check_animeid_MAL()
    output = list_objects_info_db[0]

    assert output.id_media == args_db_info[0]
    assert output.my_status == args_db_info[1]
    assert output.format_media == args_db_info[2]
