from flask import Blueprint, render_template
from flask_login import current_user, login_required
from app.models.user import User
from app.models.gameboard import calculate_score, get_ranking
from app.decorators.role_required import role_required

gameboard_bp = Blueprint('gameboard', __name__)

@gameboard_bp.route('/gameboard/<int:user_id>')
@login_required
@role_required('admin', 'employee', 'manager')
def gameboard(user_id):
    user = User.query.get(user_id)
    score = calculate_score(user_id)
    ranking = get_ranking()

    for r in ranking:
        if r["name"] == user.username:
            r["me"] = True

    # Chọn layout dựa theo role của người dùng hiện tại
    role = current_user.role  # giả sử User có thuộc tính role
    layout_path = f"{role}/layout"

    return render_template(
        'gamebroad/gamebroad.html',
        user=user,
        score=score,
        ranking=ranking,
        layout=layout_path  # Truyền layout động
    )

 