from flask import Flask, render_template, g, redirect
import re

app = Flask(__name__)

@app.before_request
def load_contents():
    with open("book_viewer/data/toc.txt", "r") as file:
        g.contents = file.readlines()

@app.route("/")
def index():
    return render_template('home.html', contents=g.contents)


@app.route("/chapters/<page_num>")
def chapter(page_num):
    if page_num.isdigit() and (1 <= int(page_num) <= len(g.contents)):
        chapter_title = f"Chapter {page_num} - {g.contents[int(page_num)-1]}"

        with open(f"book_viewer/data/chp{page_num}.txt", "r") as file:
            chapter = file.read()

        return render_template('chapter.html',
                            chapter_title=chapter_title,
                            contents=g.contents,
                            chapter=chapter)
    else:
        return redirect("/")

@app.errorhandler(404)
def page_not_found(error):
    return redirect("/")

# Define the filter
def paragrify(text):
    return f'<p>{re.sub(r"(\n\n)", '</p>\n\n<p>', text).strip()}</p>'

# Register the filter with the app
app.jinja_env.filters['paragrify'] = paragrify

if __name__ == "__main__":
    app.run(debug=True, port=5003)