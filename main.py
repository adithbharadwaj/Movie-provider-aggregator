from flask import Flask, redirect, url_for, request, render_template
import requests

app = Flask(__name__)

'''
---------------------------------------------------------------------------------------------
routing to Display the Pages
'''
# initial page. the page that is open when we start the server in localhost:5000
@app.route('/')
def main():
    return render_template('search.html')


'''
---------------------------------------------------------------------------------------------
Actual API implementations
'''
@app.route('/search_movie', methods=['POST', 'GET'])
def search():
    if request.method == 'POST':
        movie = request.form['search_movie']
        url = '''https://api.themoviedb.org/3/search/movie?api_key=00e967be34501054c5adb40c77221a4c&language=en-US' 
              '&query={}&page=1&include_adult=false'''.format(
            movie)
        data = requests.get(url).json()['results']
        res = []
        for key in data:
            res.append([key['title'], key['overview'], key['id']])
        return render_template('search.html', result=res)

'''
---------------------------------------------------------------------------------------------
Driver function
'''

if __name__ == '__main__':
    app.secret_key = 'super secret key'

    app.debug = True  # debug is used for developing since it allows us to make changes in the python file without
    # having to restart the server again and again.
    app.run()
