from flask import Flask , render_template, request
from random import choice, randrange
from stories import stories
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"
app.debug = True

debug = DebugToolbarExtension(app)


@app.route('/')
def home_page():    
    return render_template('select-story.html', stories=stories.values())


@app.route('/game')
def game_page():

    story_id = request.args["story_id"]
    story = stories[story_id]

    prompts = story.prompts

    return render_template('game.html', story_id=story_id, title=story.title, prompts=prompts)



@app.route('/madlib')
def show_madlib():
    
       
    story_id = request.args["story_id"]
    story = stories[story_id]

    madlib_story = story.generate(request.args)

    return render_template("madlib.html", title=story.title, text=madlib_story)



