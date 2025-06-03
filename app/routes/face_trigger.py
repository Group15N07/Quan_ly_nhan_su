import subprocess
from flask import Blueprint, redirect, url_for, flash
from flask_login import login_required, current_user
from datetime import datetime
from app.models.attendance import Attendance
from app import db

face_trigger_bp = Blueprint('face_trigger', __name__)

@face_trigger_bp.route('/chamcong/face')
@login_required
def chamcong_face():
    username = current_user.username
    user_id = current_user.id

    try:
        # Gọi subprocess để chạy nhận diện khuôn mặt
        result = subprocess.run(
            ['python', 'face_module/run.py', username],
            check=False  # Không raise lỗi nếu exit code != 0
        )

        now = datetime.now().replace(microsecond=0)
        today = now.date()

        # Nếu nhận diện thành công (exit code == 0)
        if result.returncode == 0:
            record = Attendance.query.filter_by(user_id=user_id, date=today).first()

            if not record:
                # ✅ Trường hợp chưa có chấm công hôm nay → check-in
                new_record = Attendance(
                    user_id=user_id,
                    date=today,
                    check_in=now
                )
                db.session.add(new_record)
                db.session.commit()
                flash("✅ Check-in thành công!")

            elif not record.check_out:
                # ✅ Đã check-in, giờ thêm check-out + tính giờ
                record.check_out = now
                if record.check_in:
                    duration = record.check_out - record.check_in
                    record.total_hours = round(duration.total_seconds() / 3600, 2)
                db.session.commit()
                flash("✅ Check-out thành công!")

            else:
                # ✅ Đã chấm công đủ 2 lần trong ngày
                flash("✅ Đã chấm công đầy đủ hôm nay.")

        else:
            flash("❌ Nhận diện thất bại. Không ghi chấm công.")

    except Exception as e:
        flash("⚠️ Lỗi khi gọi AI nhận diện: " + str(e))

    return redirect(url_for('attendance.bang_cham_cong_ngay'))