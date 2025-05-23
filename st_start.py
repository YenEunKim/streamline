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


st.markdown("---")

# 자기소개 텍스트
st.markdown("""
<h2 style='text-align: center;'>Ye Eun Kim.</h2>
<p style='text-align: center;'>
Yeeun Kim is a designer based in Seoul, Korea. Interested in photography, video, typography, and branding.<br>
Majoring visual communication design at Hongik University.
</p>
""", unsafe_allow_html=True)