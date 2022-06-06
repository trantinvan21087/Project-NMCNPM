<h1 align="center">ĐỒ ÁN NHẬP MÔN CÔNG NGHỆ PHẦN MỀM</h1>

<h2 align="center">ĐỀ TÀI QUẢN LÝ HỌC SINH</h2>

<h3 align="center">GVHD: Bùi Tấn Lộc</h3>


### 1. Giới thiệu project 
Hiện tại, giáo dục và công nghệ hoá đang là một trong những xu hướng toàn cầu. Vì giáo dục luôn được thực hiện và xuyên suốt, nên loại phần mềm quản lý học sinh sẽ đáp ứng được xu thế hiện đại hoá và nhu cầu giáo dục hiện nay.

### 2. Thông tin thành viên
| Họ và tên | MSSV | Lớp |
| --- | --- | --- |
| Trần Tín Văn | 19120714 | 19_22 |
| Đỗ Nhật Toàn | 19120688 | 19_22 |
| Đinh Nhật Tường | 19120709 | 19_22 |
| Đào Xuân Tùng | 19120707 | 19_22 |
| Mai Dương Nguyên Trường | 19120698 | 19_22 |

### 3. Thông tin môi trường <!-- Môi trường thực thi (phiên bản hệ điều hành, SDK, Dev Tools, cơ sở dữ liệu, etc.) -->
Đồ án này được xây dựng bằng Django v4.0.4 và ngôn ngữ Python 3.9.7, hỗ trợ cho cả Linux và Windows nhưng tập trung chủ yếu vào Windows 10.

### 4. Cấu hình  <!-- Hướng dẫn cấu hình project chạy local PC. -->
Local PC cần phải tối thiểu cài đặt được Django và Python để chạy đồ án này. Sau khi tải source đồ án, tiến hành cd đến thư mục Project-NMCNPM/SM/ và chạy lệnh `python manage.py runserver` để chạy server tại localhost.

### 5. Hướng dẫn deploy  <!-- Hướng dẫn deploy project lên Heroku, Netlify, etc. (có thể bổ sung cho đến present cuối kỳ) -->
Deploy sử dụng Heroku.

Tải và cài đặt git,heroku cli:
![image](https://user-images.githubusercontent.com/74363485/172088514-84234e5b-78e1-4f38-8bcf-dc63b96e5f09.png)

Đăng kí và đăng nhập tài khoản heroku trên web:
![image](https://user-images.githubusercontent.com/74363485/172088563-e0cf79a1-3ca2-4163-bbc1-cd32b0283d64.png)

Sử dụng git clone repo từ github về và di chuyển đến đó:
![image](https://user-images.githubusercontent.com/74363485/172088643-7105c7f0-9014-4957-b244-1ff9508d703b.png)

Đăng nhập heroku thông qua terminal:
![image](https://user-images.githubusercontent.com/74363485/172047823-dd2f95e1-baf3-4fd3-810b-e44da06a24ee.png)

Tạo app heroku:
![image](https://user-images.githubusercontent.com/74363485/172047924-6057cce3-0498-49f9-b2d4-5acaf902f7b5.png)

Tạo 1 file requirements.txt ở cùng thư mục project có chứa đầy đủ module của Python app:
![image](https://user-images.githubusercontent.com/74363485/172088353-98a65e1d-24ee-4396-a2c0-706898e9d0ea.png)

Tạo 1 procfile cho python app:
![image](https://user-images.githubusercontent.com/74363485/172088773-e096c085-cfa7-43db-b4c3-16f017c95866.png)

Tiến hành deploy app lên heroku:
![image](https://user-images.githubusercontent.com/74363485/172088711-06f7154a-9dd4-4399-aa74-6faeb79c803a.png)

Sử dụng lệnh log để kiểm tra log và lỗi nếu có:
![image](https://user-images.githubusercontent.com/74363485/172089271-61c05bf4-d94d-4a57-b658-9ae791f71210.png)

Truy cập tới trang web của app đã deploy lên heroku:
![image](https://user-images.githubusercontent.com/74363485/172088906-2eeeee0d-6289-4adb-8737-f040f411c6a0.png)

Vào trang web Heroku để quản lý tài nguyên của app:
![image](https://user-images.githubusercontent.com/74363485/172089149-323df58b-e0ea-4cde-81cc-9ac41e96eebe.png)


### 6. Link demo project <!-- Link Google Drive hoặc Youtube video demo (có thể bổ sung cho đến present cuối kỳ) -->
[Google Drive](https://drive.google.com/drive/folders/1ibR6lSzFQP0H9uKOjFmbjEPT_IfP_PN-?usp=sharing) (TBA)

### 7. Current status  <!-- Current status: tóm tắt những gì đã hoàn thành (có thể bổ sung cho đến present cuối kỳ) -->
TBA

### 8. Future work  <!-- Future works: tóm tắt những gì cần làm thêm (có thể bổ sung cho đến present cuối kỳ) -->
TBA

### 9. Nguồn tham khảo  <!-- Tham khảo chéo các project liên quan nếu có (backend thì giới thiệu link tham khảo frontend và ngược lại) -->
TBA 

