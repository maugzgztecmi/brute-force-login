from flask import Flask, request, render_template_string, redirect

app = Flask(__name__)

# Credenciales válidas (para prueba)
VALID_USERNAME = 'admin'
VALID_PASSWORD = 'password123'

HTML = """
<!doctype html>
<title>Login</title>
<h2>Login</h2>
<form method="post">
  Username: <input name="username"><br>
  Password: <input name="password" type="password"><br>
  <input type="submit" value="Login">
</form>
{% if error %}
<p style="color:red;">{{ error }}</p>
{% endif %}
"""

@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] == VALID_USERNAME and request.form['password'] == VALID_PASSWORD:
            return 'Login successful!'
        else:
            error = 'Invalid credentials.'
    return render_template_string(HTML, error=error)

if __name__ == '__main__':
    app.run(debug=True)
