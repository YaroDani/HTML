from flask import Flask, render_template

app = Flask(__name__)

@app.route('/games-events', methods=['POST', 'GET'])
def games ():
    start = None
    error = None
    if request.method == 'POST':
        action = request.form.get('action')
        if action == 'start':
            start = True
        if action == 'create':
            name_event=request.form.get('name_event')
            info=request.form.get('info')
            start_date=request.form.get('start_date')
            end_date = request.form.get('end_date')
            event = [name_event, info, start_date, end_date]
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute('SELECT id FROM users WHERE email=?', (session['email'], ))
            user = cursor.fetchone()
            if not user:
                conn.close()
                return redirect(url_for('login'))
            else:
                user_id = user[0]

            if name_event and start_date and end_date:
                conn = get_db_connection()
                cursor = conn.cursor()

                cursor.execute("INSERT INTO events (name_events, info, start_date, end_date, user_id) VALUES (?, ?, ?, ?, ?)",
                               (name_event, info, start_date, end_date, user_id))
                conn.commit()
                conn.close()

    return render_template('games_events.html', start=start, error=error)

'''
@app.route('/about-me/<name>/<age>')
def about(name, age):
    return name + " " + age + " y. o."


app.run(debug=True)
