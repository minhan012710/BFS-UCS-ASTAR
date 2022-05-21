# Bài tập cài đặt thuật toán điều khiển xe oto thoát khỏi maze

- File định dạng đầu vào: 

Dòng đầu tiên 3 số là N kích thước của maze, số bức tường (có thể trùng nhau)
và giá trị Vmax.

Dòng thứ hai là giá trị vị trí xuất phát và vị trí kết thúc (theo thứ tự dòng - cột).
Xe luôn xuất phát ở hướng bắc.

Sau đó là các dòng ghi vị trí (x1, y1) và (x2, y2) thể hiện
có 1 bức tường nối 2 ô (x1, y1) và (x2, y2), với x1, x2 là dòng, y1, y2 là cột.
Các ô đánh số theo thứ tự từ 0 đến N-1
 

- Question 1: Đọc hiểu chương trình `car_bfs.py` và `mktest_car.py`. Cài đặt phần tính
chi phí đường đi tìm được bằng BFS, công thức `cost = 1 + sqrt(v)` với `v` là giá trị
vận tốc tại vị trí hiện tại

- Question 2: Cài đặt thuật toán UCS `car_ucs.py`, yêu cầu in ra màn hình 
thông tin tương tự `car_bfs.py` 

- Question 3: Cài đặt thuật toán A* theo gợi ý trên lớp, yêu cầu in ra màn hình 
thông tin tương tự `car_bfs.py`. Bạn có cải tiến gì để giảm số lượng đỉnh được
tìm kiếm trong trường hợp này

Lưu ý: Điền đầy đủ thông tin ở code và nộp lại theo thư mục mssv_hovaten.zip cả 3 file bài tập.