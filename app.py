from flask import Flask, render_template, request, jsonify, redirect, url_for
from database import db, Todo

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todos.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route('/')
def index():
    with app.app_context():
        todos = Todo.query.order_by(Todo.id.desc()).all()
        print(f"Found {len(todos)} todos")  # 调试信息
        for todo in todos:
            print(f"Todo {todo.id}: {todo.title} - {todo.completed}")  # 调试信息
    return render_template('index.html', todos=todos)

@app.route('/add', methods=['POST'])
def add_todo():
    title = request.form.get('title')
    print(f"Adding todo: {title}")  # 调试信息
    if title:
        with app.app_context():
            todo = Todo(title=title, completed=False)
            db.session.add(todo)
            try:
                db.session.commit()
                print(f"Todo added successfully: {todo.id}")  # 调试信息
            except Exception as e:
                db.session.rollback()
                print(f"Error committing to database: {e}")  # 调试信息
                return "Error adding todo", 500
    return redirect(url_for('index'))

@app.route('/toggle/<int:todo_id>')
def toggle_todo(todo_id):
    with app.app_context():
        todo = Todo.query.get(todo_id)
        if todo:
            todo.completed = not todo.completed
            db.session.commit()
    return redirect(url_for('index'))

@app.route('/delete/<int:todo_id>')
def delete_todo(todo_id):
    with app.app_context():
        todo = Todo.query.get(todo_id)
        if todo:
            db.session.delete(todo)
            db.session.commit()
    return redirect(url_for('index'))

@app.route('/api/todos', methods=['GET'])
def get_todos():
    with app.app_context():
        todos = Todo.query.order_by(Todo.id.desc()).all()
    return jsonify([{
        'id': todo.id,
        'title': todo.title,
        'completed': todo.completed,
        'created_at': todo.created_at.isoformat()
    } for todo in todos])

@app.route('/api/todos', methods=['POST'])
def create_todo():
    data = request.get_json()
    title = data.get('title')
    if title:
        with app.app_context():
            todo = Todo(title=title, completed=False)
            db.session.add(todo)
            try:
                db.session.commit()
                return jsonify({
                    'id': todo.id,
                    'title': todo.title,
                    'completed': todo.completed,
                    'created_at': todo.created_at.isoformat()
                }), 201
            except Exception as e:
                db.session.rollback()
                print(f"Error creating todo: {e}")
                return jsonify({'error': 'Failed to create todo'}), 500
    return jsonify({'error': 'Title is required'}), 400

@app.route('/api/todos/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    with app.app_context():
        todo = Todo.query.get(todo_id)
        if not todo:
            return jsonify({'error': 'Todo not found'}), 404

        data = request.get_json()
        if 'completed' in data:
            todo.completed = data['completed']
            db.session.commit()
        return jsonify({
            'id': todo.id,
            'title': todo.title,
            'completed': todo.completed,
            'created_at': todo.created_at.isoformat()
        })

@app.route('/api/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo_api(todo_id):
    with app.app_context():
        todo = Todo.query.get(todo_id)
        if todo:
            db.session.delete(todo)
            db.session.commit()
            return jsonify({'success': True})
    return jsonify({'error': 'Todo not found'}), 404

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)