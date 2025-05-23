import streamlit as st
# 기본 설정
st.set_page_config(page_title="TASTE pro", layout="wide")

# 상단 메뉴
st.markdown("""
<style>
.navbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
}
.menu a {
    margin: 0 10px;
    color: #000;
    text-decoration: none;
    font-weight: bold;
}
.menu a:hover {
    color: #f76c5e;
}
</style>

<div class="navbar">
    <div><h1 style="color:#f76c5e;">TASTE <span style="font-style: italic;">pro</span></h1></div>
    <div class="menu">
        <a href="#">카테고리</a>
        <a href="#">신상품</a>
        <a href="#">베스트</a>
        <a href="#">리뷰</a>
        <a href="#">이벤트</a>
        <a href="#">테이스트프로 소개</a>
        <a href="#">로그인</a>
        <a href="#">회원가입</a>
    </div>
</div>
""", unsafe_allow_html=True)

# 메인 배너
st.markdown("## 1인 가구를 위한 소분형 소스 솔루션")
st.write("모바일로도 만나보세요!")
st.button("더 알아보기")

# 소스 카테고리
st.markdown("---")
cols = st.columns(6)
sauces = ["chili sauce", "soy sauce", "seasoned salt", "gochujang", "mustard sauce", "tomato ketchup"]
colors = ["#f76c5e", "#f28d6b", "#8eaebd", "#732c2c", "#f59d5c", "#922e2e"]

for col, sauce, color in zip(cols, sauces, colors):
    with col:
        st.markdown(f"<h4 style='color:{color};text-align:center'>{sauce}</h4>", unsafe_allow_html=True)

# 하단 카드 영역
st.markdown("---")
col1, col2 = st.columns(2)

with col1:
    st.image("https://cdn.pixabay.com/photo/2015/04/08/13/13/food-712665_1280.jpg", caption="간편 레시피")
    st.markdown("### 1인 가구를 위한 간편 레시피")

with col2:
    st.image("https://cdn.pixabay.com/photo/2016/03/05/19/02/abstract-1238247_1280.jpg", caption="소분형 소스")
    st.markdown("### 1인 가구를 위한 소분형 소스")
