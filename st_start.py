import streamlit as st
from PIL import Image
import os

st.set_page_config(page_title="TASTE pro", layout="wide")

# ----------- CSS 스타일 -----------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');

body, html {
    font-family: 'Roboto', sans-serif;
}
.navbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 20px 40px;
    border-bottom: 1px solid #eee;
}
.menu {
    display: flex;
    gap: 25px;
    align-items: center;
}
.menu a {
    text-decoration: none;
    color: #333;
    font-weight: 600;
}
.menu a:hover {
    color: #f76c5e;
}
.icons img {
    margin-left: 15px;
    width: 22px;
}
.banner {
    display: flex;
    padding: 60px 40px;
    background: #fff5f0;
    border-radius: 15px;
    margin: 30px;
}
.banner-text {
    flex: 1;
    padding-right: 40px;
}
.banner-text h1 {
    font-size: 32px;
}
.banner-text p {
    font-size: 16px;
    color: #555;
}
.banner-button {
    background-color: #f76c5e;
    color: white;
    padding: 12px 25px;
    border-radius: 30px;
    font-weight: bold;
    display: inline-block;
    margin-top: 20px;
}
.card-container {
    display: flex;
    justify-content: space-around;
    margin: 50px 40px;
}
.card {
    background-color: #fff1ea;
    border-radius: 20px;
    padding: 20px;
    text-align: center;
    width: 45%;
    box-shadow: 0 2px 10px rgba(0,0,0,0.05);
}
.card img {
    width: 100%;
    border-radius: 15px;
    margin-bottom: 15px;
}
footer {
    background-color: #fefefe;
    padding: 30px 40px;
    border-top: 1px solid #ddd;
    margin-top: 40px;
    font-size: 14px;
    color: #666;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

# ----------- 이미지 경로 로드 -----------
def load_image(name):
    return Image.open(os.path.join("images", name))

# ----------- 헤더 네비게이션 -----------
col1, col2, col3 = st.columns([1, 6, 1])
with col1:
    st.image(load_image("logo.png"), width=120)
with col2:
    st.markdown("""
    <div class="menu">
        <a href="#">카테고리</a>
        <a href="#">신상품</a>
        <a href="#">베스트</a>
        <a href="#">리뷰</a>
        <a href="#">이벤트</a>
        <a href="#">테이스트포 소개</a>
    </div>
    """, unsafe_allow_html=True)
with col3:
    st.markdown("""
    <div class="icons">
        <img src="images/icon_search.png">
        <img src="images/icon_cart.png">
        <img src="images/icon_user.png">
    </div>
    """, unsafe_allow_html=True)
