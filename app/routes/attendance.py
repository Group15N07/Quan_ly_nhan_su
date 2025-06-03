from flask import Blueprint, render_template
from app.models.attendance import Attendance
from datetime import date
from app.models.user import User
from app.utils.render_with_role_layout import render_with_role
attendance_bp = Blueprint('attendance', __name__)

@attendance_bp.route('/chamcong')
def bang_cham_cong_ngay():
    today = date.today()
    recs = Attendance.query.filter_by(date=today).all()
    records = [{
        'id': r.id,
        'name': r.user.username,
        'date': r.date.strftime('%Y-%m-%d'),
        'check_in': r.check_in.strftime('%H:%M:%S') if r.check_in else '',
        'check_out': r.check_out.strftime('%H:%M:%S') if r.check_out else '',
        'total_hours': r.total_hours or ''
    } for r in recs]
    return render_with_role('attendance/bang_cham_cong_ngay.html', records=records)

@attendance_bp.route('/chamcong/tongket')
def tongket_cham_cong_thang():
    from calendar import monthrange
    from datetime import datetime

    # Nhận tháng/năm từ form GET
    month = int(request.args.get('month', datetime.now().month))
    year = int(request.args.get('year', datetime.now().year))
    total_days = monthrange(year, month)[1]

    summaries = []
    for u in User.query.all():
        recs = Attendance.query.filter_by(user_id=u.id).filter(
            Attendance.date.between(date(year, month, 1), date(year, month, total_days))
        ).all()
        days_worked = len([r for r in recs if r.check_in])
        total_hours = sum([r.total_hours or 0 for r in recs])
        summaries.append({
            'name': u.username,
            'days_worked': days_worked,
            'total_hours': total_hours,
            'days_absent': total_days - days_worked
        })

    return render_template(
        'attendance/bang_cham_cong_thang_tong_ket.html',
        summaries=summaries,
        month=month,
        year=year
    )

    return render_template('attendance/bang_cham_cong_thang_tong_ket.html',
                           summaries=summaries, month=month, year=year)
@attendance_bp.route('/chamcong/tongket/export')
def export_excel():
    import pandas as pd
    from io import BytesIO
    from flask import send_file

    month = int(request.args.get('month'))
    year = int(request.args.get('year'))
    from calendar import monthrange
    total_days = monthrange(year, month)[1]

    data = []
    for u in User.query.all():
        recs = Attendance.query.filter_by(user_id=u.id).filter(
            Attendance.date.between(date(year, month, 1), date(year, month, total_days))
        ).all()
        days_worked = len([r for r in recs if r.check_in])
        total_hours = sum([r.total_hours or 0 for r in recs])
        days_absent = total_days - days_worked
        data.append({
            'Tên nhân viên': u.username,
            'Số ngày làm': days_worked,
            'Số giờ công': total_hours,
            'Số ngày vắng': days_absent
        })

    df = pd.DataFrame(data)
    output = BytesIO()
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False, sheet_name='TongKet')
    output.seek(0)
    return send_file(output, download_name=f"tongket_{month}_{year}.xlsx", as_attachment=True)
