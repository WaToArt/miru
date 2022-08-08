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

def test_get_id_kitsu(class_info_wotakoi, anime_wotaku_id_kitsu):

    assert class_info_wotakoi.id_kitsu == anime_wotaku_id_kitsu

def test_get_id_anilist(class_info_wotakoi, anime_wotaku_id_anilist):
    
    assert class_info_wotakoi.id_anilist == anime_wotaku_id_anilist


# === Tests - class "anime" ===

def test_anime_get_mal_link(anime_wotaku_ni_koi):
    output = anime_wotaku_ni_koi.link_mal

    assert output == "https://myanimelist.net/anime/35968"

def test_anime_get_kistu_link(anime_wotaku_ni_koi):
    output = anime_wotaku_ni_koi.link_kitsu

    assert output == "https://kitsu.io/anime/13660"

def test_anime_get_anilist_link(anime_wotaku_ni_koi):
    output = anime_wotaku_ni_koi.link_anilist

    assert output == "https://anilist.co/anime/99578"


# === Tests - class "Manga" ===
def test_manga_get_MAL_link(manga_horimiya):
    output = manga_horimiya.link_mal

    assert output == "https://myanimelist.net/manga/42451"

def test_manga_get_Kitsu_link(manga_horimiya, na_link_kitsu): 
    # FIXME - Unable to get raw manga id number for Kitsu... Will work on this test later when id number is obtained.
    ## For now, purposely have the output return the "Kitsu doesn't have a webpage :'["
    output = manga_horimiya.link_kitsu

    assert manga_horimiya.id_kitsu == None
    assert output == na_link_kitsu


def test_manga_get_anilist_link(manga_horimiya):
    output = manga_horimiya.link_anilist

    assert output == "https://anilist.co/manga/72451"

