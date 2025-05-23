import streamlit as st
from PIL import Image
import base64

# 페이지 설정
st.set_page_config(page_title="TASTE pro", layout="wide")

# SF Pro 폰트 적용 (base64로 가져올 수도 있지만 여기선 Google Fonts로 유사한 San Francisco 대체 사용)
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;700&display=swap');

html, body, div, h1, h2, h3, p {
    font-family: 'Roboto', sans-serif;
}
.card-container {
    display: flex;
    justify-content: space-around;
    margin-top: 50px;
    margin-bottom: 80px;
}
.card {
    width: 45%;
    background: #fff2ec;
    padding: 20px;
    border-radius: 25px;
    text-align: center;
    box-shadow: 0 4px 15px rgba(0,0,0,0.05);
}
.card img {
    width: 100%;
    border-radius: 20px;
    margin-bottom: 20px;
}
.card h3 {
    font-size: 22px;
    font-weight: 700;
    margin: 0;
}
</style>
""", unsafe_allow_html=True)

# 이미지 로드
recipe_img = Image.open("Mask group.png")
sauce_img = Image.open("909090909 1.png")

# 카드 섹션
st.markdown("""
<div class="card-container">
    <div class="card">
        <img src="data:image/png;base64,%s" />
        <h3>1인 가구를 위한 간편 레시피</h3>
    </div>
    <div class="card">
        <img src="data:image/png;base64,%s" />
        <h3>1인 가구를 위한 소분형 소스</h3>
    </div>
</div>
""" % (
    base64.b64encode(recipe_img.tobytes()).decode("utf-8"),
    base64.b64encode(sauce_img.tobytes()).decode("utf-8")
), unsafe_allow_html=True)