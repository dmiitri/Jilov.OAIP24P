from flask import Flask, render_template

app = Flask(__name__)

movies = [
    {
        "id": 1,
        "title": "Интерстеллар",
        "year": 2014,
        "rating": 8.7,
        "genre": "Фантастика",
        "description": "Команда исследователей отправляется сквозь червоточину в поисках нового дома для человечества"
    },
    {
        "id": 2,
        "title": "Матрица",
        "year": 1999,
        "rating": 8.5,
        "genre": "Фантастика, боевик",
        "description": "Хакер Нео узнаёт, что окружающий мир — иллюзия, созданная машинами"
    },
    {
        "id": 3,
        "title": "Шрек",
        "year": 2001,
        "rating": 8.1,
        "genre": "Анимация, комедия",
        "description": "Огр Шрек отправляется спасать принцессу Фиону, чтобы вернуть себе болото"
    },
    {
        "id": 4,
        "title": "Начало",
        "year": 2010,
        "rating": 8.8,
        "genre": "Фантастика, триллер",
        "description": "Вор, умеющий проникать в сны, получает задание внедрить идею в сознание человека"
    },
    {
        "id": 5,
        "title": "Побег из Шоушенка",
        "year": 1994,
        "rating": 9.3,
        "genre": "Драма",
        "description": "Банкир Энди Дюфрейн приговорён к пожизненному заключению и мечтает о свободе"
    }
]

@app.route("/")
def index():
    return render_template("index.html", movies=movies)

@app.route("/movie/<int:movie_id>")
def movie(movie_id):
    for movie in movies:
        if movie["id"] == movie_id:
            return render_template("movie.html", movie=movie)

    return "Фильм не найден", 404

if __name__ == "__main__":
    app.run(debug=True)