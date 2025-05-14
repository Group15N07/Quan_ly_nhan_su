# Đề xuất dự án: Ứng dụng quản lý nhân sự tích hợp chấm công bằng nhận diện khuôn mặt

## 1. Giới thiệu tổng quan
Trong bối cảnh số hóa doanh nghiệp ngày càng phát triển, việc xây dựng một hệ thống quản lý nhân sự là điều cần thiết. Đề tài hướng đến việc thiết kế một ứng dụng hỗ trợ quản lý nhân sự hiệu quả, tích hợp nhận diện khuôn mặt bằng **Scrfd** để phát hiện và **arcface** để chấm công tự động, tăng tính bảo mật và minh bạch.

Hệ thống còn áp dụng **game hóa** để tạo động lực làm việc, đồng thời đáp ứng yêu cầu **mở rộng**, **bảo mật** và **trải nghiệm người dùng hiện đại**.

## 2. Tầm nhìn và lý do phát triển
Nhóm chúng em xây dựng ứng dụng nhằm hỗ trợ các doanh nghiệp vừa và nhỏ hiện đại hóa công tác quản lý nhân sự, vốn thường gặp khó khăn trong việc theo dõi hồ sơ, chấm công và đánh giá hiệu suất.

Hệ thống tích hợp chấm công bằng **nhận diện khuôn mặt kết hợp GPS**, giúp quản lý minh bạch và chống gian lận. Ngoài ra, ứng dụng còn **game hóa** quá trình làm việc, tạo động lực, tăng sự gắn kết giữa nhân viên và doanh nghiệp mà không cần đầu tư vào hệ thống cồng kềnh, phức tạp.

## 3. Đối tượng hướng đến
- Các mô hình doanh nghiệp, công ty vừa và nhỏ  
- Công ty cần quản lý nhân sự đơn giản, tiết kiệm chi phí  
- Các tổ chức chưa có hệ thống quản lý nhân sự chuyên nghiệp  

## 4. Chức năng chính
- Chấm công bằng nhận diện khuôn mặt  
- Quản lý hồ sơ nhân viên: lưu trữ, tra cứu thông tin nhân viên  
- Thông báo và nhắc nhở: Tự động gửi thông báo công việc, sinh nhật, kỷ niệm làm việc  
- Phân quyền truy cập: admin, HR, nhân viên  

## 5. Kiến trúc phần mềm
### Thành phần chính
- **Frontend**: Giao diện người dùng (đăng nhập, quản lý, nhân sự, chấm công…)  
- **Database**: Lưu trữ thông tin nhân viên, phòng ban…

### Công nghệ sử dụng
- **Frontend**: HTML, Python, CSS  
- **Database**: MySQL  

## 6. Mô hình tương tác người dùng
### Quản trị viên
- Quản lý nhân sự,thêm, sửa, xóa, phòng ban, chấm công, lương  
### Quản lý
- Quản lý nhân sự, chấm công, quản lý phòng ban

### Nhân viên
- Đăng nhập, chấm công, xem lịch sử làm việc, bảng lương  

## 7. MVP và định hướng phát triển
### Chức năng MVP
- Đăng nhập/Đăng xuất  
- Quản lý nhân sự, phòng ban  
- Chấm công, theo dõi lịch làm  
- Xem bảng lương cơ bản  

### Mục tiêu
- Đưa sản phẩm trở thành giải pháp hữu ích cho doanh nghiệp vừa và nhỏ  
- Tiết kiệm thời gian, chi phí cho các doanh nghiệp  
- Cải tiến nâng cao thêm các chức năng: backend và tích hợp AI  

