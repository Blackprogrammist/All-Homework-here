from flask import Flask, render_template

app = Flask(__name__)
app.template_folder = 'templates'


@app.route('/')
def home():
    return render_template('home.html', title='Home Page', text='Welcome to the Home Page!')


@app.route('/about')
def about():
    return render_template('about.html', title='About Page', text='This is the About Page.')


@app.route('/anime/<anime>')
def anime(anime):
    main_characters = ['Naruto Uzumaki', 'Sasuke Uchiha', 'Sakura Haruno']
    genres = ['Action', 'Adventure', 'Fantasy']
    episodes = 500

    return render_template('anime.html', title='Anime Page',
                           anime=anime, main_characters=main_characters, genres=genres, episodes=episodes)


if __name__ == '__main__':
    app.run(debug=True)
