import streamlit as st
# 페이지 세팅
st.set_page_config(page_title="TASTE pro", layout="wide")

# CSS 삽입
st.markdown("""
<style>
body {
    font-family: 'Pretendard', sans-serif;
    background-color: #fff;
}
.header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 30px 50px;
    border-bottom: 1px solid #eee;
}
.logo {
    font-size: 30px;
    font-weight: bold;
    color: black;
}
.logo span {
    color: #f76c5e;
    font-style: italic;
}
.menu {
    display: flex;
    gap: 20px;
}
.menu a {
    font-weight: 500;
    text-decoration: none;
    color: #333;
}
.menu a:hover {
    color: #f76c5e;
}
.banner {
    background: linear-gradient(to right, #fff5f0, #fbe3db);
    padding: 60px;
    text-align: left;
}
.banner h1 {
    font-size: 32px;
    margin-bottom: 15px;
}
.banner p {
    font-size: 18px;
    color: #444;
}
.button {
    display: inline-block;
    padding: 10px 30px;
    background-color: #f76c5e;
    color: white;
    border-radius: 30px;
    font-weight: bold;
    margin-top: 20px;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

# HTML 구조
st.markdown("""
<div class="header">
    <div class="logo">TASTE <span>po</span></div>
    <div class="menu">
        <a href="#">카테고리</a>
        <a href="#">신상품</a>
        <a href="#">베스트</a>
        <a href="#">리뷰</a>
        <a href="#">이벤트</a>
        <a href="#">테이스트포 소개</a>
        <a href="#">로그인</a>
        <a href="#">회원가입</a>
    </div>
</div>

<div class="banner">
    <h1>1인 가구를 위한 소분형 소스 솔루션</h1>
    <p>모바일로도 만나보세요!</p>
    <div class="button">더 알아보기</div>
</div>
""", unsafe_allow_html=True)