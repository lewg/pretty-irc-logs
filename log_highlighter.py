from flask import Flask, url_for, render_template, Markup
import httplib
import re
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter

app = Flask(__name__)
app.config.from_pyfile('application.cfg')

base_url = app.config['BASE_URL']
base_path = app.config['BASE_PATH']
channels = app.config['CHANNELS']

@app.route('/')
def index():
    title = "%s" % base_url
    page_title = "Log Highlighter"
    body = Markup("<p>Use the top menu to select a channel.</p>")
    return render_template('bootstrap.html', page_title=page_title, lead=title, title=title, channels=channels, body=body)


@app.route('/<channel>')
def show_channel(channel):
    output = ""

    log_path = "/%s/%s/" % (base_path, channel)
    irc_host = httplib.HTTPConnection(base_url)
    irc_host.request("GET", log_path)
    resp = irc_host.getresponse()
    log_index = resp.read()

    file_finder = re.compile(r'<a href="([a-z0-9]+-[\d]{4}-[\d]{2}-[\d]{2})"')
    for match in file_finder.finditer(log_index):
        output += "<a href=\"%s\">%s</a><br />" % (url_for('show_log', channel=channel, log_file=match.group(1)), match.group(1))

    irc_host.close()

    page_title = "#%s" % channel
    title = "Channel: %s" % channel
    body = Markup(output)
    return render_template('bootstrap.html', page_title=page_title, title=title, channels=channels, body=body)


@app.route('/<channel>/<log_file>')
def show_log(channel, log_file):
    log_path = "/%s/%s/%s" % (base_path, channel, log_file)
    irc_host = httplib.HTTPConnection(base_url)
    irc_host.request("GET", log_path)
    resp = irc_host.getresponse()
    log_body = resp.read()
    irc_host.close()

    body = Markup(highlight(log_body, get_lexer_by_name('irc'), HtmlFormatter()))
    title = "Channel: %s" % channel
    page_title = "#%s" % channel
    lead = "Log: %s" % log_file
    return render_template('bootstrap.html', title=title, page_title=page_title, lead=lead, channel=channel, channels=channels, body=body)


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
