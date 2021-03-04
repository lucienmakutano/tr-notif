from flask import (
    request,
    render_template,
    url_for,
    flash,
    redirect
)
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from app.notif import send_notif
from config.settings import PHONE_NUMBER
from app.form import NotifyForm, AddTeacherForm
from app.model import Teacher

app = create_app()
db = SQLAlchemy(app)

@app.route("/")
def home():
    return "Home"


@app.route("/notify", methods=["GET", "POST"])
def notify():
    form = NotifyForm()
    if request.method == "POST":
        if form.validate_on_submit():
            phone = Teacher.query.get(form.code.data).phone_number
            _ = form.msg.data
            # _ = send_notif(body, PHONE_NUMBER, "+254713125823")
            print(phone)
            flash("The notification has been sent", "success")
        return redirect(url_for('notify'))
    
    return render_template("notify.html", form=form)


@app.route("/add-tr", methods=["GET", "POST"])
def add_tr():
    form = AddTeacherForm()
    if request.method == "POST":
        if form.validate_on_submit():
            c = form.code.data
            pn = form.phone.data
            tr = AddTeacherForm(code=c, phone_number=pn)
            db.session.add(tr)
            db.session.commit()
            flash("A new teacher has been added to the system", "success")
        return redirect(url_for('notify'))
    return render_template("add-tr.html", form=form)


@app.route("/update-tr")
def update_tr():
    pass


@app.route("/remove-tr")
def remove_tr():
    pass


if __name__ == "__main__":
    app.run(debug=True)
