from flask import Flask, render_template, url_for, request
from data import queries
import math
from dotenv import load_dotenv
from data.util import json_response

load_dotenv()
app = Flask('codecool_series')

@app.route('/')
def index():
    shows = queries.get_shows()
    return render_template('index.html', shows=shows)


@app.route('/design')
def design():
    return render_template('design.html')


@app.route('/shows/most-rated')
@app.route('/shows/most-rated/<pagination>')
def most_rated(pagination=0):
    args = request.args
    by = args.get('order_by')
    order = args.get('desc')
    if by:
        most_rated_shows = queries.most_rated_sorted(pagination, by, order)
        return render_template('rated.html', shows=most_rated_shows, pagination=int(pagination), by=by, order=order)
    else:
        most_rated_shows = queries.most_rated(pagination)
        return render_template('rated.html', shows=most_rated_shows, pagination=int(pagination))


@app.route('/show/<id>')
def show(id):
    '''title, average runtime length, rating, genres (in the same way as in the shows list),
    overview, and the name of the top three actors appearing in the show.'''
    show_ind = id
    show = queries.show(show_ind)
    print(show)
    return render_template('show.html', id=id, show=show)


@app.route('/shows')
def shows():
    shows = queries.shows()
    return render_template('shows.html', shows=shows)


@app.route('/shows/<show_id>/')
@json_response
def season(show_id):
    return queries.seasons_for_show(show_id)



@app.route('/tv-show/<show_id>')
def detail_show(show_id):
    characters = queries.show_characters(show_id)
    return render_template('show_detail.html', characters=characters, id=show_id)



@app.route('/trailer/<show_id>')
@json_response
def trailer(show_id):
    return queries.trailer(show_id)

def main():
    app.run(debug=False)


if __name__ == '__main__':
    main()
