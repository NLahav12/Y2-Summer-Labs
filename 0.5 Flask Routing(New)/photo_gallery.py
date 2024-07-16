from flask import Flask

app = Flask(__name__)

welcome_str = '''
Welcome to Nadav's food, pets and outer space photo gallery
'''

@app.route('/home')
def home():
    return f'''
    <html> 
    <head>Photo gallery</head>
    <body>
    <h1>Photo Gallery</h1>
    <p>{welcome_str}</p>
    <a href='/food1'>go to the first food photo</a>
    <br>
    <br>
    <a href='/food3'>go to the third food photo</a>
    <br>
    <br>

    <a href='/pet2'>go to the second pet photo</a>
    <br>
    <br>

    <a href='/outer_space1'>go to the first outer space photo</a>
    <br>
    <br>
    </body>
    </html>'''

@app.route('/food1')
def food1():
    return ''' 
    <html>
    <body>
    <img src="https://heygrillhey.com/wp-content/uploads/2018/05/Smoked-Hamburgers-683x1024.png"
    width="400">
    <br>
    <a href='/food2'>go to the second food photo</a>
    <br>
    <a href='/home'>go back to the home page</a>
    </body>
    </html>
    '''

@app.route('/food2')
def food2():
    return ''' 
    <html>
    <body>
    <img src="https://www.cookingclassy.com/wp-content/uploads/2022/07/grilled-steak-15-600x900.jpg"
    width="400">
    <br>
    <a href='/food1'>go to the first food photo</a>
    <br>
    <a href='/food3'>go to the third food photo</a>
    </body>
    </html>
    '''

@app.route('/food3')
def food3():
    return ''' 
    <html>
    <body>
    <img src="https://www.allrecipes.com/thmb/0xH8n2D4cC97t7mcC7eT2SDZ0aE=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/6776_Pizza-Dough_ddmfs_2x1_1725-fdaa76496da045b3bdaadcec6d4c5398.jpg"
    width="400">
    <br>
    <a href='/home'>go back to the home page</a>
    <br>
    <a href='/food2'>go to the second food photo</a>
    </body>
    </html>
    '''

@app.route('/pet1')
def pet1():
    return ''' 
    <html>
    <body>
    <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSsfPVX8SiUyr3RrqjHs7G1yzeKSYY03D73Jaf5gHD4PnsfpUR-SkzMPIvrvwIVRzxuQks&usqp=CAU"
    width="400">
    <br>
    <a href='/pet2'>go to the second pet photo</a>
    </body>
    </html>
    '''

@app.route('/pet2')
def pet2():
    return ''' 
    <html>
    <body>
    <img src="https://media.4-paws.org/7/b/8/4/7b84da50b67c8c39b9deb0d6581efa3309960ed6/VIER%20PFOTEN_2019-12-13_209-2001x2000-600x600.jpg"
    width="400">
    <br>
    <a href='/pet1'>go to the first pet photo</a>
    <br>
    <a href='/pet3'>go to the third pet photo</a>
    <br>
    <a href='/home'>go back to the home page</a>
    </body>
    </html>
    '''

@app.route('/pet3')
def pet3():
    return ''' 
    <html>
    <body>
    <img src="https://i.natgeofe.com/n/e3ae5fbf-ddc9-4b18-8c75-81d2daf962c1/3948225.jpg"
    width="400">
    <br>
    <a href='/pet2'>go to the second pet photo</a>
    </body>
    </html>
    '''

@app.route('/outer_space1')
def outer_space1():
    return ''' 
    <html>
    <body>
    <img src="https://images.photowall.com/products/56987/outer-space-4.jpg?h=699&q=85"
    width="400">
    <br>
    <a href='/outer_space2'>go to the second outer space photo</a>
    <br>
    <a href='/outer_space3'>go to the third outer space photo</a>
    <br>
    <a href='/home'>go back to the home page</a>
    <br>
    </body>
    </html>
    '''

@app.route('/outer_space2')
def outer_space2():
    return ''' 
    <html>
    <body>
    <img src="https://t4.ftcdn.net/jpg/06/20/08/47/360_F_620084766_fGRU1NqbRmNxiqw5EfY9oq1weKIo3FNH.jpg"
    width="400">
    <br>
    <a href='/outer_space1'>go to the first outer space photo</a>
    <br>
    <a href='/outer_space3'>go to the third outer space photo</a>
    <br>
    </body>
    </html>
    '''

@app.route('/outer_space3')
def outer_space3():
    return ''' 
    <html>
    <body>
    <img src="https://encyclopedia.pub/media/common/202210/mceclip11-6358acb3b8cf3.png"
    width="400">
    <br>
    <a href='/outer_space1'>go to the first outer space photo</a>
    <br>
    <a href='/outer_space2'>go to the second outer space photo</a>
    <br>
    </body>
    </html>
    '''

    
if __name__ == '__main__':
    app.run(debug=True)