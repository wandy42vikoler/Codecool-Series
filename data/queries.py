from data import data_manager
from psycopg2._psycopg import AsIs


def get_shows():
    return data_manager.execute_select('SELECT id, title FROM shows;')


def most_rated(pagination):
    return data_manager.execute_select(
        '''SELECT DISTINCT shows.id, title, year, runtime, shows.homepage, CAST(rating AS DECIMAL (9, 1)) AS rating, string_agg(genres.name, ',') AS genre, trailer
            FROM shows
            INNER JOIN show_genres ON show_genres.show_id = shows.id
            INNER JOIN genres ON genres.id = show_genres.genre_id
            GROUP BY shows.id
            ORDER BY rating DESC
            LIMIT 15
            OFFSET %(pagination)s;''', {'pagination': pagination})


def most_rated_sorted(pagination, order_by, desc):
    return data_manager.execute_select(
        '''SELECT DISTINCT shows.id, title, year, runtime, shows.homepage, CAST(rating AS DECIMAL (9, 1)) AS rating, string_agg(genres.name, ',') AS genre, trailer, shows.homepage
            FROM shows
            INNER JOIN show_genres ON show_genres.show_id = shows.id
            INNER JOIN genres ON genres.id = show_genres.genre_id
            GROUP BY shows.id
            ORDER BY %(order_by)s  %(desc)s
            LIMIT 15
            OFFSET %(pagination)s;''', {'pagination': pagination, 'order_by': AsIs(order_by), 'desc': AsIs(desc)})


def show(id):
    fetchall = False
    return data_manager.execute_select(
        '''SELECT DISTINCT shows.id, title, year, runtime, CAST(rating AS DECIMAL (9, 1)) AS rating, string_agg(DISTINCT genres.name, ',') AS genre, trailer, string_agg(DISTINCT actors.name, ',') AS actors, shows.overview
            FROM shows
            INNER JOIN show_genres ON show_genres.show_id = shows.id
            INNER JOIN genres ON genres.id = show_genres.genre_id
            INNER JOIN show_characters ON show_characters.show_id = shows.id
            INNER JOIN actors ON actors.id = show_characters.actor_id
            WHERE shows.id = %(id)s
            GROUP BY shows.id;''', {'id': id}, fetchall = False)


def shows():
    return data_manager.execute_select(
        '''SELECT id, title
            FROM shows
            WHERE rating > 9''')


def seasons_for_show(show_id):
    return data_manager.execute_select(
        '''SELECT seasons.title, string_agg(DISTINCT seasons.overview, ' ') AS overview, COUNT(episodes) AS episode_n
            FROM seasons
            INNER JOIN episodes ON episodes.season_id = seasons.id
            WHERE show_id = %(show_id)s
            GROUP BY seasons.title''', {'show_id': show_id})


def show_characters(show_id):
    return data_manager.execute_select('''
    SELECT show_characters.character_name, actors.name, actors.birthday
    FROM shows
    INNER JOIN show_characters ON show_characters.show_id = shows.id
    INNER JOIN actors ON actors.id = show_characters.actor_id
    WHERE shows.id = %(show_id)s''', {'show_id': show_id})


def trailer(show_id):
    return data_manager.execute_select('''
        SELECT trailer
        FROM shows
        WHERE shows.id = %(show_id)s
        ''', {'show_id': show_id})



