import streamlit as st

# 페이지 설정
st.set_page_config(page_title="Ye Eun Kim", layout="wide")

# 사용자 정의 스타일
st.markdown("""
    <style>
    /* 전체 폰트 변경 */
    html, body, [class*="css"] {
        font-family: 'Helvetica Neue', sans-serif;
        color: #000000;
        background-color: white;
    }

    /* 링크 스타일 초기화 */
    a {
        text-decoration: none !important;
        color: inherit !important;
    }

    /* 검색창 커스터마이징 */
    .stTextInput>div>div>input {
        background-color: white;
        border: none;
        border-bottom: 1px solid #ccc;
        padding: 4px 6px;
        font-size: 14px;
    }

    /* 상단 구분선 스타일 */
    hr {
        border: none;
        border-top: 1px solid #ccc;
        margin: 2em 0;
    }
    </style>
""", unsafe_allow_html=True)

# 상단 네비게이션
with st.container():
    cols = st.columns([1, 1, 1, 4, 1])
    with cols[0]:
        st.markdown("**Works**")
    with cols[1]:
        st.markdown("**About**")
    with cols[2]:
        st.markdown("**Contact**")
    with cols[3]:
        st.markdown("<h3 style='text-align: center;'>Ye Eun.</h3>", unsafe_allow_html=True)
    with cols[4]:
        st.text_input("Search")

st.markdown("<hr>", unsafe_allow_html=True)

# 이미지 갤러리
with st.container():
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.image("data/1.png", use_column_width=True)
    with col2:
        st.image("data/2.png", use_column_width=True)
    with col3:
        st.image("data/3.png", use_column_width=True)
    with col4:
        st.image("data/4.png", use_column_width=True)

st.markdown("<hr>", unsafe_allow_html=True)

# 자기소개 텍스트
st.markdown("""
<h2 style='text-align: center;'>Ye Eun Kim.</h2>
<p style='text-align: center;'>
Yeeun Kim is a designer based in Seoul, Korea. Interested in photography, video, typography, and branding.<br>
Majoring visual communication design at Hongik University.
</p>
""", unsafe_allow_html=True)

