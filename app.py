from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/youtube')
def scrape_youtube():
    youtube_url = 'https://www.youtube.com/feed/trending'
    response = requests.get(youtube_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract video titles
    video_titles = [title.text for title in soup.select('h3')]

    return render_template('youtube.html', video_titles=video_titles)

@app.route('/amazon')
def scrape_amazon():
    amazon_url = 'https://www.amazon.com/best-sellers-electronics/zgbs/electronics/'
    response = requests.get(amazon_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract product titles
    product_titles = [title.text.strip() for title in soup.select('.p13n-sc-truncated')]

    return render_template('amazon.html', product_titles=product_titles)

if __name__ == '__main__':
    app.run(debug=True)
