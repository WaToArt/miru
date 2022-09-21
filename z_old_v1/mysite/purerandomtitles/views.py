from django.shortcuts import render

from scans.scan_json import scan_json
from scans.scan_xml import scan_xml, Kitsu_anime_xml
# Create your views here.

def index(request):
    scan_json_class = scan_json()
    scan_json_class.run_db_online()
    # scan_json_class.run_db_offline('../databases/anime-offline-database-minified.json')
    scan_json_class.set_any_random_title()
    randomDbTitle = scan_json_class.grab_title()
    random_MAL = scan_json_class.obtain_anime_all_sources()
    randomDbMAL = f"{random_MAL.get('mal')}"


    class_xml = Kitsu_anime_xml('anime')
    random_id = class_xml.get_random_id_v2()
    randomUserMAL = f'https://myanimelist.net/anime/{str(random_id)}'
    scan_json_class.set_current_anime_from_db(randomUserMAL)
    randomUserAnime = scan_json_class.grab_title()

    return render(request, "purerandomtitles/index.html",{
        "randomUserMAL": randomUserMAL,
        "randomUserAnime": scan_json_class.grab_title(),
        
        "randomDbTitle": randomDbTitle,
        "randomDbMAL": randomDbMAL
    })

