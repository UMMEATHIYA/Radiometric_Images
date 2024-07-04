import sqlite3

# SQLite DB Name
DB_Name =  "solar_panel_sep01.db"

# SQLite DB Table Schema
TableSchema="""
drop table if exists mbox1;
create table mbox1 (
    id integer primary key autoincrement,
    avg integer,
    min integer,
    max integer,
    maxpos_x integer,
    maxpos_y integer,
    minpos_x integer,
    minpos_y integer,
    unit text,
    Timestamp DATETIME NOT NULL DEFAULT (strftime('%Y-%m-%d %H:%M:%S', 'NOW'))
);

drop table if exists mbox2;
create table mbox2 (
    id integer primary key autoincrement,
    avg integer,
    min integer,
    max integer,
    maxpos_x integer,
    maxpos_y integer,
    minpos_x integer,
    minpos_y integer,
    unit text,
    Timestamp DATETIME NOT NULL DEFAULT (strftime('%Y-%m-%d %H:%M:%S', 'NOW'))
);

drop table if exists mbox3;
create table mbox3 (
    id integer primary key autoincrement,
    avg integer,
    min integer,
    max integer,
    maxpos_x integer,
    maxpos_y integer,
    minpos_x integer,
    minpos_y integer,
    unit text,
    Timestamp DATETIME NOT NULL DEFAULT (strftime('%Y-%m-%d %H:%M:%S', 'NOW'))
);

drop table if exists mbox4;
create table mbox4 (
    id integer primary key autoincrement,
    avg integer,
    min integer,
    max integer,
    maxpos_x integer,
    maxpos_y integer,
    minpos_x integer,
    minpos_y integer,
    unit text,
    Timestamp DATETIME NOT NULL DEFAULT (strftime('%Y-%m-%d %H:%M:%S', 'NOW'))
);

drop table if exists solar_sensor;
create table solar_sensor (
    id integer primary key autoincrement,
    bv float,
    sv float,
    i float,
    lv float,
    p float,
    Timestamp DATETIME NOT NULL DEFAULT (strftime('%Y-%m-%d %H:%M:%S', 'NOW'))
);

drop table if exists temp_sensor;
create table temp_sensor (
    id integer primary key autoincrement,
    sensor float,
    name text,
    unit text,
    Timestamp DATETIME NOT NULL DEFAULT (strftime('%Y-%m-%d %H:%M:%S', 'NOW'))
);
"""

#Connect or Create DB File
conn = sqlite3.connect(DB_Name)
curs = conn.cursor()

#Create Tables
sqlite3.complete_statement(TableSchema)
curs.executescript(TableSchema)

#Close DB
curs.close()
conn.close()