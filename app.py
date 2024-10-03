from flask import Flask, render_template, session, redirect, url_for, g, request
from database import get_db, close_db
from flask_session import Session
from werkzeug.security import generate_password_hash, check_password_hash
from forms import RegistrationForm, LoginForm, CreateTimetableForm
from functools import wraps

app = Flask(__name__)
app.teardown_appcontext(close_db)
app.config["SECRET_KEY"] = "this-is-my-secret-key"
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.before_request
def logged_in_user():
    g.user = session.get("user_id", None)

def login_required(view):
    @wraps(view)
    def wrapped_view(*args, **kwargs):
        if g.user is None:
            return redirect(url_for("login", next=request.url))
        return view(*args, **kwargs)
    return wrapped_view


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user_id = form.user_id.data
        password = form.password.data
        password2 = form.password2.data
        db = get_db()
        possible_clashing_user = db.execute("""SELECT * FROM users 
                                    WHERE user_id = ?; """, (user_id,)).fetchone()
        if possible_clashing_user is not None:
            form.user_id.errors.append("User is already taken")
        else:
            db.execute("""INSERT INTO users (user_id, password) 
                            VALUES (?, ?);""", (user_id, generate_password_hash(password)))
            db.commit()
            return redirect ( url_for("login"))
    return render_template("register.html", form=form)
    

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user_id = form.user_id.data
        password = form.password.data
        db = get_db()
        possible_clashing_user = db.execute("""SELECT * FROM users
                                            WHERE user_id = ?;""", (user_id,)).fetchone()
        if possible_clashing_user is None:
            form.user_id.errors.append("No such user")
        elif not check_password_hash(possible_clashing_user["password"], password):
            form.password.errors.append("Incorrect password")
        else:
            session.clear()
            session["user_id"] = user_id
            next_page = request.args.get("next")
            if not next_page:
                next_page = url_for("index")
            return redirect(url_for ("timetable"))
    return render_template("login.html", form=form)
    

@app.route("/logout")
def logout():
    session.clear()
    return redirect( url_for("index") )


@app.route("/timetable", methods=["GET", "POST"])
@login_required
def timetable():
    users = get_db().execute("SELECT user_id FROM users WHERE user_id = ?", (session["user_id"],)).fetchall()
    if request.method == "POST":
        if "create_timetable" in request.form:
            return redirect(url_for("create_timetable"))
        elif "show_timetable" in request.form:
            return redirect(url_for("show_timetable"))
    return render_template("timetable.html", users=users)


@app.route('/timetable/create_timetable', methods=['GET', 'POST'])
def create_timetable():
    form = CreateTimetableForm()
    if form.validate_on_submit():
        return redirect(url_for('created_timetable'))
    else:
        return render_template('create_timetable.html', form=form)

@app.route('/timetable/created_timetable', methods=['GET', 'POST'])
def created_timetable():
    form = CreateTimetableForm()
    if form.validate_on_submit():
        selected_courses = form.course.data
        db = get_db()
        try:
            listToStr = ','.join([str("?") for e in selected_courses]) 
            courses = db.execute(f"""SELECT * FROM timetable 
                        WHERE course IN ({listToStr}) ORDER BY course;""", tuple(selected_courses)).fetchall()
            return render_template("created_timetable.html", selected_courses=courses)
        except:
            return "There was an error...." 
    else:
        return render_template('created_timetable.html', form=form)
    
@app.route('/timetable/show_timetable', methods=['GET', 'POST'])
def show_timetable():
    users = get_db().execute("SELECT user_id FROM users WHERE user_id = ?", (session["user_id"],)).fetchall()
    db = get_db()
    user_timetable = db.execute("""SELECT * FROM timetable WHERE id=?;""", (session["user_id"])).fetchone()
    back = url_for('timetable')

    return render_template("show_timetable.html", users=users)

