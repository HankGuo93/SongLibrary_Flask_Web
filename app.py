from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/songlibrary")
def songlibrary():
    df = pd.read_csv ('./static/SongLibrary.csv')
    df_html = df.to_html()
    return render_template('songlibrary.html', **locals())

@app.route("/getsongsbysinger")
def getsongsbysinger():
    df = pd.read_csv ('./static/SongLibrary.csv')
    singer = request.args.get('singer')
    filter = df['Singer'] == singer
    results = df[filter]
    return results.to_html()

@app.route("/getsongbysongname")
def getsongbysongname():
    df = pd.read_csv ('./static/SongLibrary.csv')
    name = request.args.get('name')
    filter = df['SongName'] == name
    results = df[filter]
    return results.to_html()

@app.route("/submitBySinger", methods=['POST'])
def submitBySinger():
    Singer = request.values['Singer']
    ResultHeader = 'Hello, Here is Your Search Result!! ＼（＾∀＾）メ（＾∀＾）ノ'
    df = pd.read_csv ('./static/SongLibrary.csv')
    filter = df['Singer'] == Singer
    results = df[filter].to_html()
    return render_template('home.html',**locals())

@app.route("/submitBySong", methods=['POST'])
def submitBySong():
    Song = request.values['Song']
    ResultHeader = 'Hello, Here is Your Search Result!! ＼（＾∀＾）メ（＾∀＾）ノ'
    df = pd.read_csv ('./static/SongLibrary.csv')
    filter = df['SongName'] == Song
    results = df[filter].to_html()
    return render_template('home.html',**locals())

if __name__ == "__main__":
    app.run()