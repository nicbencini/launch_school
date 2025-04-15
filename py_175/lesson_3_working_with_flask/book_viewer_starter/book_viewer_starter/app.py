from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    with open("book_viewer/data/toc.txt", "r") as file:
        contents = file.readlines()
        return render_template('home.html', contents=contents)


@app.route("/chapters/<page_num>")
def chapter(page_num):

    
    with open("book_viewer/data/toc.txt", "r") as file:
        contents = file.readlines()

    chapter_title = f"Chapter {page_num} - {contents[int(page_num)-1]}"

    with open(f"book_viewer/data/chp{page_num}.txt", "r") as file:
        chapter = file.read()

    return render_template('chapter.html',
                           chapter_title=chapter_title,
                           contents=contents,
                           chapter=chapter)



if __name__ == "__main__":
    app.run(debug=True, port=5003)