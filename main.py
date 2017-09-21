from flask import Flask, request
from caesar import *

app = Flask(__name__)

form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
      <form method="POST" action="/caesar">
      <label for="rot">
      Rotate By:
      <input type="text" name="rot" style="width:30px;"/ value="0">
      <br />
      <br />
      <textarea name="text">
      </textarea>
      <br />
      <br />
      <input type="submit" value="Submit Query"/>
    </body>
</html>
    """


@app.route("/")
def index():
    return form

@app.route("/caesar", methods=["POST"])
def caesar():
    rot = int(request.form["rot"])
    text = request.form["text"]
    ret = encrypt_caesar(text, rot)
    
    
    return """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
      <form method="POST" action="/caesar">
      <label for="rot">
      Rotate By:
      <input type="text" name="rot" style="width:30px;"/ value="{0}">
      <br />
      <br />
      <textarea name="text">{1}
      </textarea>
      <br />
      <br />
      <input type="submit" value="Submit Query"/>
    </body>
</html>
    """.format(rot,ret)


app.run(debug=True)
