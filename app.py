from flask import Flask, request, render_template

from extractor import get_upnextchain

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route("/", methods=["GET", "POST"])
def run_page():
    if request.method == "POST":
        videolink = None
        try:
            videolink = str(request.form["videolink"])
        except:
            errors += "<p>{!r} is not a string.</p>\n".format(request.form["videolink"])
        if videolink is not None:
            videoId = videolink.split("=")[1]
            results = get_upnextchain(videoId)
            if len(results) == 0:
                failmessage="Could not get related videos"
                return'''
                <html><body>
                <p>{failmessage}</p>
                </body></html>
                '''.format(failmessage=failmessage)
            return '''
            <html><body>
            <p>The id is {videoId}</p>
            <p>The next videos are {results}</p>
            <iframe width="540" height="360" src="https://www.youtube.com/embed/{videoId}" frameborder="0"></iframe>
            </body></html>
            '''.format(videoId=videoId,results=results)
    return render_template("main_page.html")