# Film Geek Website

## Description
Hello, my name is Mohammad Erfan Ranjbarkohan.  
For my final project in the CS50 course, I created a website called **Film Geek**, designed to help users find movies that match their preferences.

The idea comes from a common situation: wanting to watch a movie but not knowing which one.  
The website provides an easy way to search for movies based on:

- Genre
- Director’s name
- Actor’s name
- Production time range
- Minimum IMDb rating

All filters are optional. After submitting the form, a list of matching movies is displayed, each showing:

- A thumbnail image
- The movie’s name
- A link to more details

Clicking on a movie brings up full details including director, cast, genre, and rating.

## Development Process
Initially, I faced limitations accessing IMDb’s full database due to cost and complexity.  
As a solution, I gathered data from IMDb’s **Top 250 Movies** list using a Python script and stored it in a **SQLite** database.

This project helped me improve in:

- Database design and queries
- API usage
- Web development using Flask (Python)
- HTML and CSS frontend design

## Project Structure

- **static/**: Contains CSS files and images.
- **templates/**: Includes HTML templates like `layout.html`, `index.html`, `results.html`, and `details.html`.
- **app.py**: Backend Flask application handling routes and logic.
- **create_sql.py**: Script to build and populate the database.
- **movies.db**: SQLite database with movie details.

## Challenges and Future Plans
One major challenge was designing the search functionality to allow multiple optional filters efficiently.  
I also learned to structure the project modularly to improve development and maintenance.

In the future, I plan to expand Film Geek by:

- Adding personalized movie recommendations
- Implementing user reviews
- Creating user-specific watchlists

---

**Film Geek** represents the skills I gained during CS50 and is a real-world demonstration of my interest in programming, databases, and web development.
