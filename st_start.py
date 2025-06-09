import streamlit as st

st.set_page_config(page_title="Ye Eun Kim", layout="wide")

# 상태 관리
if "page" not in st.session_state:
    st.session_state.page = "main"

def go_to(page_name):
    st.session_state.page = page_name

# CSS 스타일 정의
st.markdown("""
    <style>
    .image-box {
        position: relative;
        width: 100%;
        height: auto;
    }
    .image-box img {
        width: 100%;
        height: auto;
        border-radius: 4px;
    }
    .centered-button {
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        background-color: rgba(0,0,0,0.6);
        color: white;
        padding: 10px 20px;
        border: none;
        border-radius: 12px;
        font-size: 16px;
        cursor: pointer;
    }
    .centered-button:hover {
        background-color: rgba(255,255,255,0.9);
        color: black;
    }
    </style>
""", unsafe_allow_html=True)

# 메인 페이지
if st.session_state.page == "main":
    st.markdown("<div style='text-align:center; font-size: 24px; font-weight: bold;'>Ye Eun.</div><hr>", unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)

    for i, (col, label, img, target) in enumerate(zip(
        [col1, col2, col3, col4],
        ["Photography", "Video", "Typography", "Branding"],
        ["data/1.png", "data/2.png", "data/3.png", "data/4.png"],
        ["photo1", "photo2", "photo3", "photo4"]
    )):
        with col:
            # Streamlit이 실제 클릭 처리를 하도록 숨은 버튼 생성
            if st.button(label, key=f"btn_{i}", help=label):
                go_to(target)

            # 실제 보이는 부분은 HTML 마크업
            st.markdown(f"""
            <div class="image-box">
                <img src="{img}">
                <form action="" method="post">
                    <button name="fake_btn_{i}" class="centered-button">{label}</button>
                </form>
            </div>
            """, unsafe_allow_html=True)

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