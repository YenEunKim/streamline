import streamlit as st

# 페이지 설정 (중복 없이 맨 위에서 한 번만)
st.set_page_config(page_title="Ye Eun Kim", layout="wide")

# 사용자 정의 스타일
st.markdown("""
    <style>
    html, body, [class*="css"] {
        font-family: 'Helvetica Neue', sans-serif;
        background-color: white;
        color: #000;
    }
    a {
        text-decoration: none;
        color: inherit;
    }
    .stTextInput>div>div>input {
        background-color: white;
        border: none;
        border-bottom: 1px solid #ccc;
    }
    .gallery-img img {
        height: 300px;
        object-fit: cover;
        width: 100%;
    }
    hr {
        border: none;
        border-top: 1px solid #ccc;
        margin: 2em 0;
    }
    </style>
""", unsafe_allow_html=True)

# 세션 상태를 활용한 페이지 전환
if "page" not in st.session_state:
    st.session_state.page = "main"

# ⬇️ MAIN PAGE
if st.session_state.page == "main":
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

    # 이미지 갤러리 (1번만 버튼으로 클릭 가능)
    with st.container():
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            if st.button(" ", key="photo1_btn"):
                st.session_state.page = "photo1"
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

# ⬇️ DETAIL PAGE
elif st.session_state.page == "photo1":
    st.markdown("""
    <div style='text-align: center; font-size: 24px; font-weight: bold; margin-top: 10px; margin-bottom: 10px;'>
        Ye Eun.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<hr>", unsafe_allow_html=True)

    # 상세 이미지
    col1, col2 = st.columns(2)
    with col1:
        st.image("data/1-1.png", use_column_width=True)
    with col2:
        st.image("data/1-2.png", use_column_width=True)

    col3, col4 = st.columns(2)
    with col3:
        st.image("data/1-3.png", use_column_width=True)
    with col4:
        st.image("data/1-4.png", use_column_width=True)

    st.markdown("<br><br>", unsafe_allow_html=True)

    # Contact 정보
    st.markdown("""
    <h3 style='text-align: center;'>Contact.</h3>
    <p style='text-align: center;'>
    anna08060@gmail.com<br>
    instagram
    </p>
    """, unsafe_allow_html=True)

    # 뒤로 가기 버튼
    if st.button("Back to Home"):
        st.session_state.page = "main"
