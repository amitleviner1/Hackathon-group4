from __future__ import annotations
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
ASSETS_DIR = BASE_DIR / "assets"
DB_PATH = BASE_DIR / "donations.sqlite3"

SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 720
CAPTION = "Donation Tree"
FONT_PATH = str(ASSETS_DIR / "font.otf")
BG_IMAGE = ASSETS_DIR / "Background1.jpg"
PLAY_RECT = ASSETS_DIR / "Play Rect.png"
OPTIONS_RECT = ASSETS_DIR / "Options Rect.png"
QUIT_RECT = ASSETS_DIR / "Quit Rect.png"

MONEY_TO_SEEDS_RATE = 10
GOODS_TO_SEEDS_RATE = 1
VOL_TO_SEEDS_RATE = 1
