from flask import (
    Flask,
    request,
    make_response,
    render_template_string,
    redirect,
    url_for,
)
import sqlite3
import os
import secrets
import hashlib

app = Flask(__name__)

#  [ИЗМЕНЕНО] Session Management:
# секретный ключ теперь берётся из переменной окружения или генерируется безопасно
app.secret_key = os.environ.get("SECRET_KEY", secrets.token_hex(32))

DB_PATH = os.environ.get("APP_DB_PATH", "app.db")


#  [ДОБАВЛЕНО] Security Headers Middleware
@app.after_request
def set_security_headers(response):
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["Content-Security-Policy"] = (
        "default-src 'self'; script-src 'self'; style-src 'self' 'unsafe-inline'"
    )
    response.headers["Strict-Transport-Security"] = (
        "max-age=31536000; includeSubDomains"
    )
    response.headers["Permissions-Policy"] = "geolocation=(), microphone=(), camera=()"
    return response


#  [ДОБАВЛЕНО] Password Hashing (SHA-256)
def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode("utf-8")).hexdigest()


def init_db():
    #  [ИЗМЕНЕНО] Пароли берутся из env и хранятся в хешированном виде
    admin_pw = os.environ.get("ADMIN_PASSWORD", "admin123")
    user_pw = os.environ.get("USER_PASSWORD", "user123")

    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            password TEXT,
            role TEXT
        )
        """
    )
    cur.execute("DELETE FROM users")
    cur.execute(
        "INSERT INTO users (username, password, role) VALUES (?, ?, ?)",
        ("admin", hash_password(admin_pw), "admin"),
    )
    cur.execute(
        "INSERT INTO users (username, password, role) VALUES (?, ?, ?)",
        ("user", hash_password(user_pw), "user"),
    )
    conn.commit()
    conn.close()


@app.route("/")
def index():
    html = """
    <h1>Vulnerable DAST Demo App</h1>
    <p>Пример уязвимого приложения для лабораторной по DAST.</p>
    <ul>
      <li><a href="/echo?msg=Hello">Reflected XSS / echo</a></li>
      <li><a href="/search?username=admin">SQL Injection / search</a></li>
      <li><a href="/login">Небезопасный логин</a></li>
      <li><a href="/profile">Профиль (зависит от cookie)</a></li>
      <li><a href="/admin">«Админка» без нормальной авторизации</a></li>
      <li><a href="/files/">Directory listing</a></li>
    </ul>
    """
    resp = make_response(html)

    #  [ИЗМЕНЕНО] Secure Cookies
    resp.set_cookie(
        "session",
        "guest-session-id",
        httponly=True,
        secure=True,
        samesite="Lax",
    )
    return resp


@app.route("/echo")
def echo():
    msg = request.args.get("msg", "")

    #  [ИЗМЕНЕНО] XSS Protection:
    # format() заменён на Jinja2 auto-escaping
    template = """
    <h2>Echo</h2>
    <p>Сообщение: {{ msg }}</p>
    <p>Попробуйте передать что-нибудь вроде: <code>&lt;script&gt;alert('XSS')&lt;/script&gt;</code></p>
    <a href="/">Назад</a>
    """
    return render_template_string(template, msg=msg)


@app.route("/search")
def search():
    username = request.args.get("username", "")
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    rows = []
    error = None
    try:
        #  [ИЗМЕНЕНО] SQL Injection Protection (parameterized query)
        cur.execute(
            "SELECT id, username, role FROM users WHERE username = ?", (username,)
        )
        rows = cur.fetchall()
    except Exception as e:
        error = str(e)

    conn.close()

    template = """
    <h2>Поиск пользователя</h2>
    <p>Запрос: <code>{{ query }}</code></p>
    {% if error %}
      <p style="color:red;">SQL error: {{ error }}</p>
    {% endif %}
    {% if rows %}
      <ul>
      {% for id, username, role in rows %}
        <li>{{ id }} – {{ username }} ({{ role }})</li>
      {% endfor %}
      </ul>
    {% else %}
      <p>Ничего не найдено</p>
    {% endif %}
    <a href="/">Назад</a>
    """
    shown_query = "SELECT id, username, role FROM users WHERE username = ?"
    return render_template_string(template, query=shown_query, rows=rows, error=error)


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        form = """
        <h2>Логин</h2>
        <form method="post">
          <label>Username: <input type="text" name="username"></label><br>
          <label>Password: <input type="password" name="password"></label><br>
          <button type="submit">Login</button>
        </form>
        <a href="/">Назад</a>
        """
        return render_template_string(form)

    username = request.form.get("username", "")
    password = request.form.get("password", "")

    #  [ИЗМЕНЕНО] Password Hashing при проверке
    password_hash = hash_password(password)

    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute(
        #  [ИЗМЕНЕНО] SQL Injection Protection
        "SELECT id, username, role FROM users WHERE username = ? AND password = ?",
        (username, password_hash),
    )
    row = cur.fetchone()
    conn.close()

    if row:
        _, uname, role = row
        session_token = secrets.token_hex(16)

        resp = make_response(
            f"<h2>Добро пожаловать, {uname} ({role})!</h2><a href='/'>На главную</a>"
        )

        #  [ИЗМЕНЕНО] Secure Cookies
        resp.set_cookie("user", uname, httponly=True, secure=True, samesite="Lax")
        resp.set_cookie("role", role, httponly=True, secure=True, samesite="Lax")
        resp.set_cookie(
            "session_token", session_token, httponly=True, secure=True, samesite="Lax"
        )
        return resp

    return render_template_string(
        "<h2>Неверные учетные данные</h2><a href='/login'>Попробовать снова</a>"
    )


@app.route("/profile")
def profile():
    username = request.cookies.get("user", "guest")
    role = request.cookies.get("role", "guest")

    template = """
    <h2>Профиль пользователя</h2>
    <p>Имя: {{ username }}</p>
    <p>Роль: {{ role }}</p>
    <a href="/">Назад</a>
    """
    return render_template_string(template, username=username, role=role)


@app.route("/admin")
def admin():
    role = request.cookies.get("role", "guest")
    if role != "admin":
        return "<h2>Доступ запрещён</h2>", 403

    return render_template_string("<h2>Admin panel</h2>")


@app.route("/files/")
@app.route("/files/<path:subpath>")
def files(subpath=""):
    base_dir = os.path.abspath(os.path.dirname(__file__))
    target_dir = os.path.abspath(os.path.join(base_dir, "files"))

    #  [ИЗМЕНЕНО] Directory Traversal Protection (whitelist)
    ALLOWED_FILES = []

    full_path = os.path.abspath(os.path.join(target_dir, subpath))

    #  path traversal check
    if not full_path.startswith(target_dir):
        return "<h2>Доступ запрещён</h2>", 403

    if not os.path.exists(full_path):
        return "<h2>Путь не найден</h2>", 404

    #  запрет directory listing
    if os.path.isdir(full_path):
        return "<h2>Доступ к директориям запрещён</h2>", 403

    #  whitelist enforcement
    if subpath not in ALLOWED_FILES:
        return "<h2>Доступ к этому файлу запрещён</h2>", 403

    with open(full_path, "r", encoding="utf-8", errors="ignore") as f:
        return f"<pre>{f.read()}</pre>"


if __name__ == "__main__":
    init_db()

    #  [ИЗМЕНЕНО] Debug Mode Control через env
    debug_mode = os.environ.get("FLASK_DEBUG", "False").lower() == "true"
    app.run(host="0.0.0.0", port=8080, debug=debug_mode)  # nosec
