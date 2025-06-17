# app/models/gameboard.py

from app.models.user import User
from app import db

def calculate_score(user):
    # Tính điểm theo KPI ví dụ
    score = 0
    score += user.attendance_score or 0
    score += user.kpi_score or 0
    score += user.deadline_score or 0
    return score

def ranking_demo():
    users = User.query.all()
    ranked = sorted(users, key=lambda u: calculate_score(u), reverse=True)
    return ranked
