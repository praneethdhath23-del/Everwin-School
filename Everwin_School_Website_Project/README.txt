EVERWIN SCHOOL WEBSITE PROJECT

PROJECT STRUCTURE

Everwin_School_Website_Project/
  index.html                    Main updated website
  images/                       Local image assets
    01_Kolathur_CBSE/            Kolathur gallery photos
    02_Mathur/                   Mathur campus photos
    03_Janakipuram/              Janakipuram inauguration photo
    04_Surapet/                  Surapet campus photos
    05_Management/               Founder, CEO and principal portraits
    06_Brand/                     Official school logos
    07_Awards/                    Awards and recognition photos
    08_Facilities/                Facility icons
    09_Sembium/                   Sembium building photo
    10_General/                   Honest branch photo placeholders
  scripts/
    download_images.py           Downloads available official image sources
  IMAGE_SOURCES.txt              Image URL manifest
  README.txt                     This guide

SETUP
1. Extract the ZIP.
2. Open the extracted folder in File Explorer.
3. Open Command Prompt in this folder.
4. Run: python scripts\download_images.py
5. When downloads finish, open index.html in Chrome.

IMPORTANT
- The HTML now uses local relative paths in images/, so keep index.html and images/ together.
- The downloader fetches image files from the official Everwin website when reachable. Some URLs may fail if the school has moved or removed an image.
- Maduravoyal, Perambur, Kolathur Matric and Paruthipattu have clearly marked original SVG placeholders where a confirmed campus photo URL was not available. These are not school photographs and are not repeated logos.
- Some images are from other Everwin campuses and are labelled as such; do not misrepresent them as another branch.
- Get permission from the school before public redistribution or commercial use of photographs.
