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

1. Extract data from S3 to two staging tables on Redshift, namely `staging_events` and `staging_songs`.
2. Transform and load data from staging tables to analytics tables on Redshift.


## Files included


1. `create_tables.py` create fact and dimension tables for the star schema in Redshift.
2. `etl.py` load data from S3 into staging tables on Redshift and then process that data into your analytics tables on Redshift.
3. `sql_queries.py` contains all sql queries, and is imported into the last two files above.
4. `dwh.cfg` contains AWS Redshift configuration infomation
5. `README.md`provides detailed description of the project.

Run `create_tables.py` create fact and dimension tables for the star schema in Redshift, then run `etl.py` to load data from S3 to staging tables on Redshift and load data from staging tables to analytics tables on Redshift.