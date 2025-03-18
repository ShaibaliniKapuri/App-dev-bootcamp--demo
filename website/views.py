from flask import current_app as app, render_template,redirect, request, url_for, flash
from website.model import db, Post, User, Comment
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


# Edit Post Route (General User)
@app.route('/edit/<int:post_id>', methods=['GET', 'POST'])
@login_required
def edit_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user and  not current_user.is_admin():
        flash('You do not have permission to edit this post.', 'error')
        return redirect(url_for('home'))

    if request.method == 'POST':
        post.title = request.form.get('title')
        post.content = request.form.get('content')
        db.session.commit()
        flash('Post updated successfully!', 'success')
        return redirect(url_for('home'))

    return render_template('edit_post.html', post=post)


# Delete Post Route (General User and Admin)
@app.route('/delete/<int:post_id>', methods=['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user and  not current_user.is_admin():
        flash('You do not have permission to delete this post.', 'error')
        return redirect(url_for('home'))

    db.session.delete(post)
    db.session.commit()
    flash('Post deleted successfully!', 'success')
    return redirect(url_for('home'))


# Add Comment Route
@app.route('/add_comment/<int:post_id>', methods=['POST'])
@login_required
def add_comment(post_id):
    post = Post.query.get_or_404(post_id)
    content = request.form.get('content')
    if content:
        comment = Comment(content=content, user_id=current_user.id, post_id=post.id)
        db.session.add(comment)
        db.session.commit()
        flash('Comment added successfully!', 'success')
    return redirect(url_for('home'))

# Edit Comment Route
@app.route('/edit_comment/<int:comment_id>', methods=['GET', 'POST'])
@login_required
def edit_comment(comment_id):
    comment = Comment.query.get_or_404(comment_id)
    if comment.author != current_user and not current_user.is_admin():
        flash('You do not have permission to edit this comment.', 'error')
        return redirect(url_for('home'))

    if request.method == 'POST':
        comment.content = request.form.get('content')
        db.session.commit()
        flash('Comment updated successfully!', 'success')
        return redirect(url_for('home'))

    return render_template('edit_comment.html', comment=comment)

# Delete Comment Route
@app.route('/delete_comment/<int:comment_id>', methods=['POST'])
@login_required
def delete_comment(comment_id):
    comment = Comment.query.get_or_404(comment_id)
    if comment.author != current_user and not current_user.is_admin():
        flash('You do not have permission to delete this comment.', 'error')
        return redirect(url_for('home'))

    db.session.delete(comment)
    db.session.commit()
    flash('Comment deleted successfully!', 'success')
    return redirect(url_for('home'))

# Admin Dashboard Route
@app.route('/admin/dashboard')
@login_required
def admin_dashboard():
    if not current_user.is_admin():
        flash('You do not have permission to access this page.', 'error')
        return redirect(url_for('home'))

    # App statistics
    total_users = User.query.count()
    total_posts = Post.query.count()
    total_comments = Comment.query.count()

    users = User.query.all()
    posts = Post.query.all()
    comments = Comment.query.all()

    # Prepare data for Chart.js
    user_data = {
        'labels': [user.username for user in users],
        'posts': [len(user.posts) for user in users],
        'comments': [len(user.comments) for user in users],
    }

    return render_template('admin_dashboard.html', total_users=total_users, total_posts=total_posts, total_comments=total_comments, user_data=user_data)
    



# Search Route
@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query', '').strip()
    if query:
        # Search posts by title or content
        posts = Post.query.filter(
            (Post.title.contains(query)) | (Post.content.contains(query))
        ).all()
        # Search users by username
        users = User.query.filter(User.username.contains(query)).all()
    else:
        posts = []
        users = []
    return render_template('search.html', query=query, posts=posts, users=users)