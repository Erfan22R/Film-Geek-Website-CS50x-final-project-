import sqlite3
import requests

# تابع ساخت جدول
def create_table(conn):
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS movies (
                        Title TEXT,
                        Year TEXT,
                        Rated TEXT,
                        Released TEXT,
                        Runtime TEXT,
                        Genre TEXT,
                        Director TEXT,
                        Writer TEXT,
                        Actors TEXT,
                        Plot TEXT,
                        Language TEXT,
                        Country TEXT,
                        Awards TEXT,
                        Poster TEXT,
                        Ratings TEXT,
                        Metascore TEXT,
                        imdbRating TEXT,
                        imdbVotes TEXT,
                        imdbID TEXT PRIMARY KEY,
                        Type TEXT,
                        BoxOffice TEXT,
                        Production TEXT,
                        Website TEXT)''')
    conn.commit()

# اتصال به دیتابیس
conn = sqlite3.connect("movies.db")
create_table(conn)
cursor = conn.cursor()

# تنظیم API Key
API_KEY = "fe269a27"

# خواندن لیست فیلم‌ها
with open("top_250_movies.txt", "r", encoding="utf-8") as file:
    movie_names = [line.strip() for line in file]

# دریافت اطلاعات فیلم‌ها و ذخیره
for movie in movie_names:
    params = {"t": movie, "apikey": API_KEY}
    response = requests.get("http://www.omdbapi.com/", params=params)
    data = response.json()

    if data["Response"] == "True":
        cursor.execute('''
            INSERT OR IGNORE INTO movies (
                Title, Year, Rated, Released, Runtime, Genre, Director, Writer,
                Actors, Plot, Language, Country, Awards, Poster, Ratings,
                Metascore, imdbRating, imdbVotes, imdbID, Type, BoxOffice,
                Production, Website)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            data.get("Title"),
            data.get("Year"),
            data.get("Rated"),
            data.get("Released"),
            data.get("Runtime"),
            data.get("Genre"),
            data.get("Director"),
            data.get("Writer"),
            data.get("Actors"),
            data.get("Plot"),
            data.get("Language"),
            data.get("Country"),
            data.get("Awards"),
            data.get("Poster"),
            str(data.get("Ratings")),  # تبدیل Ratings به رشته
            data.get("Metascore"),
            data.get("imdbRating"),
            data.get("imdbVotes"),
            data.get("imdbID"),
            data.get("Type"),
            data.get("BoxOffice"),
            data.get("Production"),
            data.get("Website")
        ))
        print(f"{data['Title']} ذخیره شد.")
    else:
        print(f"اطلاعات {movie} یافت نشد.")

# ذخیره تغییرات و بستن اتصال
conn.commit()
conn.close()
print("همه اطلاعات ذخیره شد!")
