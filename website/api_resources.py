from flask import current_app as app, render_template,redirect, request, url_for, flash, jsonify
from website.model import db, Post, User, Comment
from flask_login import login_required, current_user
from flask_restful import Api, Resource,reqparse

api = Api()


# Request Parsers
post_parser = reqparse.RequestParser()
post_parser.add_argument('title', type=str, required=True, help='Title is required')
post_parser.add_argument('content', type=str, required=True, help='Content is required')
post_parser.add_argument('user_id', type=int, required=True, help='User ID is required')

comment_parser = reqparse.RequestParser()
comment_parser.add_argument('content', type=str, required=True, help='Content is required')
comment_parser.add_argument('user_id', type=int, required=True, help='User ID is required')
comment_parser.add_argument('post_id', type=int, required=True, help='Post ID is required')


# Flask-RESTful Resources
class AllPostsResource(Resource):
    def get(self):
        posts = Post.query.all()
        posts_data = [{
            'id': post.id,
            'title': post.title,
            'content': post.content,
            'author': post.author.username,
            'comments': [{
                'id': comment.id,
                'content': comment.content,
                'author': comment.author.username,
                'timestamp': comment.timestamp.isoformat()
            } for comment in post.comments]
        } for post in posts]
        return jsonify(posts_data)
    
    def post(self):
        args = post_parser.parse_args()
        user = User.query.get(args['user_id'])
        if not user:
            return {'message': 'User not found'}, 404

        post = Post(title=args['title'], content=args['content'], user_id=args['user_id'])
        db.session.add(post)
        db.session.commit()
        return {'message': 'Post created successfully', 'id': post.id}, 201

    
# Add Flask-RESTful resources
api.add_resource(AllPostsResource, '/api/posts')

class AllCommentsResource(Resource):
    def get(self):
        comments = Comment.query.all()
        comments_data = [{
            'id': comment.id,
            'content': comment.content,
            'author': comment.author.username,
            'post_id': comment.post_id,
            'timestamp': comment.timestamp.isoformat()
        } for comment in comments]
        return jsonify(comments_data)
    
    def post(self):
        args = comment_parser.parse_args()
        user = User.query.get(args['user_id'])
        post = Post.query.get(args['post_id'])
        if not user or not post:
            return {'message': 'User or Post not found'}, 404

        comment = Comment(content=args['content'], user_id=args['user_id'], post_id=args['post_id'])
        db.session.add(comment)
        db.session.commit()
        return {'message': 'Comment created successfully', 'id': comment.id}, 201

api.add_resource(AllCommentsResource, '/api/comments')