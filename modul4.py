from flask import Flask, render_template
app = Flask(__name__)
@app.route('/ferdi')
def gethobi():
 hobi1= 'Bermain game'
 hobi2= 'bermain bola'
 hobi3= 'membaca'
 return render_template('ferdi.html', hobi1 = {{hobi1}} , hobi2 = {{hobi2}} , hobi3 = {{hobi3}})
if __name__ == '__main__':
 app.run(debug=True)