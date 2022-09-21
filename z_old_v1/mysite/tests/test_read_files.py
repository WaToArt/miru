
from scans.scan_xml import read_file
# ====== class "read_file" ======

# === Tests - class "read_file"
def test_read_file_file_found(xml_kitsu_anime_location):
    log_file = read_file()
    output = log_file.readline_file(xml_kitsu_anime_location)

    assert output == '<?xml version="1.0"?>'

def test_read_file_errored():
    log_file = read_file()
    output = log_file.readline_file('nothing')
    assert output == "sadge ੨( ･᷄ ︵･᷅ )ｼ. Error: [Errno 2] No such file or directory: 'nothing'" 
