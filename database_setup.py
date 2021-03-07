import sqlite3
import pandas as pd
import load_excel


conn = sqlite3.connect('Project_data.db', detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
cur = conn.cursor()

# create tables
conn.execute('CREATE TABLE continent (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT)')
conn.execute('CREATE TABLE country( id INTEGER PRIMARY KEY AUTOINCREMENT, continent_id INTEGER, name TEXT, population INTEGER, '
             'population_density INTEGER, land_area INTEGER, energy_consumption INTEGER, FOREIGN KEY(continent_id) '
             'REFERENCES continent(id) )')
conn.execute('CREATE TABLE livestock( id INTEGER PRIMARY KEY AUTOINCREMENT, country_id INTEGER, cattle INTEGER, sheep INTEGER, '
             'goat INTEGER, pig INTEGER, eguines INTEGER, buffallo INTEGER, camel INTEGER, FOREIGN KEY(country_id) REFERENCES'
             ' country(id))')

file = pd.ExcelFile('Open-source-data.xls')
continents = file.sheet_names
for continent in continents:
    name = continent
    cur.execute('INSERT INTO continent VALUES(NULL, ?)', [name])
    conn.commit()

sheets = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for sheet in sheets:
    countries = load_excel.which_sheet(sheet, 1)
    populations = load_excel.which_sheet(sheet, 2)
    population_densities = load_excel.which_sheet(sheet, 3)
    land_areas = load_excel.which_sheet(sheet, 4)
    energy_consumptions = load_excel.which_sheet(sheet, 12)
    index = 0
    for country in countries:
        continent_id = sheet
        name = countries[index]
        population = 10
        population_density = 15
        land_area = 12
        energy_consumption = 91
        cur.execute('INSERT INTO country VALUES(NULL, ?, ?, ?, ?, ?, ?)', (continent_id, name, population, population_density, land_area, energy_consumption))
        conn.commit()
        index = index + 1
id_country = 0
index = 0
for sheet in sheets:
    cattles = load_excel.which_sheet(sheet, 5)
    sheeps = load_excel.which_sheet(sheet, 6)
    goats = load_excel.which_sheet(sheet, 7)
    pigs = load_excel.which_sheet(sheet, 8)
    eguiness = load_excel.which_sheet(sheet, 9)
    buffallos = load_excel.which_sheet(sheet, 10)
    camels = load_excel.which_sheet(sheet, 11)
    countries = load_excel.which_sheet(sheet, 1)
    for calf in cattles:
        id_country = id_country + 1
        country_id = id_country
        cattle = 12
        sheep = 16
        goat = 18
        pig = 11
        eguines = 19
        buffallo = 12
        camel = 15
        cur.execute('INSERT INTO livestock VALUES(NULL, ?, ?, ?, ?, ?, ?, ?, ?)', (country_id, cattle, sheep, goat, pig, eguines,
                                                                                   buffallo, camel))
        conn.commit()
        index = index + 1


conn.close()
