from __future__ import annotations
import sqlite3
from dataclasses import dataclass
from typing import List
from contextlib import contextmanager
from pathlib import Path
from config import DB_PATH, MONEY_TO_SEEDS_RATE, GOODS_TO_SEEDS_RATE, VOL_TO_SEEDS_RATE


@dataclass
class Donor:
    id: int
    name: str
    phone: str
    city: str

@dataclass
class Donation:
    id: int
    donor_id: int
    kind: str
    quantity: float
    ngo_id: int
    status: str



@dataclass

class NGO:

    id: int

    name: str

    phone: str

    address: str

    password: str

    website: str

    image: str



@contextmanager

def connect(db_path: Path = DB_PATH):

    con = sqlite3.connect(str(db_path))

    try:

        con.row_factory = sqlite3.Row

        yield con

        con.commit()

    finally:

        con.close()



def init_db() -> None:

    with connect() as con:

        cur = con.cursor()

        cur.execute("""CREATE TABLE IF NOT EXISTS donors (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            name TEXT NOT NULL,

            phone TEXT NOT NULL,

            city TEXT NOT NULL)""")


        cur.execute("""CREATE TABLE IF NOT EXISTS ngos (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            name TEXT NOT NULL,

            phone TEXT,

            address TEXT,

            password TEXT NOT NULL,

            website TEXT,

            image TEXT)""")



        cur.execute("""CREATE TABLE IF NOT EXISTS donations (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            donor_id INTEGER NOT NULL,

            kind TEXT NOT NULL CHECK(kind IN ('money','goods','volunteer')),

            quantity REAL NOT NULL,

            ngo_id INTEGER NOT NULL,

            status TEXT NOT NULL CHECK(status IN ('pending','approved')) DEFAULT 'pending',

            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

            FOREIGN KEY(donor_id) REFERENCES donors(id),

            FOREIG