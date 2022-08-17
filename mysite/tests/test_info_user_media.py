import pytest

from mypkg.info_user_media import info, manga, anime, lightnovel
from tests.conftest import *

# ==================== TESTS ====================


# === Tests - class "info" ===
def test_get_title(class_info_wotakoi, anime_wotaku_title):
    output = class_info_wotakoi.title
    assert output == anime_wotaku_title

def test_get_id_primary(class_info_wotakoi, anime_wotaku_id_mal):

    output = class_info_wotakoi.id_primary
    assert output == anime_wotaku_id_mal

def test_get_id_myanimelist(class_info_wotakoi, anime_wotaku_id_mal):

    output = class_info_wotakoi.id_mal
    assert output == anime_wotaku_id_mal



# === Tests - class "anime" ===


def test_set_kitsu_link_has_input(anime_wotaku_link_kitsu):
    test_kitsu_link = anime(35968)
    wotakoi_kitsu_url_with_id = "https://kitsu.io/anime/13660"
    test_kitsu_link.set_kitsu_link(wotakoi_kitsu_url_with_id)

    assert test_kitsu_link.link_kitsu == anime_wotaku_link_kitsu

def test_set_kitsu_link_None():
    test_class_kitsu_link_None = anime(35968)
    test_class_kitsu_link_None.set_kitsu_link(None)
    
    output = test_class_kitsu_link_None.link_kitsu
    assert output == "Kitsu.io doesn't have a page :'("

def test_set_anilist_link_has_input(anime_wotaku_link_anilist):
    test_class_anilist_link_exists = anime(35968)
    test_class_anilist_link_exists.set_anilist_link("https://anilist.co/anime/99578")

    output = test_class_anilist_link_exists.link_anilist
    assert output == anime_wotaku_link_anilist

def test_set_anilist_link_None():
    test_class_anilist_link_None = anime(35968)
    test_class_anilist_link_None.set_anilist_link(None)

    output = test_class_anilist_link_None.link_anilist
    assert output == "Anilist doesn't have a webpage ;["