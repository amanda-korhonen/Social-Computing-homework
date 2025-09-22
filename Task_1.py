# Task 1

import sqlite3

import pandas as pd

# import os
# os.system('clear')

DB_File = "database.sqlite"

# Excercise 1.1
#  opening the database
try: 
    con = sqlite3.connect(DB_File)
    print("SQLite Database connected")
except Exception as e:
    print(f"Failed to load the database '{e}'")

tablenames_df = pd.read_sql_query("SELECT name FROM sqlite_master WHERE type='table'", con)
print(tablenames_df)

for table in ['comments', 'follows', 'posts', 'reactions', 'users']:
    print(f'\n\ncontents of {table}')
    table = pd.read_sql_query(f"SELECT * FROM {table}", con)
    print(table)

# Exercise 1.2
try: 
    lurkers_df = pd.read_sql_query("""
    SELECT 
        COUNT(id) AS lurkers_count
    FROM users
    WHERE id NOT IN (SELECT user_id FROM comments)
        AND id NOT IN (SELECT user_id FROM posts)
        AND id NOT IN (SELECT user_id FROM reactions)
    """, con)
    print(lurkers_df)
except Exception as e:
    print(f"Error occurred: {e}")

# Exercise 1.3
try: 
    most_engaged_df = pd.read_sql_query("""
    SELECT 
        users.id AS user_id,
        users.username,
        COUNT(DISTINCT reactions.id) + COUNT(DISTINCT comments.id) AS total_engagement
    FROM users 
    JOIN
        posts
    ON
        users.id = posts.user_id
    LEFT JOIN 
        reactions
    ON
        posts.id = reactions.post_id              
    LEFT JOIN 
        comments
    ON 
        posts.id = comments.post_id     
    GROUP BY 
        users.id, users.username 
    ORDER BY
        total_engagement DESC
    LIMIT 5;
    """, con)
    print(f'\n\nTop 5 most influencal users')
    print(most_engaged_df)
except Exception as e:
    print(f"Error occurred: {e}")


