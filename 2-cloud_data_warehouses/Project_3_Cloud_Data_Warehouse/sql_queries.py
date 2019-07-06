import configparser


# CONFIG
config = configparser.ConfigParser()
config.read('dwh.cfg')

# DROP TABLES

staging_events_table_drop = "DROP TABLE IF EXISTS staging_events;"
staging_songs_table_drop = "DROP TABLE IF EXISTS staging_songs;"
songplay_table_drop = "DROP TABLE IF EXISTS songplays;"
user_table_drop = "DROP TABLE IF EXISTS users;"
song_table_drop = "DROP TABLE IF EXISTS songs;"
artist_table_drop = "DROP TABLE IF EXISTS artists;"
time_table_drop = "DROP TABLE IF EXISTS time;"

# CREATE TABLES

staging_events_table_create= ("""CREATE TABLE IF NOT EXISTS staging_events ( artist             varchar,
                                                                             auth               varchar,
                                                                             firstName          varchar,
                                                                             gender             varchar,
                                                                             itemInSession      int,
                                                                             lastName           varchar,
                                                                             length             numeric,
                                                                             level              varchar,
                                                                             location           varchar,
                                                                             menthod            varchar,
                                                                             page               varchar,
                                                                             registration       numeric,
                                                                             sessionId          int,         
                                                                             song               varchar,
                                                                             status             int,
                                                                             ts                 int,
                                                                             userAgent          varchar,
                                                                             userId             int           

                                                                            );
""")

staging_songs_table_create = ("""CREATE TABLE IF NOT EXISTS staging_songs (  num_songs          int,          
                                                                             artist_id          varchar,
                                                                             artist_latitude    numeric,
                                                                             artist_longitude   numeric,
                                                                             artist_location    varchar,
                                                                             artist_name        varchar,
                                                                             song_id            varchar,
                                                                             title              varchar,
                                                                             duration           numeric,
                                                                             year               int
                                                                            );
""")

songplay_table_create = ("""CREATE TABLE IF NOT EXISTS songplays ( songplay_id    int    PRIMARY KEY NOT NULL,
                                                                   start_time     timestamp,
                                                                   user_id        int                          NOT NULL,
                                                                   level          varchar,
                                                                   song_id        varchar,
                                                                   artist_id      varchar,
                                                                   session_id     int                          NOT NULL,
                                                                   location       varchar,
                                                                   user_agent     varchar 
                                                                  );

""")

user_table_create = ("""CREATE TABLE IF NOT EXISTS users (  user_id         varchar PRIMARY KEY NOT NULL, 
                                                            first_name      varchar, 
                                                            last_name       varchar, 
                                                            gender          varchar, 
                                                            level           varchar
                                                            );
""")

song_table_create = ("""CREATE TABLE IF NOT EXISTS songs (  song_id         varchar PRIMARY KEY NOT NULL, 
                                                            title           varchar, 
                                                            artist_id       varchar NOT NULL, 
                                                            year            int, 
                                                            duration        numeric
                                                        );
""")

artist_table_create = ("""CREATE TABLE IF NOT EXISTS artists (  artist_id   varchar   PRIMARY KEY NOT NULL, 
                                                                name        varchar, 
                                                                location    varchar, 
                                                                lattitude   numeric, 
                                                                longitude   numeric);
""")

time_table_create = ("""CREATE TABLE IF NOT EXISTS time (   start_time  timestamp    PRIMARY KEY NOT NULL, 
                                                            hour        int, 
                                                            day         int, 
                                                            week        int, 
                                                            month       int, 
                                                            year        int, 
                                                            weekday     int
                                                            );
""")

# STAGING TABLES

staging_events_copy = (""" copy staging_events from 's3://udacity-dend/log_data'
    credentials 'aws_iam_role={}'
    gzip delimiter ';' compupdate off region 'us-west-2';
""").format('ARN')

staging_songs_copy = ("""copy staging_songs from 's3://udacity-dend/song_data'
    credentials 'aws_iam_role={}'
    gzip delimiter ';' compupdate off region 'us-west-2';
""").format('ARN')

# FINAL TABLES

songplay_table_insert = ("""INSERT INTO songplays (songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent) 
select ts as start_time
       userId as user_id,
       level,
       song_id,
       artist_id,
       location,
       userAgent as user_agent
from staging_events e
join staging_songs  s on e.song = s.title

""")

user_table_insert = ("""INSERT INTO users (user_id, first_name, last_name, gender, level) 
select distinct userId as user_id,
                firstName as first_name,
                lastName as last_name,
                gender,
                level
from staging_evnets

""")

song_table_insert = ("""INSERT INTO songs (song_id, title, artist_id, year, duration) 
select song_id,
       title,
       artist_id,
       year,
       duration
from staging_songs
""")

artist_table_insert = ("""INSERT INTO artists (artist_id, name, location, lattitude, longitude) 
select artist_id,
       name,
       location,
       latitude,
       longitude
from staging_songs

""")

time_table_insert = ("""INSERT INTO time (start_time, hour, day, week, month, year, weekday) 
with temp as 
(select ts as start_time,
        TIMESTAMP 'epoch' + ts/1000 * interval '1 second' AS date
from staging_events)

select start_time,
       EXTRACT(hour FROM date) as hour,
       EXTRACT(day FROM date) as day,
       EXTRACT(week FROM date) as week,
       EXTRACT(month FROM date) as month,
       EXTRACT(year FROM date) as year,
       EXTRACT(weekday FROM date) as weekday
from staging_events  


""")

# QUERY LISTS

create_table_queries = [staging_events_table_create, staging_songs_table_create, songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [staging_events_table_drop, staging_songs_table_drop, songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
copy_table_queries = [staging_events_copy, staging_songs_copy]
insert_table_queries = [songplay_table_insert, user_table_insert, song_table_insert, artist_table_insert, time_table_insert]
