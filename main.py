# Import Statement
import pandas as pd

# Creates a database with our monsters and some of their stats
database = pd.DataFrame(
    {
        "Monster": [
            "Goblin",
            "Goblin Mage",
            "Wolf",
            "Dude",
            "Orc"
        ],
        "Attack": [
            3,
            3,
            5,
            4,
            5
        ],
        "Health": [
            25,
            25,
            30,
            35,
            40
        ]
    }
)

# Note: Series is one column of data

# This prints out the entire database
print(database)

# Prints out only the monster names
print(database["Monster"])

# Manually creates a standalone series
attack_series = pd.Series([3, 3, 5, 4, 5], name="Attack")

# prints out the series
print(attack_series)

# Prints out the highest value of attack in the database
print(database["Attack"].max())

# Prints out the highest value of attack in the series
print(attack_series.max())

# Breaks down the statistical information in the database
print(database.describe())
