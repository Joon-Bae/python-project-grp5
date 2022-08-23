from flask import Blueprint
from app.models import Comment, db, User
from flask_login import login_required, current_user



follows_route = Blueprint('follows', __name__)

@follows_route.post('/<int:id>')
@login_required
def follow_unfollow(id):
    user = User.query.get(id)
    if current_user not in user.followers:
        user.followers.append(current_user)
        db.session.commit()
        current_user.following.append(user)
        return {'current_user': current_user.to_dict()}
        # return {'message': f"{current_user.username} followed {user.username}" }
    else:
        user.followers.remove(current_user)
        db.session.commit()
        return {'current_user': current_user.to_dict()}
        # return {'message': f"{current_user.username} unfollowed {user.username}" }
