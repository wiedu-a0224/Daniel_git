from flask import Flask, request
import we

app = Flask('metaveyBOT')
w = we.WeaG()

@app.route('/weather')
def weather():
    location = request.args.get('location')
    r = ''
    if location:
        result = w.grab(location)
        r = w.tostr(result).replace(' ', '<br>')

    page = '''
    <form>
        站名 <input name="location" value="永和">
        
    </form>
    '''
    return page + r

@app.route('/grab')
def grab():
    location = request.args.get('location')
    r = ''
    if location:
        result = w.grab(location)
        r = w.tostr(result).replace(' ', '<br>')
    
    return r

if __name__ == "__main__":
    app.run()
