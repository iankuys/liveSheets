from flask import Flask, render_template, request, session
from flask_socketio import SocketIO, emit
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

NUM_ROWS = 5
NUM_COLS = 5

sheets = [["" for _ in range(NUM_COLS) ] for _ in range(NUM_ROWS)]

@app.route("/")
def main():
    return render_template("sheets.html", rows=NUM_ROWS, cols=NUM_COLS)

@socketio.on("changes")
def handle_changes(data):
    sheets_data = data.get("data", [])
    
    for cell in sheets_data:
        row = cell.get('row')
        col = cell.get('col')
        value = cell.get('value')
        sheets[row][col] = value

    content = { "data": sheets }
    emit("changes", json.dumps(content), broadcast=True, include_self=False)

@socketio.on("connect")
def connect(auth):
    print(f"someone joined sheets")
    
@socketio.on("disconnect")
def disconnect():
    print(f"someone left sheets")
    
if __name__ == "__main__":
    socketio.run(app, debug=True)