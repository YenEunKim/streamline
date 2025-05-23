import streamlit as st

# 페이지 설정
st.set_page_config(page_title="Ye Eun Kim", layout="wide")

# 상단 네비게이션
with st.container():
    cols = st.columns([1, 1, 1, 4, 1])
    with cols[0]:
        st.markdown("[Works](#)")
    with cols[1]:
        st.markdown("[About](#)")
    with cols[2]:
        st.markdown("[Contact](#)")
    with cols[3]:
        st.markdown("<h3 style='text-align: center;'>Ye Eun.</h3>", unsafe_allow_html=True)
    with cols[4]:
        st.text_input("Search")

st.markdown("---")

# 이미지 갤러리
with st.container():
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.image("image1.jpg", use_column_width=True)
    with col2:
        st.image("image2.jpg", use_column_width=True)
    with col3:
        st.image("image3.jpg", use_column_width=True)
    with col4:
        st.image("image4.jpg", use_column_width=True)

st.markdown("---")

# 자기소개 텍스트
st.markdown("""
<h2 style='text-align: center;'>Ye Eun Kim.</h2>
<p style='text-align: center;'>
Yeeun Kim is a designer based in Seoul, Korea. Interested in photography, video, typography, and branding.<br>
Majoring visual communication design at Hongik University.
</p>
""", unsafe_allow_html=True)