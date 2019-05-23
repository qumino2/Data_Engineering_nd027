## Purpose & Analytical goals

The purpose of this database is to leverage the data Sparkify has been collecting (which records users' activities on the streaming app) for analytics team to analyse users' behavior and preference. The database will provide the team an easy way to query their data.

## Schema design 

We design a star schema which consists one fact table and four dimension tables, namely songplays, users, songs, artists, time. 

`songplays` table

primary key: songplay_id

`users` table

primary key: user_id

`songs` table

primary key: song_id

`artists` table

primary key: artist_id

`time` table

primary key: timestamp

We choose a star schema becasue it is the simplest style of data mart schema which consists one or more fact tables referencing any number of dimensions tables. In our case, we can center fact table songplay in the center referencing other dimension tables. 

## ETL process & Pipeline

We build ETL process by processing one data file in each dataset. Firstly, we process `song_data` by reading the original JSON files into Pandas DataFrame. Then we extract data and insert records into `songs` table and `artists` table. Secondly, we process `log_data` to extract data for `time` table, `users` table, `songplays` table.  The `songplays` is a little bit more complicated than others since need to query `songs` and `artists` to get the song ID and artist ID. 

After the ETL process has been successfully built, we build the pipeline to extract, transform, load the entire datasets.

## Files included

1. `test.ipynb` is used to check if the records are successfully inserted.
2. `create_tables.py` is used to reset the tables in database
3. `etl.ypynb` reads and processes a single file from `song_data` and `log_data` and loads the data into tables.
4. `etl.py` reads and processes all files from `song_data` and `log_data` and loads them into tables.
5. `sql_queries.py` contains all sql queries, and is imported into the last three files above.
6. `data` folder contains `song_data` and `log_data`
7. `README.md`provides detailed description of the project.

Run `create_tables.py` to reset all the tables in database, then run `etl.py` to excute the ETL pipeline to process data. Finally, run `test.ipynb` to confirm if records are correctly inserted into each table.