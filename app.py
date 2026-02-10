from flask import Flask, render_template, send_from_directory, request, redirect, url_for
import os

app = Flask(__name__)

FILES_DIR = "files"

@app.route("/", methods=["GET", "POST"])
def age_check():
    if request.method == "POST":
        return redirect("/epstein/doj-disclosures/data-set-2-files")
    return render_template("age.html")

@app.route("/epstein/doj-disclosures/data-set-2-files")
def files_page():
    files = sorted(os.listdir(FILES_DIR))
    return render_template("index.html", files=files)

@app.route("/download/<filename>")
def download(filename):
    return send_from_directory(FILES_DIR, filename)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)