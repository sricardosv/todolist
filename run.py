from app import create_app, db
from app.models import User, Task

app = create_app()

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Task': Task}

@app.route('/debug/blueprints')
def debug_blueprints():
    return {name: str(bp) for name, bp in app.blueprints.items()}

if __name__ == '__main__':
    print("Registered Blueprints:", app.blueprints)
    app.run(debug=True)