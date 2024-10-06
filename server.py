from flask import Flask, session, redirect, request, url_for, render_template, jsonify
from main_db_controll import db
import os

UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def index():
    return render_template('main.html')

def answer():
    file = request.files['file']
    if file and allowed_file(file.filename):
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
    form_data = tuple(request.form.values()) + (file.filename,)
    print(form_data)
    db.add_data(form_data)
    data = db.get_data()
    print(data)
    return render_template('answer.html', obj=data)

# Новый маршрут для удаления данных
def delete_row():
    row_id = request.form.get('row_id')  # Предположим, что передается ID строки
    if row_id:
        db.delete_data(row_id)
        return jsonify({'status': 'success'})
    else:
        return jsonify({'status': 'error', 'message': 'Row ID is missing'})
    

# Маршрут для удаления данных
def delete_row():
    row_id = request.form.get('row_id')  # Получаем ID строки для удаления
    if row_id:
        try:
            db.delete_data(row_id)  # Вызов метода для удаления данных
            return jsonify({'status': 'success'})  # Возвращаем успешный ответ
        except Exception as e:
            return jsonify({'status': 'error', 'message': str(e)})
    else:
        return jsonify({'status': 'error', 'message': 'Row ID is missing'})

    
app = Flask(__name__)
app.add_url_rule('/', 'index', index, methods=["GET"])
app.add_url_rule('/answer', 'answer', answer, methods=["POST"])
app.add_url_rule('/delete', 'delete_row', delete_row, methods=["POST"])  # Новый маршрут
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if __name__ == '__main__':
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    app.run(debug=True)