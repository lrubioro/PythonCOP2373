# Lory Rubio Programming Assignment 13
# This  program creates a database with 10 cities in florida stored in a table.
# The table also simulate population growth for the next 20 years at a 2% growth rate for each year.
# Using matplotlib, a function is created to show the population growth for a city. The user is shown the 10 cities as options and the asked to choose one and the population growth for the city is visually displayed.

# import sqlite3 to create the population_LR data base
import sqlite3

# import matplotlib.pyplot to show population growth
import matplotlib.pyplot as plt

# create the database
database_name = "population_LR.db"

def database_table():
    conn = sqlite3.connect(database_name)
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS population")
    c.execute('''CREATE TABLE population (
                       city TEXT,
                       year INTEGER,
                       population INTEGER
                   )''')
    conn.commit()
    conn.close()
    print('Your Database and Table has been created with requested city info.')

# fill database and table with chosen 2023 city stats
def insert_data():
    initial_populations = {
        "Sarasota": 57602,
        "Orlando": 307573,
        "Miami": 455924,
        "Jacksonville": 985843,
        "Fort Myers": 97372,
        "St. Petersburg": 263553,
        "Tallahassee": 202221,
        "Bradenton": 56289,
        "Cape Coral": 224455,
        "Clearwater": 116850
    }

    # code to instruct the filling
    conn = sqlite3.connect(database_name)
    c = conn.cursor()
    for city, pop in initial_populations.items():
        c.execute("INSERT INTO population (city, year, population) VALUES (?, ?, ?)",
                  (city, 2023, pop))
    conn.commit()
    conn.close()
    print('For the year 2023 the data has been recorded in population table')

# now create the code to simulate the %2 growth of each city and the functions according to the user
def simulate_population_growth():
    cities = [
        "Sarasota",
        "Orlando",
        "Miami",
        "Jacksonville",
        "Fort Myers",
        "St. Petersburg",
        "Tallahassee",
        "Bradenton",
        "Cape Coral",
        "Clearwater"
    ]

    # address teh exact database in which to fill into
    conn = sqlite3.connect(database_name)
    c = conn.cursor()

    for city in cities:
        c.execute("SELECT population FROM population WHERE city = ? AND year = 2023", (city,))
        result = c.fetchone()

        if result:
            pop = result[0]
            for year in range(2024, 2024 + 20):

                # the %2 increase math
                pop = int(pop * 1.02)

                # uodate table values with new growth in population
                c.execute("INSERT INTO population (city, year, population) VALUES (?, ?, ?)",
                          (city, year, pop))

    conn.commit()
    conn.close()
    print("The expected population from at a rate of %2 has been updated into the population table")

# now plot the results
def plot_population():
    cities = [
        "Sarasota",
        "Orlando",
        "Miami",
        "Jacksonville",
        "Fort Myers",
        "St. Petersburg",
        "Tallahassee",
        "Bradenton",
        "Cape Coral",
        "Clearwater"
    ]

    print("Please enter the city to view it's population growth (function format):")

    # assign the city choices after they have been listed to user into numerical values
    for idx, city in enumerate(cities, 1):
        print(f"{idx}. {city}")

    choice = int(input("Enter the number of your chosen city: "))
    selected_city = cities[choice - 1]

    conn = sqlite3.connect(database_name)
    c = conn.cursor()
    c.execute("SELECT year, population FROM population WHERE city = ? ORDER BY year", (selected_city,))
    data = c.fetchall()
    conn.close()

    years = [row[0] for row in data]
    populations = [row[1] for row in data]

    plt.plot(years, populations, marker='o')
    plt.title(" The Population Growth of your selected city")
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# Call back all functions
database_table()
insert_data()
simulate_population_growth()
plot_population()
