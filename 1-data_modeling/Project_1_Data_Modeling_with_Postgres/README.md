## Purpose & Analytical goals

The purpose of this database is to leverage the data Sparkify has been collecting (which records users' activities on the streaming app) for analytics team to analyse users' behavior and preference. The database will provide the team an easy way to query their data.

## Schema design 

We design a star schema which consists one fact table and four dimension tables, namely songplays, users, songs, artists, time. 

We choose a star schema becasue it is the simplest style of data mart schema which consists one or more fact tables referencing any number of dimensions tables. In our case, we can center fact table songplay in the center referencing other dimension tables. 

## ETL process & Pipeline

We build ETL process by processing one data file in each dataset. Firstly, we process `song_data` by reading the original JSON files into Pandas DataFrame. Then we extract data and insert records into `songs` table and `artists` table. Secondly, we process `log_data` to extract data for `time` table, `users` table, `songplays` table.  The `songplays` is a little bit more complicated than others since need to query `songs` and `artists` to get the song ID and artist ID. 

After the ETL process has been successfully built, we build the pipeline to extract, transform, load the entire datasets.