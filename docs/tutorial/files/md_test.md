# Documents

Một thành phần không thể thiếu trong các ứng dụng RAG là dữ liệu, chúng ta có nhiều loại dữ liệu khác nhau như: pdf, docx, csv, pptx, html, database... mỗi loại khác nhau không tuân theo một quy chuẩn chung nào. Chính vì vậy, Documents trong Llama Index được tạo ra với vai trò như một cái khuôn để chứa và đưa các loại dữ liệu về một loại cấu trúc chung.

Điểm đặc biệt trong cấu trúc của Documents là nó có thể chứa thêm các thông tin bổ xung về dữ liệu trong đó, thành phần này gọi là siêu dữ liệu(metadata). Hiểu đơn giản thì nó là các thông tin bổ xung mà chúng ta cung cấp thêm cho dữ liệu như mô tả, tóm tắt, tiêu đề... những thông tin này nhằm mục đích hỗ trợ quá trình tìm kiếm hiệu quả hơn.

Để tạo Document từ dữ liệu, cú pháp sử dụng như sau: `Document(text, metadata, id_)`
Trong đó:

    * text: dữ liệu đầu vào dạng text

    * metadata: siêu dữ liệu, thường có định dạng dictionary, thường được tạo tự động bởi thư viện.

    * id_: Chỉ số của đối tượng Document này, nó thường được tạo một cách tự động
