from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

books = [
    {'id': 1, 'title': 'Treasure Island', 'author': 'Robert Louis Stevenson', 'year': 1883},
    {'id': 2, 'title': 'Metro 2033', 'author': 'Dmitry Glukhovsky', 'year': 2005},
    {'id': 3, 'title': "World of Sophie's", 'author': 'Jostein Gaarder', 'year': 1991}
]


@app.route('/')
def home():
    return render_template('index.html', books=books)


@app.route('/book/<int:book_id>')
def book(book_id):
    book = [book for book in books if book['id'] == book_id][0]
    return render_template('book.html', book=book)


@app.route('/addbook', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        new_book = {
            'id': len(books) + 1,
            'title': request.form['title'],
            'author': request.form['author'],
            'year': request.form['year']
        }
        books.append(new_book)
        return redirect(url_for('home'))
    return render_template('addbook.html')


if __name__ == '__main__':
    app.run(debug=True)
