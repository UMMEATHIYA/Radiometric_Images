import sqlite3

connection = sqlite3.connect("solar_panel.db")
cursor = connection.cursor()


cursor.execute("create table solar_panel ( spot text, temperature float, rawvalue integer, xcoordinate integer, ycoordinate integer )")

result_list = [
    ("spot1", 23.4, 1992, 100, 110),
    ("spot1", 22.7, 1822, 101, 111),
    ("spot1", 24.0, 1888, 102, 112),
    ("spot1", 25.1, 1733, 103, 114),
    ("spot2", 22.4, 1934, 104, 115),
    ("spot2", 23.1, 1870, 105, 116),
    ("spot2", 22.9, 1823, 106, 117),
    ("spot2", 22.4, 1873, 107, 118),
    ("spot3", 26.4, 1778, 108, 119),
    ("spot3", 25.9, 1765, 109, 120),
    ("spot3", 26.1, 1568, 110, 121),
    ("spot3", 25.5, 1453, 111, 122),
    ("spot4", 27.4, 1442, 112, 123),
    ("spot4", 26.8, 1562, 113, 124),
    ("spot4", 27.6, 1686, 114, 125),
    ("spot4", 28.1, 1403, 115, 126)
]

cursor.executemany("insert into solar_panel values (?,?,?,?,?)", result_list)


#print database rows
for row in cursor.execute("select * from solar_panel"):
    print(row)

connection.commit()
connection.close()