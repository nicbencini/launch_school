from flask import Flask, render_template, g, redirect, url_for, request
import re
from pathlib import Path

# Base directory of this script
BASE_DIR = Path(__file__).parent.resolve()
# Data directory relative to base
DATA_DIR = BASE_DIR / "book_viewer" / "data"

app = Flask(__name__)

@app.before_request
def load_contents():
    toc_path = DATA_DIR / "toc.txt"
    # Read lines including newline characters
    g.contents = toc_path.read_text().splitlines(keepends=True)

@app.route("/")
def index():
    return render_template('home.html', contents=g.contents)

@app.route("/chapters/<page_num>")
def chapter(page_num):
    if page_num.isdigit() and 1 <= int(page_num) <= len(g.contents):
        # Build chapter title
        chapter_title = f"Chapter {page_num} - {g.contents[int(page_num)-1].strip()}"
        # Path to chapter file
        chapter_path = DATA_DIR / f"chp{page_num}.txt"
        chapter = chapter_path.read_text()
       
        return render_template('chapter.html',
                               chapter_title=chapter_title,
                               contents=g.contents,
                               chapter=chapter)
    else:
        return redirect(url_for('index'))

@app.errorhandler(404)
def page_not_found(error):
    return redirect(url_for('index'))

@app.route("/search")
def search():
    query = request.args.get('query', '')
    results = chapters_matching(query) if query else []
    return render_template('search.html', query=query, results=results)

# Jinja2 filter to wrap paragraphs
def paragrify(text):
    # Escape backslashes inside regex string
    return f'<p>{re.sub(r"(\n\n)", "</p>\n\n<p>", text).strip()}</p>'


def chapters_matching(query):
    if not query:
        return []

    results = []
    for index, name in enumerate(g.contents, start=1):
        with open(f"{DATA_DIR}/chp{index}.txt", "r") as file:
            chapter_content = file.read()
        if query.lower() in chapter_content.lower():
            results.append({'number': index, 'name': name})

    return results


app.jinja_env.filters['paragrify'] = paragrify

if __name__ == "__main__":
    app.run(debug=True, port=5003)
