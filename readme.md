<p align="center">
  <img src="https://github.com/NguyenDinhTiem/AIO-MENTAL-HEALTH/blob/09100bbbff16a633912288ff3c4c031e9f7dac8b/data/images/logo.png" alt="">
</p>

# AIO MENTAL HEALTH - DỰ ÁN CHĂM SÓC SỨC KHỎE TINH THẦN CHO NGƯỜI VIỆT

## 1. Hướng dẫn cài đặt
### Tải mã nguồn về máy
```python
git clone https://github.com/NguyenDinhTiem/AIO-MENTAL-HEALTH.git
```
### Tạo môi trường và kích hoạt môi trường
```python
conda create -n aio_env python=3.11
conda activate aio_env
```
### Tạo OPENAI API KEY
Tạo thư mục /.streamlit/secrets.toml, nhập thông tin API vào file này.
```python
[openai]
OPENAI_API_KEY = "sk-your-api-key"
```
### Cài đặt các thư viện
```python
pip install -r requirements.txt
```
### Chạy ứng dụng
```python
streamlit run Home.py
```
### Để tinh chỉnh ứng dụng vui lòng xem hướng dẫn tại đây: 

2. Hệ thống
![Hệ thống thực hiện trò chuyện với người dùng (1)(2), phân tích và chẩn đoán (3), theo dõi tiến trình sức khỏe (4)](data/images/2.simple-pipeline.png)
![Quy trình xử lí dữ liệu, dữ liệu thô được xử lí bởi Ingest Pipeline(1), quy trình xử lí được lưu lại tại bộ nhớ cache(2), sau đó quá trình tạo index và lưu trữ tại kho index(3)](data/images/2.quy-trinh-xu-li-du-lieu.png)
![Agent quản lí lịch sử trò chuyện và sử dụng các công cụ truy vấn DMS5 và công cụ lưu trữ kết quả chẩn đoán.](data/images/2.tao-agent.png)
![Luồng hoạt động của ứng dụng](data/images/2.xay-dung-app.png)

3. Demo
Bạn có thể trải nghiệm ứng dụng tại đây: https://aio-mentalhealth.streamlit.app/

![Demo1](data/images/demo1.png)
![Demo1](data/images/demo2.png)
![Demo1](data/images/demo3.png)
![Demo1](data/images/demo4.png)