@app.route('/api/get_user')
def api_get_user():
    tid = request.args.get('tid')
    if not tid:
        return jsonify({'ok': False, 'error': 'missing_tid'}), 400
    conn = get_db(); cur = conn.cursor()
    cur.execute('SELECT * FROM users WHERE telegram_id=?', (str(tid),))
    user = cur.fetchone()
    conn.close()
    if not user:
        return jsonify({'ok': False, 'error': 'not_found'}), 404
    return jsonify({'ok': True, 'coins': user['coins'], 'name': user['name']})