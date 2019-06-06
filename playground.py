from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play')
def static_box():
    return render_template('playground.html', num_times=3)

@app.route('/play/<num>')
def box(num):
    return render_template('playground.html', num_times=int(num))

@app.route('/play/<num>/<color>')
def box_color(num, color):
    return render_template('playground.html', num_times=int(num), color=(color))

if __name__ =="__main__":
    app.run(debug=True)