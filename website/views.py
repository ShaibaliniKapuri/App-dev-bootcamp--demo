from flask import current_app as app, render_template,redirect, request, url_for, flash
from website.model import db, Post, User
from flask_login import login_required, current_user

@app.route("/")
def home():
    posts = Post.query.all()
    return render_template('start.html', posts=posts)


@app.route('/create', methods=['GET', 'POST'])
@login_required
def create_post():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        post = Post(title=title, content=content, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Post created successfully!', 'success')
        return redirect(url_for('home'))
    return render_template('create.html')