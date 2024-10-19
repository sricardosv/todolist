from flask import render_template, redirect, url_for, request
from flask_login import current_user, login_required
from app import db
from app.main import bp
from app.models import Task


@bp.route('/')
@bp.route('/index')
@login_required
def index():
    print("index main")
    print(current_user)
    tasks = Task.query.filter_by(user_id=current_user.id).all()
    return render_template('index.html', tasks=tasks, user=current_user)

@bp.route('/add', methods=['POST'])
@login_required
def add_task():
    title = request.form.get('title')
    if title:
        new_task = Task(title=title, completed=False, user_id=current_user.id)
        db.session.add(new_task)
        db.session.commit()
    return redirect(url_for('main.index'))

@bp.route('/complete/<int:task_id>', methods=['POST'])
@login_required
def complete_task(task_id):
    task = Task.query.get(task_id)
    if task and task.user_id == current_user.id:
        task.completed = True
        db.session.commit()
    return redirect(url_for('main.index'))

@bp.route('/uncomplete/<int:task_id>', methods=['POST'])
@login_required
def uncomplete_task(task_id):
    task = Task.query.get(task_id)
    if task and task.user_id == current_user.id:
        task.completed = False
        db.session.commit()
    return redirect(url_for('main.index'))