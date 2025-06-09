import streamlit as st

st.set_page_config(page_title="Ye Eun Kim", layout="wide")

# 페이지 상태 관리
if "page" not in st.session_state:
    st.session_state.page = "main"

def go_to(page_name):
    st.session_state.page = page_name

# ---------- MAIN PAGE ----------
if st.session_state.page == "main":
    st.markdown("<h2 style='text-align: center;'>Ye Eun.</h2><hr>", unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)

    # 이미지 + 버튼 반복 처리
    for i, (col, label, img_path, target) in enumerate(zip(
        [col1, col2, col3, col4],
        ["Photography", "Video", "Typography", "Branding"],
        ["data/1.png", "data/2.png", "data/3.png", "data/4.png"],
        ["photo1", "photo2", "photo3", "photo4"]
    )):
        with col:
            st.image(img_path, use_container_width=True)

            # Streamlit 버튼을 가운데 정렬
            st.markdown("<div style='text-align:center;'>", unsafe_allow_html=True)
            if st.button(label, key=f"btn_{i}"):
                go_to(target)
            st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<hr>", unsafe_allow_html=True)

    # 자기소개
    st.markdown("""
        <h2 style='text-align: center;'>Ye Eun Kim.</h2>
        <p style='text-align: center;'>
        Yeeun Kim is a designer based in Seoul, Korea. Interested in photography, video, typography, and branding.<br>
        Majoring visual communication design at Hongik University.
        </p>
    """, unsafe_allow_html=True)

# ---------- PHOTO 1 ----------
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

# ---------- PHOTO 2 (Video 포함) ----------
elif st.session_state.page == "photo2":
    st.markdown("## Ye Eun.")

    # 🎥 비디오 상단 재생
    try:
        with open("data/video.mp4", "rb") as video_file:
            st.video(video_file.read())
    except FileNotFoundError:
        st.warning("비디오 파일(data/video.mp4)을 찾을 수 없습니다.")

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

# ---------- PHOTO 3 ----------
elif st.session_state.page == "photo3":
    st.markdown("## Ye Eun.")
    st.image("data/3-1.png", use_container_width=True)

    st.markdown("### Contact.")
    st.write("anna08060@gmail.com")
    st.write("instagram")

    if st.button("Back", key="back3"):
        go_to("main")

# ---------- PHOTO 4 ----------
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