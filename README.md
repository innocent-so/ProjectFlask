# ProjectFlask

A site diplaying some selected information from the open source data @ (https://sedac.ciesin.columbia.edu/ddc/baseline/index.html) 
this site takes each country in a continent and displays its population, population_density, land_mass, energy_consumptions as well as some other livestock information
for the specified year in the open source data. The purpose of this project is show surpossed agricultural farmer he's options if he intends moving to a new country to
setup a livestock farm, and how those livestocks have fair in those areas or which countries or continents suited for those livestocks

we first begin by installing flask
with pip install flask

other dependecies and packages to be installed include
1. pandas
using pip install pandas
2. openpyxl to load the data from the excel spreadsheet
using pip install openpyxl
3. xlrd for reading the xslx spreadsheet
using pip install xlrd

The Load_excel.py 

this pyscript is soley to load the excel file and store the data while counting the individual number of rolls per sheet
this is done by declaing two functions one that takes two parameters, (the sheet number, the collumn number)
we input the exact sheet number or sheetname and colummn number and it takes all the rolls in that exact colummn and saves it into and array


The database_setup.py

this pyscript sets up the database for this application.
the three databse tables (continents, countries and livestocks), and are linked together with foriegn keys.
the countries tables linked to the continents primary key and the livestock table connected to the countries primary key
the load-excel is imported and the functions are called to load the data from each colummn, placed into the desired arrays.
and then looped over and stored into the related tables in the database.
(a little error was encountered in loading the arrays and storing in the database. it returns index error(index out of range) for every other column except the country colummn
even tho printing out each array returns the exact value expected to be store) 
Although the database is then later saved properly in the database but still returns the index error.  
(hence the database is filled with ones so the application can run and render the templates)

Project.py

this pyscript basically runs the flask app.
it is connected to the databse and the data from the database is pushed to into the jinja templates and displayed ont he city.

the try and except blocks is used to handle exception incase what is requested from the database cannot be fetched it displays and error instead of the template to be rendered
if not the template is rendered with the information pulled from the database

