import os
import json
from pickletools import int4
from xml.dom import ValidationErr
from xml.etree import ElementTree as ET

import requests
from requests import Response, models
from requests.exceptions import ConnectionError

from tqdm.auto import tqdm
from os import devnull
from docopt import docopt

from jsonschema import validate, ValidationError

from datetime import datetime, date
import os, sys

class parsed_user_list_xml:
    def __init__(self) -> None:
        self.website:str = None

        self.xml_location:str = None

    def set_website(self, website:str=None) -> None:
        match website:
            case "mal":
                print("Setting to: mal (MyAnimeList)")
                self.website = "mal"
            case "anilist":
                print("Setting to: anilist")
                self.website = "anilist"
            case "kitsu":
                print("Setting to: kitsu")
                self.website = "kitsu"
            case _:
                print("Unexpected input. Defaulting to: 'mal' (myanimelist)")
                self.website = "mal"

    def search_xml_location(self) -> str: # TODO
        website_locations:dict = {
            'mal': ['./xml_files/xml_mal', 
            '../xml_files/xml_mal'],

            'anilist': ['./xml_files/xml_anilist',
            '../xml_files/xml_anilist'],

            'kitsu': ['./xml_files/xml_kitsuio',
            '../xml_files/xml_kitsuio']
        }
        website_substrings:dict = {
            'mal': ['animelist_', 
            ],
            
            'anilist': ['scrape_anilistanimealt', 
            ],
            
            'kitsu': ['kitsu--anime', 
            ],
        }

        chosen_site_substring:list[str] = website_substrings.get(self.website)
        chosen_site_locations:list[str] = website_locations.get(self.website)

        for location in chosen_site_locations:
            for root, dirs, files, in os.walk(location):
                for file in files:
                    for substring in chosen_site_substring:
                        if substring in file and file.endswith('.xml'):
                            xml_location = os.path.join(root,file)

                            self.xml_location = xml_location
                            # return xml_location
    
    def parse_xml(self, file_name:str = None):
        if file_name == None:
            file_name = self.search_xml_location()

        try:
            tree = ET.parse(file_name) # These commands negate the need for "with open"
            return tree.getroot()

        except FileNotFoundError as E:
            print(f"Error: {E}")
            print("Ending program now.")
            sys.exit()

