from flask import Flask, render_template_string, request
import random

app = Flask(__name__)

SIZE = 4

def new_grid():
    grid = [[0]*SIZE for _ in range(SIZE)]
    add_number(grid)
    add_number(grid)
    return grid

def add_number(grid):
    empty = [(i, j) for i in range(SIZE) for j in range(SIZE) if grid[i][j] == 0]
    if empty:
        i, j = random.choice(empty)
        grid[i][j] = random.choice([2, 4])

def move_left(grid):
    new = []
    for row in grid:
        row = [x for x in row if x != 0]
        for i in range(len(row)-1):
            if row[i] == row[i+1]:
                row[i] *= 2
                row[i+1] = 0
        row = [x for x in row if x != 0]
        row += [0]*(SIZE-len(row))
        new.append(row)
    return new

def rotate(grid):
    return [list(row) for row in zip(*grid[::-1])]

def move(grid, direction):
    for _ in range(direction):
        grid = rotate(grid)
    grid = move_left(grid)
    for _ in range((4-direction)%4):
        grid = rotate(grid)
    add_number(grid)
    return grid

grid = new_grid()

HTML = """
<!DOCTYPE html>
<html>
<head>
<title>2048 Game</title>
<style>
table { margin: auto; }
td {
  width: 60px; height: 60px;
  text-align: center;
  font-size: 24px;
  border: 1px solid #ccc;
}
button { margin: 10px; padding: 10px; }
</style>
</head>
<body>
<h2 align="center">2048 Game (Python + Flask)</h2>
<table>
{% for row in grid %}
<tr>
{% for cell in row %}
<td>{{ cell if cell != 0 else '' }}</td>
{% endfor %}
</tr>
{% endfor %}
</table>

<form method="post" align="center">
<button name="move" value="0">⬅ Left</button>
<button name="move" value="1">⬆ Up</button>
<button name="move" value="2">➡ Right</button>
<button name="move" value="3">⬇ Down</button>
</form>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def game():
    global grid
    if request.method == "POST":
        grid = move(grid, int(request.form["move"]))
    return render_template_string(HTML, grid=grid)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)