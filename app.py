from flask import Flask, render_template
app = Flask(__name__, template_folder="template")

@app.route('/')
def hello():
  return render_template('index4.html')
if __name__ == "__main__":
   app.run(debug=True)
