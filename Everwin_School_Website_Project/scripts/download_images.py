from pathlib import Path
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

BASE = Path(__file__).resolve().parent.parent
SOURCES = {
    'images/09_Sembium/sembium_building.jpg': 'https://everwinschool.com/sembium-buliding.jpg',
    'images/10_General/family.png': 'https://everwinschool.com/family.png',
    'images/01_Kolathur_CBSE/kolathur_campus_01.jpg': 'https://www.everwinschool.com/img/school/kollathur_cbse/kolathur_cbse1.jpg',
    'images/01_Kolathur_CBSE/kolathur_campus_02.jpg': 'https://www.everwinschool.com/img/school/kollathur_cbse/kolathur_cbse2.jpg',
    'images/01_Kolathur_CBSE/kolathur_activity_03.jpg': 'https://www.everwinschool.com/img/school/kollathur_cbse/kolathur_cbse3.jpg',
    'images/01_Kolathur_CBSE/kolathur_building_04.jpg': 'https://www.everwinschool.com/img/school/kollathur_cbse/kolathur_cbse4.jpg',
    'images/01_Kolathur_CBSE/kolathur_cricket_05.jpg': 'https://www.everwinschool.com/img/school/kollathur_cbse/kolathur_cbse5.jpg',
    'images/01_Kolathur_CBSE/kolathur_computer_lab_06.jpg': 'https://www.everwinschool.com/img/school/kollathur_cbse/kolathur_cbse6.jpg',
    'images/01_Kolathur_CBSE/kolathur_class_activity_07.jpg': 'https://www.everwinschool.com/img/school/kollathur_cbse/kolathur_cbse7.jpg',
    'images/01_Kolathur_CBSE/kolathur_chess_08.jpg': 'https://www.everwinschool.com/uploadimages/schoolgal/20180109040958kolathur_cbse8.jpg',
    'images/01_Kolathur_CBSE/kolathur_classroom_09.jpg': 'https://www.everwinschool.com/img/school/kollathur_cbse/kolathur_cbse9.jpg',
    'images/01_Kolathur_CBSE/kolathur_smart_class_10.jpg': 'https://www.everwinschool.com/img/school/kollathur_cbse/kolathur_cbse20.jpg',
    'images/02_Mathur/mathur_gate_01.jpg': 'https://www.everwinschool.com/img/school/mathur/mathur3.jpg',
    'images/02_Mathur/mathur_building_02.jpg': 'https://www.everwinschool.com/img/school/mathur/mathur4.jpg',
    'images/03_Janakipuram/janakipuram_inauguration.jpg': 'https://www.everwinschool.com/img/school/janakipuram/Janakipuraminaugurationimage.jpg',
    'images/04_Surapet/surapet_entrance.jpg': 'https://everwinschool.com/img/school/surapet/surapet_entrance.jpeg',
    'images/04_Surapet/surapet_admission_gate.jpg': 'https://everwinschool.com/img/school/surapet/WhatsApp%20Image%202022-12-28%20at%2010.59.49%20AM%20%281%29.jpeg',
    'images/04_Surapet/surapet_campus_block.jpg': 'https://everwinschool.com/img/school/surapet/WhatsApp%20Image%202022-12-28%20at%2010.59.49%20AM.jpeg',
    'images/05_Management/founder_dr_b_purushothaman.jpg': 'https://www.everwinschool.com/images/Mr.Purushothaman.jpg',
    'images/05_Management/ceo_mrs_v_mageswari.jpg': 'https://www.everwinschool.com/images/Mrs.Mageswari.jpg',
    'images/05_Management/mathur_principal_sanjitha_baanu.jpg': 'https://www.everwinschool.com/images/Founder/Sanjitha_Baanu_S.jpg',
    'images/06_Brand/everwin_kolathur_logo.png': 'https://www.everwinschool.com/images/School-Logo/logo-kolathur-vid.png',
    'images/06_Brand/everwin_surapet_logo.png': 'https://everwinschool.com/images/School-Logo/Everwin%20Vidhyashram%20Surapet%20Logo.png',
    'images/07_Awards/award_screen_1.jpg': 'https://www.everwinschool.com/images/Founder/Screen%201.jpg',
    'images/07_Awards/award_screen_2.jpg': 'https://www.everwinschool.com/images/Founder/Screen%202.jpg',
    'images/07_Awards/award_screen_3.jpg': 'https://www.everwinschool.com/images/Founder/Screen%203.jpg',
    'images/07_Awards/award_screen_4.jpg': 'https://www.everwinschool.com/images/Founder/Screen%204.jpg',
    'images/07_Awards/award_screen_5.jpg': 'https://www.everwinschool.com/images/Founder/Screen%205.jpg',
    'images/07_Awards/award_screen_6.jpg': 'https://www.everwinschool.com/images/Founder/Screen%206.jpg',
    'images/08_Facilities/smart_class_icon.png': 'https://www.everwinschool.com/images/smartcalss-icon.png',
    'images/08_Facilities/air_conditioning_icon.png': 'https://www.everwinschool.com/images/air-conditioning.png',
    'images/08_Facilities/sports_field_icon.png': 'https://www.everwinschool.com/images/soccer-field-.png',
    'images/08_Facilities/analysis_icon.png': 'https://www.everwinschool.com/images/analysis.png',
}

for rel, url in SOURCES.items():
    dest = BASE / rel
    dest.parent.mkdir(parents=True, exist_ok=True)
    try:
        req = Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urlopen(req, timeout=25) as response:
            data = response.read()
            ctype = response.headers.get("Content-Type", "")
        if not ctype.startswith("image/") or len(data) < 1000:
            print(f"SKIP (not a valid image response): {rel} [{ctype}]")
            continue
        dest.write_bytes(data)
        print(f"OK {rel} ({len(data):,} bytes)")
    except (HTTPError, URLError, TimeoutError, OSError) as e:
        print(f"FAILED {rel}: {e}")
print("\nFinished. Only successful, distinct downloads are saved in images/.")
