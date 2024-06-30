from flask import Flask 

@app.route('/weather')
def weather():
    page = '''
    <form action="/grab">
        站名 <input name="location">
    </from>
    '''
    return page
@app.route('/grab')
def grab():
    location = flask.request.args.get('location')
    paage = f'''got location {loction}'''
    return page

app.run()