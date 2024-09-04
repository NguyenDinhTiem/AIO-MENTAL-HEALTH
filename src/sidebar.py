import streamlit as st

def show_sidebar():
    st.sidebar.image("data/images/logo.png", use_column_width=True)
    st.sidebar.markdown('### 🧠 Ứng dụng AI chăm sóc sức khỏe tâm thần của bạn theo DSM-5. ')

    st.sidebar.markdown('Hướng dẫn sử dụng:')
    st.sidebar.markdown('1. 🟢 **Đăng nhập tài khoản.**')
    st.sidebar.markdown('2. 💬 **Sử dụng chức năng chat - "Nói chuyện với chuyên gia tâm lý AI" để chia sẻ cảm xúc của bạn.**')
    st.sidebar.markdown('3. 📈 **Khi có đủ dữ liệu hoặc bạn kết thúc cuộc trò chuyện. Chuyên gia AI sẽ chuẩn đoán tình trạng sức khỏe tinh thần của bạn theo DSM5.**')
    st.sidebar.markdown('4. 📊 **Tình trạng sức khỏe tinh thần của bạn sẽ được lưu lại. Bạn có thể sử dụng chức năng user - "Theo dõi thông tin sức khỏe của bạn" để xem thống kê chi tiết về tình trạng sức khỏe tinh thần của mình.**')
    st.sidebar.markdown('📝 Product by AI VIET NAM.')