from flask import Flask, jsonify, render_template_string

app = Flask(__name__)

STUDENTS = [
    {"id": 1, "name": "Aarav Sharma", "course": "Computer Science"},
    {"id": 2, "name": "Meera Reddy", "course": "Information Technology"},
    {"id": 3, "name": "Ishaan Patel", "course": "Data Science"},
]

PAGE = """
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Student Management</title>
  <style>
    body { font-family: Arial, sans-serif; max-width: 850px; margin: 40px auto; padding: 0 18px; color: #172033; background: #f5f7fb; }
    h1 { margin-bottom: 6px; }
    .subtitle { color: #5b6475; margin-bottom: 24px; }
    .panel { background: white; border-radius: 12px; padding: 22px; box-shadow: 0 4px 18px #17203312; }
    table { width: 100%; border-collapse: collapse; }
    th, td { text-align: left; padding: 12px; border-bottom: 1px solid #e6eaf0; }
    th { background: #eef3ff; }
    .status { margin-top: 18px; color: #167044; font-weight: bold; }
    a { color: #2459c4; }
  </style>
</head>
<body>
  <h1>Student Management Portal</h1>
  <p class="subtitle">CI/CD demo powered by Flask, Jenkins, Docker and Kubernetes</p>
  <section class="panel">
    <h2>Student Records</h2>
    <table>
      <thead><tr><th>ID</th><th>Name</th><th>Course</th></tr></thead>
      <tbody>
      {% for student in students %}
        <tr><td>{{ student.id }}</td><td>{{ student.name }}</td><td>{{ student.course }}</td></tr>
      {% endfor %}
      </tbody>
    </table>
    <p class="status">Application is running successfully.</p>
    <p>Health check: <a href="/health">/health</a> · API: <a href="/api/students">/api/students</a></p>
  </section>
</body>
</html>
"""

@app.get("/")
def home():
    return render_template_string(PAGE, students=STUDENTS)

@app.get("/health")
def health():
    return jsonify(status="healthy"), 200

@app.get("/api/students")
def students():
    return jsonify(STUDENTS), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
