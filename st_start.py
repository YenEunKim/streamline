import streamlit as st

st.set_page_config(page_title="Ye Eun Kim", layout="wide")

# 페이지 상태 관리
if "page" not in st.session_state:
    st.session_state.page = "main"

def go_to(page_name):
    st.session_state.page = page_name

# 쿼리 파라미터 방식 대신 세션 방식 유지

# MAIN PAGE
if st.session_state.page == "main":
    st.markdown("<div style='text-align:center; font-size: 24px; font-weight: bold;'>Ye Eun.</div><hr>", unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        if st.button("Photography", key="photo1"):
            go_to("photo1")
        st.image("data/1.png", use_container_width=True)

    with col2:
        if st.button("Video", key="photo2"):
            go_to("photo2")
        st.image("data/2.png", use_container_width=True)

    with col3:
        if st.button("Typography", key="photo3"):
            go_to("photo3")
        st.image("data/3.png", use_container_width=True)

    with col4:
        if st.button("Branding", key="photo4"):
            go_to("photo4")
        st.image("data/4.png", use_container_width=True)

    st.markdown("<hr>", unsafe_allow_html=True)

    

    st.markdown("""
        <h2 style='text-align: center;'>Ye Eun Kim.</h2>
        <p style='text-align: center;'>
        Yeeun Kim is a designer based in Seoul, Korea. Interested in photography, video, typography, and branding.<br>
        Majoring visual communication design at Hongik University.
        </p>
    """, unsafe_allow_html=True)

# 상세 페이지 1
elif st.session_state.page == "photo1":
    st.markdown("## Ye Eun.")
    col1, col2 = st.columns(2)
    with col1:
        st.image("data/1-1.png", use_container_width=True)
    with col2:
        st.image("data/1-2.png", use_container_width=True)
    col3, col4 = st.columns(2)
    with col3:
        st.image("data/1-3.png", use_container_width=True)
    with col4:
        st.image("data/1-4.png", use_container_width=True)

    st.markdown("### Contact.")
    st.write("anna08060@gmail.com")
    st.write("instagram")
    if st.button("Back", key="back1"):
        go_to("main")

# 상세 페이지 2
elif st.session_state.page == "photo2":
    st.markdown("## Ye Eun.")
    col1, col2 = st.columns(2)
    with col1:
        st.image("data/2-1.png", use_container_width=True)
    with col2:
        st.image("data/2-2.png", use_container_width=True)
    col3, col4 = st.columns(2)
    with col3:
        st.image("data/2-3.png", use_container_width=True)
    with col4:
        st.image("data/2-4.png", use_container_width=True)

    st.markdown("### Contact.")
    st.write("anna08060@gmail.com")
    st.write("instagram")
    if st.button("Back", key="back2"):
        go_to("main")

# 상세 페이지 3
elif st.session_state.page == "photo3":
    st.markdown("## Ye Eun.")
    st.image("data/3-1.png", use_container_width=True)

    st.markdown("### Contact.")
    st.write("anna08060@gmail.com")
    st.write("instagram")
    if st.button("Back", key="back3"):
        go_to("main")

# 상세 페이지 4
elif st.session_state.page == "photo4":
    st.markdown("## Ye Eun.")
    col1, col2 = st.columns(2)
    with col1:
        st.image("data/4-1.png", use_container_width=True)
    with col2:
        st.image("data/4-2.png", use_container_width=True)

    st.markdown("### Contact.")
    st.write("anna08060@gmail.com")
    st.write("instagram")
    if st.button("Back", key="back4"):
        go_to("main")