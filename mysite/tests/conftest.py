import pytest

from mypkg.info_user_media import info, manga, anime, lightnovel

# 1 - Info how how conftest.py works with pytest.fixtures: https://docs.pytest.org/en/6.2.x/fixture.html#scope-sharing-fixtures-across-classes-modules-packages-or-session
# === Arrange - "webpage doesn't exist" variables ===
@pytest.fixture()
def na_link_mal() -> str: # na = Not available
    return "MyAnimeList doesn't have a page :'["

@pytest.fixture
def na_link_kitsu() -> str:
    return "Kitsu.io doesn't have a page :'("

@pytest.fixture
def na_link_anilist() -> str:
    return "Anilist doesn't have a webpage ;["


# === Arrange - class "info" ===
@pytest.fixture()
def class_info_wotakoi() -> info:
    info_wotakoi = info(35968)    
    info_wotakoi.id_anilist = 99578
    info_wotakoi.title = "Wotaku ni Koi wa Muzukashii"
    info_wotakoi.id_mal = 35968

    return info_wotakoi

@pytest.fixture(autouse=True)
def info_wotakoi_title(class_info_wotakoi) -> None:
    class_info_wotakoi.id_kitsu = 13660


# === Arrange - fixture "Wotaku"/"Wotakoi" ===
@pytest.fixture
def anime_wotaku_title() -> str:
    return "Wotaku ni Koi wa Muzukashii"

@pytest.fixture
def anime_wotaku_id_mal() -> int:
    return 35968

@pytest.fixture
def anime_wotaku_id_kitsu() -> int:
    return 13660

@pytest.fixture
def anime_wotaku_id_anilist() -> int:
    return 99578

@pytest.fixture
def anime_wotaku_link_mal() -> str:
    return "https://myanimelist.net/anime/35968"

@pytest.fixture
def anime_wotaku_link_anilist() -> str:
    return "https://anilist.co/anime/99578"

@pytest.fixture
def anime_wotaku_link_kitsu() -> str:
    return "https://kitsu.io/anime/13660"

@pytest.fixture
def anime_wotaku_ni_koi(anime_wotaku_title,anime_wotaku_id_kitsu,anime_wotaku_id_anilist) -> anime: # Uses MAL database
    anime_wotakoi = anime(35968)

    # # Method 1 - works, but this manually call functions 1 by 1. These function calls were already tested from its father class, "info".
    # anime_wotakoi.title = ("Wotaku ni Koi wa Muzukashii")
    # anime_wotakoi.id_mal = (35968)
    # anime_wotakoi.id_kitsu = (13660)
    # anime_wotakoi.id_anilist = (99578)

    # # Method 2 - This works as well, but let's independently input the parameters for reliablibity reasons
    # anime_wotakoi.use_database_MAL(anime_wotaku_title,anime_wotaku_id_kitsu,anime_wotaku_id_anilist)



    # # Method 3 AND preferred way - Primary way to setup class as it also explains which database is being used (name of function) AND check that all of the functions are working properly.
    # ## Shifting these two functions into "autouse" fixture
    # anime_wotakoi.use_database_MAL("Wotaku ni Koi wa Muzukashii", 13660, 99578) 

    return anime_wotakoi

@pytest.fixture(autouse=True)
def anime_wotakoi_use_db_MAL(anime_wotaku_ni_koi) -> None:
    anime_wotaku_ni_koi.use_database_MAL("Wotaku ni Koi wa Muzukashii", 13660, 99578) 
    anime_wotaku_ni_koi.set_all_links()



# === Arrange - class "manga" ===

@pytest.fixture
def manga_horimiya() -> manga:
    manga_horimiya = manga(42451)
    manga_horimiya.use_database_MAL("Horimiya", None, 72451)
    manga_horimiya.set_all_links()

    return manga_horimiya

# === Arrange - class "lightnovel" ===
@pytest.fixture
def ln_86() -> lightnovel: # ln = light novel
    ln_86_title = "86"
    ln_86_mal_id = 104039
    ln_86_kitsu_id = None
    ln_86_anilist_id = 98610


    ln_86 = lightnovel(ln_86_mal_id)
    ln_86.use_database_MAL(ln_86_title, ln_86_kitsu_id,ln_86_anilist_id)

    return ln_86

# ====== Module - "test_scan_files.py" ======

# === Arrange - class "read_file" - #TODO - COmmented temporary to focus on learning how conftest.py works with pytext.fixtures
@pytest.fixture
def xml_kitsu_anime_location() -> str:
    return "./xml_files/xml_kitsuio/kitsu--anime.xml"
@pytest.fixture
def kitsu() -> str:
    return "Kitsu"

# ====== Module - "info_db.py" ======

# === Arrange - class "id_info" ===
@pytest.fixture
def args_db_info():
    args_db_info:list = [48556, "Dropped", "anime"]
    return args_db_info

# ====== Module - "scan_json.py" =====
@pytest.fixture
def offline_anime_json_path():
    return "./databases/anime-offline-database.json"

@pytest.fixture
def mamani_project_anime_db_repo_url():
    return "https://github.com/manami-project/anime-offline-database"

