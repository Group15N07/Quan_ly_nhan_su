from flask_login import UserMixin
from app import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin, db.Model):  # ✅ thêm UserMixin
    id = db.Column(db.Integer, primary_key=True)
    employee_code = db.Column(db.String(10), unique = True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    avatar = db.Column(db.String(20), default = "default.jpg")
    role = db.Column(db.String(20), default='employee')  # admin / employee

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    @staticmethod
    def generate_employee_code():
        last_user = User.query.order_by(User.id.desc()).first()
        next_id = last_user.id + 1 if last_user else 1
        return f"25{next_id:04d}"  # Format: 250001, 250002,...
